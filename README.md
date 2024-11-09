# Pydrolono

A Python client for accessing hydrological data from the Norwegian Water Resources and Energy Directorate (NVE) Hydrology API.

## Features

- Easy access to NVE's Hydrology API
- Support for retrieving stations, parameters, and observations
- Data conversion to Pandas DataFrames
- Type-safe with dataclass models
- Comprehensive error handling

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Setup

```python
from pydrolono.client import NVEHydroAPIClient

# Initialize client with API key from environment variable NVE_API_KEY
client = NVEHydroAPIClient()
```

### Get Available Parameters

```python
parameters = client.get_parameters()
if parameters:
    print(f"Retrieved {parameters.itemCount} parameters")
```

### Get Active Stations

```python
stations = client.get_stations(active=1)
if stations:
    print(f"Retrieved {stations.itemCount} active stations")
```

### Get Observations

```python
from datetime import datetime, timedelta
from pydrolono.client import ObservationsRequest

# Get last 24 hours of data
end_time = datetime.now()
start_time = end_time - timedelta(days=1)
reference_time = f"{start_time.isoformat()}/{end_time.isoformat()}"

request = ObservationsRequest(
    stationId="12.209.0",  # Example station
    parameter="1000",      # Water level
    resolutionTime="60",   # Hourly data
    referenceTime=reference_time
)

result = client.get_observations(request)
```

### Convert to DataFrame

```python
from pydrolono.client import observations_to_dataframe

if result and result.data:
    df = observations_to_dataframe(result.data)
    print(df.head())
```

## Authentication

The client requires an API key from NVE. You can provide it in two ways:

1. Set environment variable:
```bash
export NVE_API_KEY='your-api-key'
```

2. Pass directly to client:
```python
client = NVEHydroAPIClient(api_key='your-api-key')
```

## Testing

Run the test script to verify API connectivity and basic functionality:

```bash
python test_api.py
```

## License

This project is licensed under the MIT License.
