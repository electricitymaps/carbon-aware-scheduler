# CarbonIntensityDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | the location name where workflow is run | [optional] 
**start_time** | **datetime** | the time at which the workflow we are measuring carbon intensity for started | [optional] 
**end_time** | **datetime** | the time at which the workflow we are measuring carbon intensity for ended | [optional] 
**carbon_intensity** | **float** | Value of the marginal carbon intensity in grams per kilowatt-hour. | [optional] 

## Example

```python
from openapi_client.models.carbon_intensity_dto import CarbonIntensityDTO

# TODO update the JSON string below
json = "{}"
# create an instance of CarbonIntensityDTO from a JSON string
carbon_intensity_dto_instance = CarbonIntensityDTO.from_json(json)
# print the JSON string representation of the object
print(CarbonIntensityDTO.to_json())

# convert the object into a dict
carbon_intensity_dto_dict = carbon_intensity_dto_instance.to_dict()
# create an instance of CarbonIntensityDTO from a dict
carbon_intensity_dto_from_dict = CarbonIntensityDTO.from_dict(carbon_intensity_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


