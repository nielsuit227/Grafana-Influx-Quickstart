import os

from quickstart.api import InfluxAPI

org = "org"
url = "http://localhost:8086"
bucket = "scs_demo"
measurement = "Test1"
tags = [("sn", "40112")]
data = {"voltage_a": 301.2}
token = os.getenv("INFLUX_DB_TOKEN")


def test_api():
    api = InfluxAPI(
        org=org, url=url, bucket=bucket, token=token, measurement=measurement, tags=tags
    )

    # api.upload_csv("quickstart/test/files/test.csv")
    api.upload_line_protocol("quickstart/test/files/test.lp")
