from tap_lever.streams.base import BaseStream


class OpportunityFeedbackStream(BaseStream):
    API_METHOD = "GET"
    TABLE = "opportunity_feedback"

    @property
    def path(self):
        return "/opportunities/{opportunity_id}/feedback"

    def get_url(self, opportunity):
        _path = self.path.format(opportunity_id=opportunity)
        return "https://api.lever.co/v1{}".format(_path)

    def sync_data(self, opportunity_id):
        params = self.get_params(_next=None)
        url = self.get_url(opportunity_id)
        resources = self.sync_paginated(url, params)
