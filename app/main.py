import fastapi
import uvicorn

hola = {'message': 'Hi, Darío'}

app = fastapi.FastAPI()


@app.get("/")
async def root():
    return hola

if __name__ == "__main__":
    uvicorn.run(app)
