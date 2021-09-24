# Api Solar Forecast

## Read me first

### Rest commands

The following guides illustrate how to access the end points from REST communication.

* To do a POST requisition to:

  > http://<URL_SERVICE>/<SERVICE_NAME> [api_status or forecast]/<CSV_NAME> [if the service is csv]
* The json object is:

```json
{
  "address": "address",
  "start_year": 2016,
  "end_year": 2020
}
```