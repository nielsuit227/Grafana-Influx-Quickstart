repl.repl.ignoreUndefined = true;

const { InfluxDB, Point } = require("@influxdata/influxdb-client");

const token = "<TOKEN>";
const url = "<URL";
const org = "<ORG>";
const bucket = "<BUCKET>";

const client = new InfluxDB({ url, token });
const writeClient = client.getWriteApi(org, bucket, "ns");

const point = new Point("measurement1")
  .tag("tagname1", "tagvalue1")
  .intField("field1", i);
writeClient.writePoint(point);
writeClient.flush();
