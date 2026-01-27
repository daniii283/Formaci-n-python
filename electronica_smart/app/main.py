from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controladores.smart_devices import router as smart_device_router
from app.controladores.auth import router as auth_router
from app.controladores import simulation_controller
from app.controladores import device_event_logs


app = FastAPI(title="Electronica Smart API", version="0.1.0")

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(smart_device_router, prefix="/devices", tags=["Smart Devices"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(simulation_controller.router)
app.include_router(device_event_logs.router)

@app.get("/")
def read_root():
  return {"message": "Bienvenido a Electronica Smart API"}
