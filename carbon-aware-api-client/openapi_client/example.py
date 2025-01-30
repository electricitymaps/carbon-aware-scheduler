import openapi_client
from openapi_client.rest import ApiException
from datetime import datetime

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:5073",
)


# Enter a context with an instance of the API client
if __name__ == "__main__":
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.CarbonAwareApi(api_client)

        try:
            api_response = api_instance.get_current_forecast_data(
                location=['belgium'],
            )
            for e in api_response:
                print(e.to_str())
        except ApiException as e:
            print("Exception when calling CarbonAwareApi: %s\n" % e)
