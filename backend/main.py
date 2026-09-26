"""Backend Bài 9: thời tiết và danh sách thành phố yêu thích."""

import os
import sqlite3
from pathlib import Path

import requests
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field


ROOT_DIR = Path(__file__).resolve().parents[1]
load_dotenv(ROOT_DIR / ".env")

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
DB_PATH = ROOT_DIR / "weather.db"

app = FastAPI(title="Bài 9 - Weather Favorites API")


class FavoriteCity(BaseModel):
    city_name: str = Field(min_length=1, max_length=100)


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def init_database():
    # TODO 1/5: Tạo bảng favorite_cities gồm id và city_name UNIQUE.
    pass


def get_weather(city: str):
    params = {"q": city, "appid": API_KEY, "units": "metric", "lang": "vi"}
    try:
        response = requests.get(WEATHER_URL, params=params, timeout=10)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    data = response.json()
    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
    }


init_database()


@app.get("/")
def home():
    return {"message": "Weather Favorites API đang chạy"}


@app.get("/weather")
def weather(city: str):
    data = get_weather(city)
    if data is None:
        raise HTTPException(status_code=404, detail="Không tìm thấy thành phố")
    return data


@app.get("/cities")
def list_cities():
    # TODO 2/5: SELECT các thành phố, đổi từng sqlite3.Row thành dict rồi trả về list.
    return []


@app.post("/cities", status_code=status.HTTP_201_CREATED)
def add_city(city: FavoriteCity):
    # TODO 3/5: INSERT city.city_name và commit; nếu bị trùng, trả lỗi HTTP 409.
    return {"success": False, "message": "Chưa hoàn thành chức năng lưu"}


@app.delete("/cities/{city_name}")
def delete_city(city_name: str):
    # TODO 4/5: DELETE theo city_name, commit và trả về {"deleted": city_name}.
    return {"deleted": None}

