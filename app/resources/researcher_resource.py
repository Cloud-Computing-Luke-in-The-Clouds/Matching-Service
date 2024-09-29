import requests

from typing import Any

from framework.resources.base_resource import BaseResource

from app.models.researcher import ResearchProfile, Config
from app.services.service_factory import ServiceFactory

class MatchingService(BaseResource):

    def __init__(self, config):
        super().__init__(config)

        # TODO -- Replace with dependency injection.
        #
        self.data_service = ServiceFactory.get_service("ResearcherResourceDataService")
        self.database = "p1_database"
        self.collection = "research_profile"
        self.key_field="sis_course_id"

    def generate_ranking(self, user_profile, research_profile) -> list:
        return [0,1,2]

    def get_by_key(self, key: str) -> ResearchProfile:

        d_service = self.data_service

        user_profile = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        research_profile = d_service.get_data_object(
            self.database, self.collection, key_field=self.key_field, key_value=key
        )

        # user_profile = requests.get("http://localhost:8002/researcher_profile/123")
        ranking = self.generate_ranking(user_profile, research_profile)

        return ranking


