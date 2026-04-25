from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI()

# Cliente apuntando a xAI (Grok)
client = OpenAI(
    api_key=os.getenv("XAI_API_KEY"),
    base_url="https://api.x.ai/v1"
)

class Prompt(BaseModel):
    prompt: str

@app.get("/")
def home():
    return {"status": "API Grok funcionando"}

@app.post("/chat")
def chat(data: Prompt):
    try:
        response = client.chat.completions.create(
            model="x-ai/grok-imagine-image/edit",
            messages=[
                {"role": "user", "content": data.prompt}
            ]
        )

        return {
            "response": response.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))