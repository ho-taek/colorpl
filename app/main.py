from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.auth.utils import create_super_admin
from utils.config import security_settings
from app.database import Base, engine
from app.auth.routes import router as router_auth
from app.routers.member import router as router_member
from app.routers.schedule import router as router_schedule
from app.routers.review import router as router_review
from app.routers.comment import router as router_comment
from app.routers.reservation import router as router_reservation
from app.routers.show import router as router_show
from app.routers.theater import router as router_theater

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key=security_settings.SECRET_KEY)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router_auth, prefix='/auth', tags=["auth"])
app.include_router(router_member, prefix='/cs', tags=["member"])
app.include_router(router_schedule, prefix='/cs', tags=["schedule"])
app.include_router(router_review, prefix='/cs', tags=["review"])
app.include_router(router_comment, prefix='/cs', tags=["comment"])
app.include_router(router_reservation, prefix='/vm', tags=["reservation"])
app.include_router(router_show, prefix='/vm', tags=["show"])
app.include_router(router_theater, prefix='/vm', tags=["theater"])

@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    create_super_admin()

@app.get("/")
async def read_root(request: Request):
    return {"message": "Hello"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)
