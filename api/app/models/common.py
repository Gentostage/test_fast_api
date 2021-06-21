from pydantic import BaseModel, validator


class Operations(BaseModel):
    number1: int
    number2: int

    @validator("number1")
    def validate_number1(cls, value):
        if value <=0:
            raise ValueError("number1 must be a positive integer")
        return value

    @validator("number2")
    def validate_number2(cls, value):
        if value < 0:
            raise ValueError("number2 must be a non-negative integer")
        return value


class ResultOperation(BaseModel):
    result: int

    @validator("result")
    def validate_number2(cls, value):
        if value <= 0:
            raise ValueError("result is not a non-negative integer")
        return value