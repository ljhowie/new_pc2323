import fastapi
import uvicorn

print("Hello World")
api = fastapi.FastAPI()

@api.get("/")
def endpoint():
    return {"msg": "Hello world"}

uvicorn.run(api, port=8001)