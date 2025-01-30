# EmissionsForecastBatchParametersDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_at** | **datetime** | For historical forecast requests, this value is the timestamp used to access the most  recently generated forecast as of that time. | [optional] 
**location** | **str** | The location of the forecast | [optional] 
**data_start_at** | **datetime** | Start time boundary of forecasted data points.Ignores current forecast data points before this time.  Defaults to the earliest time in the forecast data. | [optional] 
**data_end_at** | **datetime** | End time boundary of forecasted data points. Ignores current forecast data points after this time.  Defaults to the latest time in the forecast data. | [optional] 
**window_size** | **int** | The estimated duration (in minutes) of the workload.  Defaults to the duration of a single forecast data point. | [optional] 

## Example

```python
from openapi_client.models.emissions_forecast_batch_parameters_dto import EmissionsForecastBatchParametersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EmissionsForecastBatchParametersDTO from a JSON string
emissions_forecast_batch_parameters_dto_instance = EmissionsForecastBatchParametersDTO.from_json(json)
# print the JSON string representation of the object
print(EmissionsForecastBatchParametersDTO.to_json())

# convert the object into a dict
emissions_forecast_batch_parameters_dto_dict = emissions_forecast_batch_parameters_dto_instance.to_dict()
# create an instance of EmissionsForecastBatchParametersDTO from a dict
emissions_forecast_batch_parameters_dto_from_dict = EmissionsForecastBatchParametersDTO.from_dict(emissions_forecast_batch_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


