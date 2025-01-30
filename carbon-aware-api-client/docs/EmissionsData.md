# EmissionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**time** | **datetime** |  | [optional] 
**rating** | **float** |  | [optional] 
**duration** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.emissions_data import EmissionsData

# TODO update the JSON string below
json = "{}"
# create an instance of EmissionsData from a JSON string
emissions_data_instance = EmissionsData.from_json(json)
# print the JSON string representation of the object
print(EmissionsData.to_json())

# convert the object into a dict
emissions_data_dict = emissions_data_instance.to_dict()
# create an instance of EmissionsData from a dict
emissions_data_from_dict = EmissionsData.from_dict(emissions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


