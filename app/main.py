from fastapi import FastAPI, Path, Query
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()
 
@app.get('/num/{num}')
def give_num(num: int):
    return{'numner':num}

@app.get("/products/")
def get_products(category: str = None):
    if category:
        return {"category": category, "products": ["Фильтрованные товары"]}
    return {"products": ["Телефон", "Ноутбук", "Наушники"]}

class GetNews(BaseModel):
    text: str

def model(data):
    return 'Оценка'

@app.post('/text_analysis/rubert')
def text_analysis_news(data:GetNews):
    data_text = data.text
    pred = model(data.text)
    return {'score': pred}
