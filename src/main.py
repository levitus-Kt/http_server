from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="src/templates")

@app.get("/", response_class=HTMLResponse, summary="Главная ручка/эндпойнт/роут", tags=['Основные ручки'])
async def main(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request,
        }
        )

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="")