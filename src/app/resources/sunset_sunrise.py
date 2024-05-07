## -- Importing External Modules -- ##
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta
import httpx, pytz

## -- Importing Internal Modules -- ##
from src.interfaces.default_response import (
    GenericError,
    PydanticError,
)
from src.interfaces.sunset_sunrise import (
    SunsetSunrisePost,
    SunsetSunrisePostResponse,
)
import config as cnfg

tag = ["Sunset Sunrise"]

router = APIRouter(
    prefix = "/sunset-sunrise",
    tags = tag,
)

responses_post = {
    200: {"model": SunsetSunrisePostResponse},
    400: {"model": GenericError},
    422: {"model": PydanticError},
}

@router.post(
        "", 
        responses = responses_post, 
    )
async def sunset_sunrise_post(
        request: SunsetSunrisePost,
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
            "lat": request.latitude,
            "lng": request.longitude,
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

    check_datetime_string: str = results[request.type.lower()]
    check_datetime: datetime = datetime.strptime(check_datetime_string.replace("T", " "), "%Y-%m-%d %H:%M:%S%z")

    if request_datetime > check_datetime:
        check_datetime += timedelta(days = 1)
        
    difference_datetime = check_datetime - request_datetime
    
    response_data: dict = {
        "remaing_time": str(difference_datetime)[:8],
        "exact_datetime": check_datetime.strftime(conversion_format),
        "request_datetime": request_datetime.strftime(conversion_format),
    }

    return {
        "description": "Request occurred successfully",
        "data": response_data,
    }
