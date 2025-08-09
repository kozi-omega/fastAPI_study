from fastapi import FastAPI

app = FastAPI()


# async=非同期処理
@app.get("/test")  # ← Decorator
async def example():
    return {"message": "hello world!"}
