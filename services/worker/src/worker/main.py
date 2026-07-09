from fastapi import FastAPI

app = FastAPI(title="Worker")


@app.post("/process")
async def process(task: int):
    return {"status": f"processed {task}"}
