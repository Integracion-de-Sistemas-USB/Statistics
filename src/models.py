from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class Scenary(BaseModel): 
    bullet_weight: float
    distance: float
    ammo: str 
    temperature: float
    altitude: float
    humidity: float
    scenary: str
    stress_level: int
    caliber: float

class Results(BaseModel): 
    id: str = None
    name: str
    accuracy: str
    scenary: Scenary

class Response(BaseModel): 
    code: int 
    status: str 
    message: str 
    result: Optional[T] = None