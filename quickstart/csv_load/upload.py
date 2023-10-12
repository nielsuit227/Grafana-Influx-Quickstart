import os

from influx.api import InfluxAPI

file_loc = "<FILE_LOC>"
time_col = "<TIME_COL>"

org = "<ORG>"
url = "<URL>"
bucket = "<BUCKET>"
measurement = "<MEASUREMENT>"
tags = ["<TAG>", "<TAG>"]
token = os.environ.get("INFLUXDB_TOKEN")


api = InfluxAPI(
    org=org, url=url, bucket=bucket, measurement=measurement, tags=tags, token=token
)
api.upload_csv(file_loc)
