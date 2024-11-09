import pytest
from datetime import datetime, timedelta
from pydrolono.client import NVEHydroAPIClient, ObservationsRequest
from pydrolono.exceptions import ValidationError, APIError

@pytest.fixture
def client():
    """Create a client instance for testing."""
    return NVEHydroAPIClient()

def test_client_initialization():
    """Test client initialization with invalid API key."""
    with pytest.raises(ValueError):
        NVEHydroAPIClient(api_key="invalid_key")

def test_get_parameters(client):
    """Test parameters endpoint."""
    result = client.get_parameters()
    assert result is not None
    assert result.itemCount > 0
    assert len(result.data) > 0

def test_get_stations(client):
    """Test stations endpoint."""
    result = client.get_stations(active=1)
    assert result is not None
    assert result.itemCount > 0
    assert len(result.data) > 0

def test_get_observations(client):
    """Test observations endpoint."""
    end_time = datetime.now()
    start_time = end_time - timedelta(days=1)
    reference_time = f"{start_time.isoformat()}/{end_time.isoformat()}"
    
    request = ObservationsRequest(
        stationId="12.209.0",
        parameter="1000",
        resolutionTime="60",
        referenceTime=reference_time
    )
    
    result = client.get_observations(request)
    assert result is not None
    assert result.itemCount > 0
    assert len(result.data) > 0

def test_invalid_station(client):
    """Test handling of invalid station ID."""
    request = ObservationsRequest(
        stationId="invalid.station.id",
        parameter="1000",
        resolutionTime="60",
        referenceTime="2024-01-01/2024-01-02"
    )
    
    with pytest.raises(APIError) as exc_info:
        client.get_observations(request)
    assert "API request failed" in str(exc_info.value)

def test_invalid_api_key():
    """Test handling of invalid API key."""
    with pytest.raises(AuthenticationError) as exc_info:
        NVEHydroAPIClient(api_key="invalid_key")
        client.get_parameters()
    assert "Invalid API key" in str(exc_info.value)

def test_invalid_parameter(client):
    """Test handling of invalid parameter."""
    request = ObservationsRequest(
        stationId="12.209.0",
        parameter="invalid",
        resolutionTime="60",
        referenceTime="2024-01-01/2024-01-02"
    )
    
    with pytest.raises(APIError) as exc_info:
        client.get_observations(request)
    assert "API request failed" in str(exc_info.value)
