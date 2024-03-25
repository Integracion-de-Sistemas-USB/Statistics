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
    x: float 
    y: float
    scenary: Scenary

class UpdateResults(BaseModel): 
    name: Optional[str] = None
    x: Optional[float] = None 
    y: Optional[float] = None
    scenary: Optional[Scenary] = None

class Response(BaseModel): 
    code: int 
    status: str 
    message: str 
    result: Optional[T] = None