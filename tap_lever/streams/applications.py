import aiohttp
import singer
from tap_lever.streams import cache as stream_cache
from tap_lever.streams.base import BaseStream, ChildAsync

LOGGER = singer.get_logger()  # noqa


class CandidateApplicationsStream(BaseStream):
    API_METHOD = "GET"
    TABLE = "candidate_applications"

    @property
    def path(self):
        return "/candidates/{candidate_id}/applications"

    def get_url(self, candidate):
        _path = self.path.format(candidate_id=candidate)
        return "https://api.lever.co/v1{}".format(_path)

    def sync_data(self):
        table = self.TABLE

        candidates = stream_cache.get("candidates")
        LOGGER.info("Found {} candidates in cache".format(len(candidates)))

        params = self.get_params(_next=None)
        for i, candidate in enumerate(candidates):
            LOGGER.info(
                "Fetching referrals for candidate {} of {}".format(
                    i + 1, len(candidates)
                )
            )
            candidate_id = candidate["id"]
            url = self.get_url(candidate_id)
            resources = self.sync_paginated(url, params)


class OpportunityApplicationsStream(ChildAsync):
    API_METHOD = "GET"
    TABLE = "opportunity_applications"

    @property
    def path(self):
        return "/opportunities/{opportunity_id}/applications"

    def get_url(self, opportunity):
        _path = self.path.format(opportunity_id=opportunity)
        return "https://api.lever.co/v1{}".format(_path)
