# Grafana-InfluxDB Quickstart Visualization

This repository provides a quickstart guide to setting up Grafana with InfluxDB using Docker. The repo includes data publishers in multiple languages including Python, JS, Java, and C++. Dive into an interactive experience and understand InfluxDB's data format with ease.

## Table of Contents

1. [Installation Instructions](#installation-instructions)
2. [InfluxDB Data Format](#influxdb-data-format)
3. [Data Upload Formats](#data-upload-formats)
4. [Contributions & Pull Requests](#contributions--pull-requests)

## Installation Instructions

### 1. Install Docker

First and foremost, ensure you have Docker installed. If not, follow the [official Docker documentation](https://docs.docker.com/get-docker/) to set it up for your OS.

### 2. Clone the Repository

```bash
git clone https://github.com/nielsuit227/grafana-influxdb-quickstart.git
cd grafana-influxdb-quickstart
```

### 3. Run Docker Compose

Using the provided `docker-compose.yml` file, set up Grafana and InfluxDB:

```bash
docker-compose up -d
```

### 4. Check it out

You can check out Influx on `http://localhost:8086`, logging in with username and password `admin`.
You can check out Grafana on `http://localhost:3000`, logging in with username and password `admin`.

### 5. Add Data to InfluxDB

Here you have two options, we provided already scripts in four common languages to publish to Influx, for which you
only need to add the data locations & credentials.
Furthermore, if you go to Influx and add upload data, an interface opens with even more instructions on how to add data
into Influx.
It's definitely recommended to check this out!

> **Note:** Make sure to add your dependencies when using local scripts :)

## InfluxDB Data Format

InfluxDB uses a unique data format that consists of:

- **Measurement:** The concept similar to a SQL table. Represents a specific category.
- **Tags:** Indexed metadata with a series of key-value pairs. Useful for querying and filtering.
- **Fields:** Non-indexed metadata with a series of key-value pairs. This is where actual data goes.
- **Time:** Timestamp for the data point. InfluxDB automatically generates this if not provided.

## Data Upload Formats

InfluxDB supports two primary data upload formats:

1. **Line Protocol:** A text-based format. An example can be found in `tests/files/test.lp` It's structured as:

```
<measurement>,<tag_key>=<tag_value> <field_key>=<field_value> <timestamp>
```

2. **CSV Format:** Comma-separated values.

> :warning: **WARNING** When you upload CSVs direclty in the Influx interface, ensure your CSV follows the InfluxDB data model (Measurement, Tags, Fields, Time).

### 6. Create a Dashboard

Once logged in:

1. Click on the '+' icon on the left sidebar and choose 'Dashboard'.
2. Add a panel and select InfluxDB as the data source.
3. Craft your queries, design your dashboard, and enjoy the visualizations!

## Contributions & Pull Requests

We encourage the community to contribute, especially in sharing Grafana dashboard samples that might be useful to others. If you'd like to add to our collection:

1. Fork the repository.
2. Create your feature branch: `git checkout -b my-new-dashboard`
3. Commit your changes: `git commit -am 'Add my new dashboard'`
4. Push to the branch: `git push origin my-new-dashboard`
5. Submit a pull request!

---

Enjoy your Grafana-InfluxDB experience, and don't hesitate to raise an issue or ask questions!
