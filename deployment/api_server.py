from fastapi import FastAPI
from pydantic import BaseModel
from deployment.inference import run_pipeline

app = FastAPI()

class VideoRequest(BaseModel):
    video_id: str

@app.post("/chapter")
def get_chapters(req: VideoRequest):
    chapters, titles = run_pipeline(req.video_id)
    return {"titles": titles, "chapters": chapters}
