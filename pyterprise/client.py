from .handler import APICaller
from ._api_response_object import object_helper
from .organization import Organization
from .team import Team

class Client():
    """
    Base client class than can modify organizations and perform other administrative tasks, for workspace or granular changes
    organization helper class needs to be instiated. Set token and V2 API URL using the non default 'init' constructor method.
    """

    def __init__(self):
        return

    def init(self, token, url="https://app.terraform.io/api/v2", ssl_verification=True, version='v2', cloud=False):
        self.token = token
        self.url = url + f'/api/{version}/'
        self.headers = {
            'Content-Type': 'application/vnd.api+json',
            'Authorization': f'Bearer {token}'
        }
        self.ssl_verification = ssl_verification
<<<<<<< HEAD
        self._api_handler = APICaller(base_url=self.url, headers=self.headers)
        self.cloud = cloud

    def check_cloud(self):
        return self.cloud
=======
        self._api_handler = APICaller(
            base_url=self.url,
            headers=self.headers
        )
>>>>>>> e2aacb559097e8f39bddba29fad53d717f0937fb

    def list_organizations(self):
        """ Returns list of instantiated class objects for workspaces. """
        organizations = []
        response = self._api_handler.call(uri='organizations')
        for organization in response.data:
            organizations.append(
                Organization(
                    organization=object_helper(organization),
                    api_handler=self._api_handler
                )
            )
        return organizations

    def set_organization(self, id):
        """ Instantiates a given organization class based off the passed id/name. """
        response = self._api_handler.call(uri=f'organizations/{id}')
        return Organization(
            organization=object_helper(response.data),
            api_handler=self._api_handler
        )

    def create_organization(
        self,
        name,
        email,
        session_timeout=20160,
        session_remember=20160,
        collaborator_auth_policy='password',
        owners_team_saml_role_id=''):
        payload = {
            "data": {
                "type": "organizations",
                "attributes": {
                    "name": name,
                    "email": email,
                    "session-timeout": session_timeout,
                    "session-remember": session_remember,
                    "collaborator-auth-policy": collaborator_auth_policy,
                    "owners-team-saml-role-id": owners_team_saml_role_id
                }
            }
        }
        return self._api_handler.call(
            method='post',
            uri=f'organizations',
            json=payload
        ).data

    def destroy_organization(self, name):
        return self._api_handler.call(
            method='delete',
            uri=f"organizations/{name}"
        )
