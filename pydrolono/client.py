

import requests
from dataclasses import dataclass
from typing import List, Optional
import pandas as pd

# Define Data Classes Based on API Schemas
@dataclass
class Parameter:
    parameter: int
    parameterName: Optional[str]
    parameterNameEng: Optional[str]
    unit: Optional[str]

@dataclass
class ParametersResult:
    currentLink: Optional[str]
    apiVersion: Optional[str]
    license: Optional[str]
    createdAt: str
    queryTime: Optional[str]
    itemCount: int
    data: List[Parameter]

@dataclass
class Observation:
    time: str
    value: Optional[float] = None
    correction: Optional[int] = None
    quality: Optional[int] = None

@dataclass
class ObservationData:
    stationId: str
    stationName: str
    parameter: int
    parameterName: str
    parameterNameEng: str
    serieVersionNo: int
    method: str
    unit: str
    observationCount: int
    observations: List[Observation]  # Nested list of Observation entries

@dataclass
class ObservationResult:
    currentLink: Optional[str]
    apiVersion: Optional[str]
    license: Optional[str]
    createdAt: str
    queryTime: Optional[str]
    itemCount: int
    data: List[ObservationData]  # List of ObservationData items

@dataclass
class Station:
    stationId: Optional[str]
    stationName: Optional[str]
    latitude: float
    longitude: float
    utmEast_Z33: Optional[int]
    utmNorth_Z33: Optional[int]
    masl: Optional[int]
    riverName: Optional[str]
    councilNumber: Optional[str]
    councilName: Optional[str]
    countyName: Optional[str]
    stationTypeName: Optional[str]
    stationStatusName: Optional[str]
    drainageBasinArea: Optional[float]
    drainageBasinAreaNorway: Optional[float]
    gradient1085: Optional[float]
    gradientBasin: Optional[float]
    gradientRiver: Optional[float]
    lengthKmBasin: Optional[float]
    lengthKmRiver: Optional[float]
    percentAgricul: Optional[float]
    percentBog: Optional[float]
    percentEffBog: Optional[float]
    percentEffLake: Optional[float]
    percentForest: Optional[float]
    percentGlacier: Optional[float]
    percentLake: Optional[float]
    percentMountain: Optional[float]
    percentUrban: Optional[float]
    stationStatusName: Optional[str]
    catchmentRegTypeName: Optional[str]
    owner: Optional[str]
    annualRunoff: Optional[float]
    specificDischarge: Optional[float]
    regulationArea: Optional[float]
    areaReservoirs: Optional[float]
    volumeReservoirs: Optional[float]
    numberReservoirs: Optional[int]
    firstYearRegulation: Optional[int]
    councilName: Optional[str]
    councilNumber: Optional[str]
    countyName: Optional[str]
    drainageBasinArea: Optional[float]
    drainageBasinKey: Optional[str]
    gradientBasin: Optional[float]
    riverName: Optional[str]
    hierarchy: Optional[str]
    lakeArea: Optional[float]
    lakeName: Optional[str]
    lakeNo: Optional[str]
    regineNo: Optional[str]
    reservoirNo: Optional[str]
    reservoirName: Optional[str]
    heightMinimum: Optional[float]
    heightHypso10: Optional[float]
    heightHypso20: Optional[float]
    heightHypso30: Optional[float]
    heightHypso40: Optional[float]
    heightHypso50: Optional[float]
    heightHypso60: Optional[float]
    heightHypso70: Optional[float]
    heightHypso80: Optional[float]
    heightHypso90: Optional[float]
    heightMaximum: Optional[float]
    utmZoneGravi: Optional[int]
    utmEastGravi: Optional[int]
    utmNorthGravi: Optional[int]
    utmZoneInlet: Optional[int]
    utmEastInlet: Optional[int]
    utmNorthInlet: Optional[int]
    utmZoneOutlet: Optional[int]
    utmEastOutlet: Optional[int]
    utmNorthOutlet: Optional[int]
    regulationPartReservoirs: Optional[float]
    transferAreaIn: Optional[float]
    transferAreaOut: Optional[float]
    reservoirAreaIn: Optional[float]
    reservoirAreaOut: Optional[float]
    reservoirVolumeIn: Optional[float]
    reservoirVolumeOut: Optional[float]
    remainingArea: Optional[float]
    qNumberOfYears: Optional[int]
    qStartYear: Optional[int]
    qEndYear: Optional[int]
    qm: Optional[float]
    q5: Optional[float]
    q10: Optional[float]
    q20: Optional[float]
    q50: Optional[float]
    q80: Optional[float]
    q90: Optional[float]
    q95: Optional[float]
    q99: Optional[float]
    q100: Optional[float]
    hm: Optional[float]
    h5: Optional[float]
    h10: Optional[float]
    h20: Optional[float]
    h50: Optional[float]
    h80: Optional[float]
    h90: Optional[float]
    h95: Optional[float]
    h99: Optional[float]
    h100: Optional[float]
    culQm: Optional[float]
    culQ5: Optional[float]
    culQ10: Optional[float]
    culQ20: Optional[float]
    culQ50: Optional[float]
    culQ80: Optional[float]
    culQ90: Optional[float]
    culQ95: Optional[float]
    culQ99: Optional[float]
    culQ100: Optional[float]
    culHm: Optional[float]
    culH5: Optional[float]
    culH10: Optional[float]
    culH20: Optional[float]
    culH50: Optional[float]
    culH80: Optional[float]
    culH90: Optional[float]
    culH95: Optional[float]
    culH99: Optional[float]
    culH100: Optional[float]
    seriesList: Optional[str]
    
@dataclass
class Station:
    stationId: Optional[str] = None
    stationName: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    utmEast_Z33: Optional[int] = None
    utmNorth_Z33: Optional[int] = None
    masl: Optional[int] = None
    riverName: Optional[str] = None
    councilNumber: Optional[str] = None
    councilName: Optional[str] = None
    countyName: Optional[str] = None
    stationTypeName: Optional[str] = None
    stationStatusName: Optional[str] = None
    drainageBasinArea: Optional[float] = None
    drainageBasinAreaNorway: Optional[float] = None
    gradient1085: Optional[float] = None
    gradientBasin: Optional[float] = None
    gradientRiver: Optional[float] = None
    lengthKmBasin: Optional[float] = None
    lengthKmRiver: Optional[float] = None
    percentAgricul: Optional[float] = None
    percentBog: Optional[float] = None
    percentEffBog: Optional[float] = None
    percentEffLake: Optional[float] = None
    percentForest: Optional[float] = None
    percentGlacier: Optional[float] = None
    percentLake: Optional[float] = None
    percentMountain: Optional[float] = None
    percentUrban: Optional[float] = None
    catchmentRegTypeName: Optional[str] = None
    owner: Optional[str] = None
    annualRunoff: Optional[float] = None
    specificDischarge: Optional[float] = None
    regulationArea: Optional[float] = None
    areaReservoirs: Optional[float] = None
    volumeReservoirs: Optional[float] = None
    numberReservoirs: Optional[int] = None
    firstYearRegulation: Optional[int] = None
    drainageBasinKey: Optional[str] = None
    hierarchy: Optional[str] = None
    lakeArea: Optional[float] = None
    lakeName: Optional[str] = None
    lakeNo: Optional[str] = None
    regineNo: Optional[str] = None
    reservoirNo: Optional[str] = None
    reservoirName: Optional[str] = None
    heightMinimum: Optional[float] = None
    heightHypso10: Optional[float] = None
    heightHypso20: Optional[float] = None
    heightHypso30: Optional[float] = None
    heightHypso40: Optional[float] = None
    heightHypso50: Optional[float] = None
    heightHypso60: Optional[float] = None
    heightHypso70: Optional[float] = None
    heightHypso80: Optional[float] = None
    heightHypso90: Optional[float] = None
    heightMaximum: Optional[float] = None
    utmZoneGravi: Optional[int] = None
    utmEastGravi: Optional[int] = None
    utmNorthGravi: Optional[int] = None
    utmZoneInlet: Optional[int] = None
    utmEastInlet: Optional[int] = None
    utmNorthInlet: Optional[int] = None
    utmZoneOutlet: Optional[int] = None
    utmEastOutlet: Optional[int] = None
    utmNorthOutlet: Optional[int] = None
    regulationPartReservoirs: Optional[float] = None
    transferAreaIn: Optional[float] = None
    transferAreaOut: Optional[float] = None
    reservoirAreaIn: Optional[float] = None
    reservoirAreaOut: Optional[float] = None
    reservoirVolumeIn: Optional[float] = None
    reservoirVolumeOut: Optional[float] = None
    remainingArea: Optional[float] = None
    qNumberOfYears: Optional[int] = None
    qStartYear: Optional[int] = None
    qEndYear: Optional[int] = None
    qm: Optional[float] = None
    q5: Optional[float] = None
    q10: Optional[float] = None
    q20: Optional[float] = None
    q50: Optional[float] = None
    q80: Optional[float] = None
    q90: Optional[float] = None
    q95: Optional[float] = None
    q99: Optional[float] = None
    q100: Optional[float] = None
    hm: Optional[float] = None
    h5: Optional[float] = None
    h10: Optional[float] = None
    h20: Optional[float] = None
    h50: Optional[float] = None
    h80: Optional[float] = None
    h90: Optional[float] = None
    h95: Optional[float] = None
    h99: Optional[float] = None
    h100: Optional[float] = None
    culQm: Optional[float] = None
    culQ5: Optional[float] = None
    culQ10: Optional[float] = None
    culQ20: Optional[float] = None
    culQ50: Optional[float] = None
    culQ80: Optional[float] = None
    culQ90: Optional[float] = None
    culQ95: Optional[float] = None
    culQ99: Optional[float] = None
    culQ100: Optional[float] = None
    culHm: Optional[float] = None
    culH5: Optional[float] = None
    culH10: Optional[float] = None
    culH20: Optional[float] = None
    culH50: Optional[float] = None
    culH80: Optional[float] = None
    culH90: Optional[float] = None
    culH95: Optional[float] = None
    culH99: Optional[float] = None
    culH100: Optional[float] = None
    seriesList: Optional[str] = None

# Full station result
@dataclass
class StationResult:
    currentLink: Optional[str]
    apiVersion: Optional[str]
    license: Optional[str]
    createdAt: str
    queryTime: Optional[str]
    itemCount: int
    data: List[Station]

# Request Body Classes for Complex Endpoints
@dataclass
class ObservationsRequest:
    stationId: str
    parameter: str
    resolutionTime: str
    versionNumber: Optional[int] = None
    referenceTime: Optional[str] = None
    qualityTypes: Optional[str] = None
    method: Optional[str] = None
    timeOffset: Optional[str] = None
    correctionTypes: Optional[str] = None

# Define API Client Class
class NVEHydroAPIClient:
    def __init__(self, api_key: str, server_url: str = "https://hydapi.nve.no/api/v1"):
        self.server_url = server_url
        self.headers = {
            "accept": "application/json",
            "X-API-Key": api_key
        }

    def _get(self, endpoint: str, params: dict = None):
        url = f"{self.server_url}{endpoint}"
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error occurred: {e}")
            return None

        
    def _post(self, endpoint: str, data: dict = None):
        url = f"{self.server_url}{endpoint}"
        try:
            response = requests.post(url, headers=self.headers, json=data)
            response.raise_for_status()
            #print("Response JSON:", response.json())  # Print the entire response for inspection
            return response.json()
        except requests.RequestException as e:
            print(f"Error occurred: {e}")
            if response is not None:
                print("Server response:", response.text)
            return None

    # Endpoint: Get Parameters
    def get_parameters(self) -> Optional[ParametersResult]:
        response_data = self._get("/Parameters")
        if response_data:
            return ParametersResult(
                currentLink=response_data.get("currentLink"),
                apiVersion=response_data.get("apiVersion"),
                license=response_data.get("license"),
                createdAt=response_data["createdAt"],
                queryTime=response_data.get("queryTime"),
                itemCount=response_data["itemCount"],
                data=[Parameter(**param) for param in response_data["data"]]
            )
        return None

    # Endpoint: Get Observations
    def get_observations(self, request_data: ObservationsRequest) -> Optional[ObservationResult]:
        """Fetch observations using POST method."""
        data_dict = [request_data.__dict__]  # Wrap request data in a list
        response_data = self._post("/Observations", data=data_dict)
        if response_data:
            # Parse response into ObservationResult with nested ObservationData
            observation_data = []
            for data_item in response_data["data"]:
                observations = [Observation(**obs) for obs in data_item["observations"]]
                observation_data.append(ObservationData(
                    stationId=data_item["stationId"],
                    stationName=data_item["stationName"],
                    parameter=data_item["parameter"],
                    parameterName=data_item["parameterName"],
                    parameterNameEng=data_item["parameterNameEng"],
                    serieVersionNo=data_item["serieVersionNo"],
                    method=data_item["method"],
                    unit=data_item["unit"],
                    observationCount=data_item["observationCount"],
                    observations=observations
                ))
            
            return ObservationResult(
                currentLink=response_data.get("currentLink"),
                apiVersion=response_data.get("apiVersion"),
                license=response_data.get("license"),
                createdAt=response_data["createdAt"],
                queryTime=response_data.get("queryTime"),
                itemCount=response_data["itemCount"],
                data=observation_data
            )
        return None

    # Endpoint: Get Stations
    def get_stations(self, active: int = 1, polygon: Optional[str] = None) -> Optional[StationResult]:
        params = {"Active": active}
        if polygon:
            params["Polygon"] = polygon
        response_data = self._get("/Stations", params=params)
        if response_data:
            return StationResult(
                currentLink=response_data.get("currentLink"),
                apiVersion=response_data.get("apiVersion"),
                license=response_data.get("license"),
                createdAt=response_data["createdAt"],
                queryTime=response_data.get("queryTime"),
                itemCount=response_data["itemCount"],
                data=[Station(**station) for station in response_data["data"]]
            )
        return None
    
def get_observations(client, stationIds, parameters, referenceTime, resolutionTime):
    """
    Fetches observation data for each combination of stationId and parameter over a specified time range.

    Parameters:
    - client: The API client instance to make requests.
    - stationIds: List of station IDs to query.
    - parameters: List of parameter IDs to query.
    - referenceTime: ISO 8601 string specifying the start and duration of the observation period.
    - resolutionTime: String representing the resolution time (e.g., "60" for hourly).

    Returns:
    - List of ObservationData instances with the aggregated results.
    """
    observations = []
    for stationId in stationIds:
        for parameter in parameters:
            observations_request = ObservationsRequest(
                stationId=stationId,
                parameter=parameter,
                resolutionTime=resolutionTime,
                referenceTime=referenceTime
            )
            try:
                observations_result = client.get_observations(request_data=observations_request)
                if observations_result:
                    observations.extend(observations_result.data)
            except Exception as e:
                print(f"Failed to get observations for station {stationId} and parameter {parameter}: {e}")
    return observations



def observations_to_dataframe(observations):
    """
    Converts a list of ObservationData into a pandas DataFrame with timestamp as the index.

    Parameters:
    - observations: List of ObservationData instances

    Returns:
    - A pandas DataFrame with timestamps as the index and station-parameter combinations as columns.
    """
    data = {}

    for obs_data in observations:
        # Create a column name based on station and parameter names, replacing spaces with underscores
        col_name = f"{obs_data.stationName.replace(' ', '_')}_{obs_data.parameterName}"

        # Extract timestamps and values for each observation in obs_data
        for obs in obs_data.observations:
            timestamp = obs.time
            value = obs.value
            
            # Add the value to the dictionary under the appropriate column name
            if timestamp not in data:
                data[timestamp] = {}
            data[timestamp][col_name] = value

    # Convert the dictionary to a DataFrame
    df = pd.DataFrame.from_dict(data, orient='index')

    # Convert index to datetime and sort
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()

    return df