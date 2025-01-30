# coding: utf-8

"""
    CarbonAware.WebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.carbon_aware_api import CarbonAwareApi


class TestCarbonAwareApi(unittest.TestCase):
    """CarbonAwareApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CarbonAwareApi()

    def tearDown(self) -> None:
        pass

    def test_batch_forecast_data_async(self) -> None:
        """Test case for batch_forecast_data_async

        Given an array of historical forecasts, retrieves the data that contains  forecasts metadata, the optimal forecast and a range of forecasts filtered by the attributes [start...end] if provided.
        """
        pass

    def test_get_average_carbon_intensity(self) -> None:
        """Test case for get_average_carbon_intensity

        Retrieves the measured carbon intensity data between the time boundaries and calculates the average carbon intensity during that period.
        """
        pass

    def test_get_average_carbon_intensity_batch(self) -> None:
        """Test case for get_average_carbon_intensity_batch

        Given an array of request objects, each with their own location and time boundaries, calculate the average carbon intensity for that location and time period   and return an array of carbon intensity objects.
        """
        pass

    def test_get_best_emissions_data_for_locations_by_time(self) -> None:
        """Test case for get_best_emissions_data_for_locations_by_time

        Calculate the best emission data by list of locations for a specified time period.
        """
        pass

    def test_get_current_forecast_data(self) -> None:
        """Test case for get_current_forecast_data

        Retrieves the most recent forecasted data and calculates the optimal marginal carbon intensity window.
        """
        pass

    def test_get_emissions_data_for_location_by_time(self) -> None:
        """Test case for get_emissions_data_for_location_by_time

        Calculate the best emission data by location for a specified time period.
        """
        pass

    def test_get_emissions_data_for_locations_by_time(self) -> None:
        """Test case for get_emissions_data_for_locations_by_time

        Calculate the observed emission data by list of locations for a specified time period.
        """
        pass


if __name__ == '__main__':
    unittest.main()
