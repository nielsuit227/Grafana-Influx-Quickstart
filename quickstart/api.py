import os
from typing import Any

import pandas as pd
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


class InfluxAPI:
    def __init__(
        self,
        org: str,
        url: str,
        bucket: str,
        token: str,
        measurement: str,
        tags: list[str] | None = None,
    ):
        self.org = org
        self.bucket = bucket
        self.measurement = measurement
        self.tags = tags if tags is not None else []
        self.client = InfluxDBClient(url=url, token=token, org=org)
        self.write_api = self.client.write_api(write_options=SYNCHRONOUS)

    def write(self, point: Point) -> None:
        for tag in self.tags:
            point.tag(*tag)
        self.write_api.write(bucket=self.bucket, org=self.org, record=point)

    def upload_dict(self, data: dict[str, Any]) -> None:
        """Uploads a dictionary to InfluxDB"""
        point = Point(self.measurement)
        for k, v in data.items():
            point.field(k, v)
        self.write(point)

    def upload_csv(self, file_loc: str, time_col: str | None = None) -> None:
        """Uploads a csv to InfluxDB given a file location.
        Given the nature of a CSV upload, it is HIGHLY RECOMMENDED to provide
        a time_col to set the time, as otherwise, the upload time will be used.
        """
        if not os.path.exists(file_loc):
            raise FileNotFoundError(f"File does not exist: {file_loc}")

        df = pd.read_csv(file_loc, parse_dates=time_col is not None, index_col=time_col)

        for i, row in df.iterrows():
            self.upload_dict(row.to_dict())

    def upload_line_protocol(self, file_loc: str, line_by_line: bool = False) -> None:
        """https://docs.influxdata.com/influxdb/cloud/reference/syntax/line-protocol/"""
        if not os.path.exists(file_loc):
            raise FileExistsError(f"File does not exist: {file_loc}")

        if line_by_line:
            for line in open(file_loc, "r"):
                self.write_api.write([line], protocol="line")

        else:
            with open(file_loc, "r") as f:
                data = f.readlines()
                self.write_api.write(data, batch_size=1000, protocol="line")
