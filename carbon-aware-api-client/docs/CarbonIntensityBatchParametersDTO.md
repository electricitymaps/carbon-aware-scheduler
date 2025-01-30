# CarbonIntensityBatchParametersDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | The location name where workflow is run | [optional] 
**start_time** | **datetime** | The time at which the workflow we are measuring carbon intensity for started | [optional] 
**end_time** | **datetime** | The time at which the workflow we are measuring carbon intensity for ended | [optional] 

## Example

```python
from openapi_client.models.carbon_intensity_batch_parameters_dto import CarbonIntensityBatchParametersDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CarbonIntensityBatchParametersDTO from a JSON string
carbon_intensity_batch_parameters_dto_instance = CarbonIntensityBatchParametersDTO.from_json(json)
# print the JSON string representation of the object
print(CarbonIntensityBatchParametersDTO.to_json())

# convert the object into a dict
carbon_intensity_batch_parameters_dto_dict = carbon_intensity_batch_parameters_dto_instance.to_dict()
# create an instance of CarbonIntensityBatchParametersDTO from a dict
carbon_intensity_batch_parameters_dto_from_dict = CarbonIntensityBatchParametersDTO.from_dict(carbon_intensity_batch_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


