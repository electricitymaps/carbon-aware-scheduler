# openapi_client.CarbonAwareApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_forecast_data_async**](CarbonAwareApi.md#batch_forecast_data_async) | **POST** /emissions/forecasts/batch | Given an array of historical forecasts, retrieves the data that contains  forecasts metadata, the optimal forecast and a range of forecasts filtered by the attributes [start...end] if provided.
[**get_average_carbon_intensity**](CarbonAwareApi.md#get_average_carbon_intensity) | **GET** /emissions/average-carbon-intensity | Retrieves the measured carbon intensity data between the time boundaries and calculates the average carbon intensity during that period.
[**get_average_carbon_intensity_batch**](CarbonAwareApi.md#get_average_carbon_intensity_batch) | **POST** /emissions/average-carbon-intensity/batch | Given an array of request objects, each with their own location and time boundaries, calculate the average carbon intensity for that location and time period   and return an array of carbon intensity objects.
[**get_best_emissions_data_for_locations_by_time**](CarbonAwareApi.md#get_best_emissions_data_for_locations_by_time) | **GET** /emissions/bylocations/best | Calculate the best emission data by list of locations for a specified time period.
[**get_current_forecast_data**](CarbonAwareApi.md#get_current_forecast_data) | **GET** /emissions/forecasts/current | Retrieves the most recent forecasted data and calculates the optimal marginal carbon intensity window.
[**get_emissions_data_for_location_by_time**](CarbonAwareApi.md#get_emissions_data_for_location_by_time) | **GET** /emissions/bylocation | Calculate the best emission data by location for a specified time period.
[**get_emissions_data_for_locations_by_time**](CarbonAwareApi.md#get_emissions_data_for_locations_by_time) | **GET** /emissions/bylocations | Calculate the observed emission data by list of locations for a specified time period.


# **batch_forecast_data_async**
> List[EmissionsForecastDTO] batch_forecast_data_async(emissions_forecast_batch_parameters_dto=emissions_forecast_batch_parameters_dto)

Given an array of historical forecasts, retrieves the data that contains  forecasts metadata, the optimal forecast and a range of forecasts filtered by the attributes [start...end] if provided.

This endpoint takes a batch of requests for historical forecast data, fetches them, and calculates the optimal   marginal carbon intensity windows for each using the same parameters available to the '/emissions/forecasts/current'  endpoint.                This endpoint is useful for back-testing what one might have done in the past, if they had access to the   current forecast at the time.

### Example


```python
import openapi_client
from openapi_client.models.emissions_forecast_batch_parameters_dto import EmissionsForecastBatchParametersDTO
from openapi_client.models.emissions_forecast_dto import EmissionsForecastDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarbonAwareApi(api_client)
    emissions_forecast_batch_parameters_dto = [openapi_client.EmissionsForecastBatchParametersDTO()] # List[EmissionsForecastBatchParametersDTO] | Array of requested forecasts. (optional)

    try:
        # Given an array of historical forecasts, retrieves the data that contains  forecasts metadata, the optimal forecast and a range of forecasts filtered by the attributes [start...end] if provided.
        api_response = api_instance.batch_forecast_data_async(emissions_forecast_batch_parameters_dto=emissions_forecast_batch_parameters_dto)
        print("The response of CarbonAwareApi->batch_forecast_data_async:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarbonAwareApi->batch_forecast_data_async: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emissions_forecast_batch_parameters_dto** | [**List[EmissionsForecastBatchParametersDTO]**](EmissionsForecastBatchParametersDTO.md)| Array of requested forecasts. | [optional] 

### Return type

[**List[EmissionsForecastDTO]**](EmissionsForecastDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested forecast objects |  -  |
**400** | Returned if any of the input parameters are invalid |  -  |
**500** | Internal server error |  -  |
**501** | Returned if the underlying data source does not support forecasting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_average_carbon_intensity**
> CarbonIntensityDTO get_average_carbon_intensity(location, start_time, end_time)

Retrieves the measured carbon intensity data between the time boundaries and calculates the average carbon intensity during that period.

This endpoint is useful for reporting the measured carbon intensity for a specific time period in a specific location.

### Example


```python
import openapi_client
from openapi_client.models.carbon_intensity_dto import CarbonIntensityDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarbonAwareApi(api_client)
    location = 'eastus' # str | The location name where workflow is run
    start_time = '2022-03-01T15:30:00Z' # datetime | The time at which the workflow we are measuring carbon intensity for started
    end_time = '2022-03-01T18:30:00Z' # datetime | The time at which the workflow we are measuring carbon intensity for ended

    try:
        # Retrieves the measured carbon intensity data between the time boundaries and calculates the average carbon intensity during that period.
        api_response = api_instance.get_average_carbon_intensity(location, start_time, end_time)
        print("The response of CarbonAwareApi->get_average_carbon_intensity:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarbonAwareApi->get_average_carbon_intensity: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| The location name where workflow is run | 
 **start_time** | **datetime**| The time at which the workflow we are measuring carbon intensity for started | 
 **end_time** | **datetime**| The time at which the workflow we are measuring carbon intensity for ended | 

### Return type

[**CarbonIntensityDTO**](CarbonIntensityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a single object that contains the information about the request and the average marginal carbon intensity |  -  |
**400** | Returned if any of the requested items are invalid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_average_carbon_intensity_batch**
> List[CarbonIntensityDTO] get_average_carbon_intensity_batch(carbon_intensity_batch_parameters_dto=carbon_intensity_batch_parameters_dto)

Given an array of request objects, each with their own location and time boundaries, calculate the average carbon intensity for that location and time period   and return an array of carbon intensity objects.

The application only supports batching across a single location with different time boundaries. If multiple locations are provided, an error is returned.  For each item in the request array, the application returns a corresponding object containing the location, time boundaries, and average marginal carbon intensity.

### Example


```python
import openapi_client
from openapi_client.models.carbon_intensity_batch_parameters_dto import CarbonIntensityBatchParametersDTO
from openapi_client.models.carbon_intensity_dto import CarbonIntensityDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarbonAwareApi(api_client)
    carbon_intensity_batch_parameters_dto = [openapi_client.CarbonIntensityBatchParametersDTO()] # List[CarbonIntensityBatchParametersDTO] | Array of inputs where each contains a \"location\", \"startDate\", and \"endDate\" for which to calculate average marginal carbon intensity. (optional)

    try:
        # Given an array of request objects, each with their own location and time boundaries, calculate the average carbon intensity for that location and time period   and return an array of carbon intensity objects.
        api_response = api_instance.get_average_carbon_intensity_batch(carbon_intensity_batch_parameters_dto=carbon_intensity_batch_parameters_dto)
        print("The response of CarbonAwareApi->get_average_carbon_intensity_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarbonAwareApi->get_average_carbon_intensity_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **carbon_intensity_batch_parameters_dto** | [**List[CarbonIntensityBatchParametersDTO]**](CarbonIntensityBatchParametersDTO.md)| Array of inputs where each contains a \&quot;location\&quot;, \&quot;startDate\&quot;, and \&quot;endDate\&quot; for which to calculate average marginal carbon intensity. | [optional] 

### Return type

[**List[CarbonIntensityDTO]**](CarbonIntensityDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns an array of objects where each contains location, time boundaries and the corresponding average marginal carbon intensity |  -  |
**400** | Returned if any of the requested items are invalid |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_best_emissions_data_for_locations_by_time**
> List[EmissionsData] get_best_emissions_data_for_locations_by_time(location, time=time, to_time=to_time)

Calculate the best emission data by list of locations for a specified time period.

### Example


```python
import openapi_client
from openapi_client.models.emissions_data import EmissionsData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarbonAwareApi(api_client)
    location = ['location_example'] # List[str] | String array of named locations
    time = '2022-03-01T15:30:00Z' # datetime | [Optional] Start time for the data query. (optional)
    to_time = '2022-03-01T18:30:00Z' # datetime | [Optional] End time for the data query. (optional)

    try:
        # Calculate the best emission data by list of locations for a specified time period.
        api_response = api_instance.get_best_emissions_data_for_locations_by_time(location, time=time, to_time=to_time)
        print("The response of CarbonAwareApi->get_best_emissions_data_for_locations_by_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarbonAwareApi->get_best_emissions_data_for_locations_by_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**List[str]**](str.md)| String array of named locations | 
 **time** | **datetime**| [Optional] Start time for the data query. | [optional] 
 **to_time** | **datetime**| [Optional] End time for the data query. | [optional] 

### Return type

[**List[EmissionsData]**](EmissionsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_forecast_data**
> List[EmissionsForecastDTO] get_current_forecast_data(location, data_start_at=data_start_at, data_end_at=data_end_at, window_size=window_size)

Retrieves the most recent forecasted data and calculates the optimal marginal carbon intensity window.

This endpoint fetches only the most recently generated forecast for all provided locations.  It uses the \"dataStartAt\" and   \"dataEndAt\" parameters to scope the forecasted data points (if available for those times). If no start or end time   boundaries are provided, the entire forecast dataset is used. The scoped data points are used to calculate average marginal   carbon intensities of the specified \"windowSize\" and the optimal marginal carbon intensity window is identified.                The forecast data represents what the data source predicts future marginal carbon intensity values to be,   not actual measured emissions data (as future values cannot be known).                This endpoint is useful for determining if there is a more carbon-optimal time to use electricity predicted in the future.

### Example


```python
import openapi_client
from openapi_client.models.emissions_forecast_dto import EmissionsForecastDTO
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarbonAwareApi(api_client)
    location = ['location_example'] # List[str] | String array of named locations
    data_start_at = '2022-03-01T15:30:00Z' # datetime | Start time boundary of forecasted data points.Ignores current forecast data points before this time.  Defaults to the earliest time in the forecast data. (optional)
    data_end_at = '2022-03-01T18:30:00Z' # datetime | End time boundary of forecasted data points. Ignores current forecast data points after this time.  Defaults to the latest time in the forecast data. (optional)
    window_size = 30 # int | The estimated duration (in minutes) of the workload.  Defaults to the duration of a single forecast data point. (optional)

    try:
        # Retrieves the most recent forecasted data and calculates the optimal marginal carbon intensity window.
        api_response = api_instance.get_current_forecast_data(location, data_start_at=data_start_at, data_end_at=data_end_at, window_size=window_size)
        print("The response of CarbonAwareApi->get_current_forecast_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarbonAwareApi->get_current_forecast_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**List[str]**](str.md)| String array of named locations | 
 **data_start_at** | **datetime**| Start time boundary of forecasted data points.Ignores current forecast data points before this time.  Defaults to the earliest time in the forecast data. | [optional] 
 **data_end_at** | **datetime**| End time boundary of forecasted data points. Ignores current forecast data points after this time.  Defaults to the latest time in the forecast data. | [optional] 
 **window_size** | **int**| The estimated duration (in minutes) of the workload.  Defaults to the duration of a single forecast data point. | [optional] 

### Return type

[**List[EmissionsForecastDTO]**](EmissionsForecastDTO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the requested forecast objects |  -  |
**400** | Returned if any of the input parameters are invalid |  -  |
**500** | Internal server error |  -  |
**501** | Returned if the underlying data source does not support forecasting |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emissions_data_for_location_by_time**
> List[EmissionsData] get_emissions_data_for_location_by_time(location, time=time, to_time=to_time)

Calculate the best emission data by location for a specified time period.

### Example


```python
import openapi_client
from openapi_client.models.emissions_data import EmissionsData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarbonAwareApi(api_client)
    location = 'location_example' # str | String named location.
    time = '2013-10-20T19:20:30+01:00' # datetime | [Optional] Start time for the data query. (optional)
    to_time = '2013-10-20T19:20:30+01:00' # datetime | [Optional] End time for the data query. (optional)

    try:
        # Calculate the best emission data by location for a specified time period.
        api_response = api_instance.get_emissions_data_for_location_by_time(location, time=time, to_time=to_time)
        print("The response of CarbonAwareApi->get_emissions_data_for_location_by_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarbonAwareApi->get_emissions_data_for_location_by_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**| String named location. | 
 **time** | **datetime**| [Optional] Start time for the data query. | [optional] 
 **to_time** | **datetime**| [Optional] End time for the data query. | [optional] 

### Return type

[**List[EmissionsData]**](EmissionsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_emissions_data_for_locations_by_time**
> List[EmissionsData] get_emissions_data_for_locations_by_time(location, time=time, to_time=to_time)

Calculate the observed emission data by list of locations for a specified time period.

### Example


```python
import openapi_client
from openapi_client.models.emissions_data import EmissionsData
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.CarbonAwareApi(api_client)
    location = ['location_example'] # List[str] | String array of named locations
    time = '2022-03-01T15:30:00Z' # datetime | [Optional] Start time for the data query. (optional)
    to_time = '2022-03-01T18:30:00Z' # datetime | [Optional] End time for the data query. (optional)

    try:
        # Calculate the observed emission data by list of locations for a specified time period.
        api_response = api_instance.get_emissions_data_for_locations_by_time(location, time=time, to_time=to_time)
        print("The response of CarbonAwareApi->get_emissions_data_for_locations_by_time:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CarbonAwareApi->get_emissions_data_for_locations_by_time: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**List[str]**](str.md)| String array of named locations | 
 **time** | **datetime**| [Optional] Start time for the data query. | [optional] 
 **to_time** | **datetime**| [Optional] End time for the data query. | [optional] 

### Return type

[**List[EmissionsData]**](EmissionsData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json; charset=utf-8

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**204** | No Content |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

