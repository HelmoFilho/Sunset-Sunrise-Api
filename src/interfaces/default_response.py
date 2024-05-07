## -- Importing External Modules -- ##
from pydantic import BaseModel, Field, ConfigDict

## -- Importing Internal Modules -- ##


## Response

### Default
class DefaultResponse(BaseModel):

    description: str = Field(
        None,
        description = "Message describing the situation of the response",
    )

    model_config = ConfigDict(
        title = "Response: Everything`s ok",
        json_schema_extra = {
            "example": {
                "description": "Specific message to the situation",
            }
        }
    ) 


### Errors
        
#### Generic
class GenericError(DefaultResponse):  

    model_config = ConfigDict(
        title = "Response: Generic Error",
        json_schema_extra = {
            "example": {
                "description": "Specific error message to the situation",
            }
        }
    ) 


##### Pydantic 
class PydanticDetails(BaseModel):

    msg: str = Field(
        None,
        description = "Error message"
    )

    type: list[dict] = Field(
        None,
        description = "Validation error type"
    )

    loc: list[str | int] = Field(
        None,
        description = "What / Where exactly is the error"
    )


class PydanticError(DefaultResponse):

    details: list[PydanticDetails] = Field(
        None,
        description = "Array with the errors from the data validator"
    )

    model_config = ConfigDict(
        title = "Response: Data validation error",
        json_schema_extra = {
            "example": {
                "description": "Request validation error",
                "details": [
                    {
                        "type": "missing",
                        "loc": [
                            "body",
                            "type"
                        ],
                        "msg": "Field required",
                        "input": {},
                        "url": "https://errors.pydantic.dev/2.6/v/missing"
                    },
                    {
                        "type": "missing",
                        "loc": [
                            "body",
                            "latitude"
                        ],
                        "msg": "Field required",
                        "input": {},
                        "url": "https://errors.pydantic.dev/2.6/v/missing"
                    },
                    {
                        "type": "missing",
                        "loc": [
                            "body",
                            "longitude"
                        ],
                        "msg": "Field required",
                        "input": {},
                        "url": "https://errors.pydantic.dev/2.6/v/missing"
                    }
                ]
            }
        }
    )
        