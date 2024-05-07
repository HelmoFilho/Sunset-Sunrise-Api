## -- Importing External Modules -- ##
from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import httpx, pytz

## -- Importing Internal Modules -- ##
from src.interfaces.default_response import (
    GenericError,
    PydanticError,
)
from src.interfaces.sunset_sunrise import (
    SunsetSunriseGet,
    SunsetSunriseGetResponse,
)
import config as cnfg

tag = ["Sunset Sunrise"]

router = APIRouter(
    prefix = "/sunset-sunrise",
    tags = tag,
)

responses_get = {
    200: {"model": SunsetSunriseGetResponse},
    400: {"model": GenericError},
    422: {"model": PydanticError},
}

@router.get(
        "", 
        responses = responses_get, 
    )
async def sunset_sunrise_get(
        query_params: SunsetSunriseGet = Depends(),
    ):
    """
    The microservice dynamically respond to the request with the following data:

    - Remaining time until the next event (either sunrise or sunset) occurs, and display it in the format H:i:s. 
    - If the time for today's event has already passed, the code should automatically compute the time until the event on the next day.
    """
    
    request_datetime: datetime = datetime.now().replace(tzinfo=pytz.timezone(cnfg.TIMEZONE))

    # Getting data from the API
    client = httpx.AsyncClient()
    response = await client.post(
        "https://api.sunrise-sunset.org/json",
        params = {
            "lat": query_params.latitude,
            "lng": query_params.longitude,
            "formatted": 0,
            "tzid": cnfg.TIMEZONE,
            "date": "today",
        },
        timeout = 60,
    )

    json_response: dict = response.json()
    results: dict = json_response.get("results")

    if (response.status_code != 200) or not results:

        return JSONResponse(
            status_code = 400,
            content = {
                "description": json_response.get("status", "UNKNOWN_ERROR")
            }
        )
    
    # Converting and calculating answers
    conversion_format: str = "%d-%m-%Y %H:%M:%S"

    check_datetime_string: str = results[query_params.type.lower()]
    check_datetime: datetime = datetime.strptime(check_datetime_string.replace("T", " "), "%Y-%m-%d %H:%M:%S%z")

    if request_datetime > check_datetime:

        response = await client.post(
            "https://api.sunrise-sunset.org/json",
            params = {
                "lat": query_params.latitude,
                "lng": query_params.longitude,
                "formatted": 0,
                "tzid": cnfg.TIMEZONE,
                "date": "tomorrow",
            },
            timeout = 60,
        )

        json_response: dict = response.json()
        results: dict = json_response.get("results")

        check_datetime_string: str = results[query_params.type.lower()]
        check_datetime: datetime = datetime.strptime(check_datetime_string.replace("T", " "), "%Y-%m-%d %H:%M:%S%z")
        
    difference_datetime = check_datetime - request_datetime
    
    response_data: dict = {
        "remaing_time": str(difference_datetime)[:8],
        "event_datetime": check_datetime.strftime(conversion_format),
        "request_datetime": request_datetime.strftime(conversion_format),
    }

    return {
        "description": "Request occurred successfully",
        "data": response_data,
    }
