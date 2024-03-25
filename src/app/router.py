from fastapi import APIRouter
from app.repository import ResultsRepo
from app.models import Results, Response, UpdateResults

router = APIRouter()

@router.get("/results/")
async def get_results(): 
    results_list = await ResultsRepo.retrieve()
    return Response(code=200, status="Ok", message="Success retrieve all data", result=results_list).model_dump(exclude_none=True)

@router.post("/results/create")
async def create_results(results: Results):
    await ResultsRepo.insert(results)
    return Response(code=200, status="Ok", message="Success created data").model_dump(exclude_none=True)

@router.get("/results/{id}")
async def get_results_id(id: str): 
    results = await ResultsRepo.retrieve_id(id)
    return Response(code=200, status="Ok", message="Success get data", result=results).model_dump(exclude_none=True)

@router.put("/results/update/{id}")
async def update_results(id: str, results: UpdateResults): 
    await ResultsRepo.update(id, results)
    return Response(code=200, status="Ok", message="Success update data").model_dump(exclude_none=True)

@router.delete("/results/delete/{id}")
async def delete_results(id: str): 
    await ResultsRepo.delete(id)
    return Response(code=200, status="Ok", message="Success delete data").model_dump(exclude_none=True)
