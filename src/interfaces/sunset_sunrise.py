## -- Importing External Modules -- ##
from pydantic import (
    BaseModel,
    Field,
    ConfigDict,
)
from enum import Enum, auto

## -- Importing Internal Modules -- ##
from src.interfaces.default_response import DefaultResponse
    
class CaseInsensitiveEnum(str, Enum):

    def _generate_next_value_(name, start, count, last_values):
        return name

    @classmethod
    def _missing_(cls, value):
        if isinstance(value, str):
            value = value.upper()
            for member in cls:
                if member.upper() == value:
                    return member
        return None

## Request
class TypeChoices(CaseInsensitiveEnum):

    SUNSET = auto()
    SUNRISE = auto()


### Post
class SunsetSunrisePost(BaseModel):

    type: TypeChoices = Field(
        ...,
        description = "What event should have the time be verified for"
    )

    latitude: float = Field(
        ...,
        description = "Latitude of the location",
        ge = -90,
        le = 90,
    )

    longitude: float = Field(
        ...,
        description = "Longitude of the location",
        ge = -180,
        le = 180,
    )


## Response

### Post
class SunsetSunrisePostData(BaseModel):

    remaing_time: str = Field(
        None,
        description = "Remaining time until next sunset/sunrise.",
    )

    exact_datetime: str = Field(
        None,
        description = "Datetime of next event.",
    )    

    request_datetime: str = Field(
        None,
        description = "Datetime of the request.",
    )


class SunsetSunrisePostResponse(DefaultResponse):

    data: SunsetSunrisePostData = Field(
        None,
        description = "data",
    )

    model_config = ConfigDict(
        title = "Response: Everything`s ok",
        json_schema_extra = {
            "example": {
                "description": "Request occurred successfully",
                "data": {
                    "remaing_time": "23:24:41",
                    "exact_datetime": "27-02-2024 18:38:55",
                    "request_datetime": "26-02-2024 19:08:13"
                }
            }
        }
    )        
