from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import sign_language_translator as slt
import uuid
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/api/translate")
async def translate_to_sign(text: str = Form(...)):
    filename = f"{uuid.uuid4().hex}.mp4"
    filepath = f"./videos/{filename}"

    model = slt.models.ConcatenativeSynthesis(
        text_language="english",
        sign_language="pk-sl",
        sign_format="video"
    )

    sign = model.translate(text)
    sign.save(filepath)

    return FileResponse(
        filepath,
        media_type="video/mp4",
        filename="sign_output.mp4"
    )
