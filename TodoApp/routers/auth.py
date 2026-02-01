from fastapi import APIRouter

#app = FastAPI() # Creates a new instance of APP

router = APIRouter()

@router.get("/auth/")
async def get_user():
    return {'user': 'authenticated'}

