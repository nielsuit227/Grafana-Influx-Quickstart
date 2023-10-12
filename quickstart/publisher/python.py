import os

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "<ORG>"
url = "<URL>"
bucket = "<BUCKET>"
measurement = "<MEASUREMENT>"
tags = [("<TAG_KEY>", "<TAG_VALUE>")]
data = {"<KEY>": "<VALUE>"}


client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

point = Point(measurement)
for tag in tags:
    point.tag(*tag)
for k, v in data.items():
    point.field(k, v)

write_api.write(bucket=bucket, org=org, record=point)
