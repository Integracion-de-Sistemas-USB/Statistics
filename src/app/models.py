from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class Scenary(BaseModel): 
    bullet_weight: float
    distance: float
    ammo: str
    scenary: str
    stress_level: int
    caliber: float

class Results(BaseModel): 
    id: str = None
    name: str
    score: float
    scenary: Scenary

class UpdateResults(BaseModel): 
    name: Optional[str] = None
    score: Optional[float] = None
    scenary: Optional[Scenary] = None

class Response(BaseModel): 
    code: int 
    status: str 
    message: str 
    result: Optional[T] = None