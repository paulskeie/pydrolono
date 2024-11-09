import os
from pydrolono.client import NVEHydroAPIClient, ObservationsRequest, observations_to_dataframe
from datetime import datetime, timedelta
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def test_api_connection():
    """Test basic API connectivity and parameter listing"""
    client = NVEHydroAPIClient()
    
    print("\n=== Testing Parameters Endpoint ===")
    parameters = client.get_parameters()
    if parameters:
        print(f"Successfully retrieved {parameters.itemCount} parameters")
        print("\nFirst 5 parameters:")
        for param in parameters.data[:5]:
            print(f"- {param.parameter}: {param.parameterName} ({param.unit})")
    else:
        print("Failed to retrieve parameters")

def test_stations():
    """Test station listing"""
    client = NVEHydroAPIClient()
    
    print("\n=== Testing Stations Endpoint ===")
    stations = client.get_stations(active=1)
    if stations:
        print(f"Successfully retrieved {stations.itemCount} active stations")
        print("\nFirst 5 stations:")
        for station in stations.data[:5]:
            print(f"- {station.stationId}: {station.stationName} ({station.latitude}, {station.longitude})")
    else:
        print("Failed to retrieve stations")

def test_observations():
    """Test observations retrieval"""
    client = NVEHydroAPIClient()
    
    # Example: Get last 24 hours of data for a specific station
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    reference_time = f"{start_time.isoformat()}/{end_time.isoformat()}"
    
    # Test station: 12.209.0 - Grønlivatn
    station_id = "12.209.0"
    # Parameter 1000 - Water level
    parameter = "1000"
    
    print(f"\n=== Testing Observations Endpoint ===")
    print(f"Querying station {station_id} for parameter {parameter}")
    print(f"Time range: {reference_time}")
    
    request = ObservationsRequest(
        stationId=station_id,
        parameter=parameter,
        resolutionTime="60",  # hourly data
        referenceTime=reference_time
    )
    
    result = client.get_observations(request)
    if result:
        print("\nSuccessfully retrieved observations")
        print(f"Total data points: {result.data[0].observationCount}")
        
        # Convert to DataFrame for better visualization
        df = observations_to_dataframe(result.data)
        print("\nData sample:")
        print(df.head())
        
        # Basic statistics
        print("\nBasic statistics:")
        print(df.describe())
    else:
        print("Failed to retrieve observations")

if __name__ == "__main__":
    test_api_connection()
    test_stations()
    test_observations()
