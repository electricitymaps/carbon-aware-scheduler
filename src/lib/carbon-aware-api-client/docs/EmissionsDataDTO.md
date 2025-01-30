# EmissionsDataDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 
**duration** | **int** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from openapi_client.models.emissions_data_dto import EmissionsDataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of EmissionsDataDTO from a JSON string
emissions_data_dto_instance = EmissionsDataDTO.from_json(json)
# print the JSON string representation of the object
print(EmissionsDataDTO.to_json())

# convert the object into a dict
emissions_data_dto_dict = emissions_data_dto_instance.to_dict()
# create an instance of EmissionsDataDTO from a dict
emissions_data_dto_from_dict = EmissionsDataDTO.from_dict(emissions_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


