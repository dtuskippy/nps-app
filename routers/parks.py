import os
import httpx
from fastapi import APIRouter
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/parks", tags=["parks"])

NPS_API_KEY = os.environ.get("NPS_API_KEY")
NPS_BASE_URL = "https://developer.nps.gov/api/v1"

@router.get("/activities")
async def get_activities():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{NPS_BASE_URL}/activities",
            params={"limit": 100, "api_key": NPS_API_KEY}
        )
        data = response.json()
        return [{"name": activity["name"]} for activity in data["data"]]


@router.get("/search")
async def search_parks(state: str, activity: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{NPS_BASE_URL}/parks",
            params={"stateCode": state, "limit": 50, "api_key": NPS_API_KEY}
        )
        data = response.json()
        filtered = [
            {
                "parks": park["fullName"],
                "description": park["description"],
                "image": park["images"][0]["url"] if park["images"] else None
            }
            for park in data["data"]
            if any(a["name"].casefold() == activity.casefold() for a in park["activities"])
        ]
        return filtered
