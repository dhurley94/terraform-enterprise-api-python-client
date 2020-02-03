from ._api_response_object import object_helper
from .handler import APICaller

class policies(object):
    def __init__(self, policy, api_handler):
        self._api_handler = api_handler
        self.id = policy.id
        attributes = account.attributes
        self.name = attributes.name
        self.description = attributes.description
        self.enforce = attributes.enforce
        self.policy_set_count = attributes.policy_set_count
        self.email = attributes.email
        self.unconfirmed_email = attributes.unconfirmed_email
        relationships = account.relationships
        self.relationships = relationships
        self.organizations = relationships.organizations
        self.policy_sets = relationships.policy_sets
        self.links = account.links

    def show(self):
        return self._api_handler.call(
            uri=f"policies/{self.id}"
        ).data
    
    def list(self, organization):
        if organization in self.organizations.data:
            return self._api_handler.call(
                uri=f"organizations/{organization}/policies"
            )
        return self.organizations.data

    def list(self):
            return self._api_handler.call(
                uri=f"organizations/{organization}/policies"
            ).data
    
    def delete(self):
        return self._api_handler.call(
            uri=f"policies/{self.policy_id}"
        )