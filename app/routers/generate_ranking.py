from fastapi import APIRouter

from app.models.researcher import ResearchProfile
from app.resources.researcher_resource import MatchingService
from app.services.service_factory import ServiceFactory

router = APIRouter()


@router.get("/generate_ranking/{user_id}", tags=["users"])
async def get_user_research_match_ranking(user_id: str) -> list:

    # TODO Do lifecycle management for singleton resource
    res = ServiceFactory.get_service("MatchingService")
    result = res.get_by_key(user_id)
    return result

