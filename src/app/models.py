from typing import TypeVar, Optional
from pydantic import BaseModel

T = TypeVar('T')

class Scenary(BaseModel): 
    bullet_weight: float
    distance: float
    ammo: str
    scenary: str
    stress_level: str
    caliber: float

class Results(BaseModel): 
    id: str = None
    code: str
    name: str
    score: list[int]
    gun: str
    scenary: Scenary

class UpdateResults(BaseModel): 
    name: Optional[str] = None
    score: Optional[int] = None
    scenary: Optional[Scenary] = None

class Response(BaseModel): 
    code: int 
    status: str 
    message: str 
    result: Optional[T] = None