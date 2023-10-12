using System;
using System.Linq;
using System.Threading.Tasks;
using InfluxDB.Client;
using InfluxDB.Client.Api.Domain;
using InfluxDB.Client.Core;
using InfluxDB.Client.Writes;

namespace Examples
{
  public class Examples
  {
    public static async Task Main(string[] args)
    {
      // You can generate an API token from the "API Tokens Tab" in the UI
      var token = Environment.GetEnvironmentVariable("INFLUX_TOKEN")!;
      const string bucket = "scs_demo";
      const string org = "ORG";

      using var client = new InfluxDBClient("http://localhost:8086", token);

      const string data = "mem,host=host1 used_percent=23.43234543";
      using (var writeApi = client.GetWriteApi())
      {
          writeApi.WriteRecord(bucket, org, WritePrecision.Ns, data);
      }
    }
  }
}



