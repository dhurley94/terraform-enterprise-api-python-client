from ._api_response_object import object_helper
from .ssh_key import SSHKey
from .user import User

class Team(object):
    def __init__(self, team, organization_name, api_handler):
        self._api_handler = api_handler
        
        self.id = team.id
        attributes = team.attributes
        self.name = attributes.name
        self.users_count = attributes.users_count
        self.visibility = attributes.visibility
        self.permissions = attributes.permissions
        self.organization_access = attributes.organization_access
        relationships = workspace.relationships
        self.users = relationships.users
        self.authentication_token = relationships.authentication_token
        self.links = team.links
    
    def generate_token(self):
        """
        Generates a new team token and overrides existing token if one exists.
        https://www.terraform.io/docs/cloud/api/team-tokens.html#generate-a-new-team-token
        """
        return self._api_handler.call(
            uri=f'teams/{id}/authentication-token',
            method='post'
        ).data
    
    def remove_token(self):
        """
        Deletes existing team token
        https://www.terraform.io/docs/cloud/api/team-tokens.html#delete-the-team-token
        """
        return self._api_handler.call(
            uri=f'teams/{id}/authentication-token',
            method='delete'
        ).data

    def list_access(self):
        return self._api_handler.call(
            uri=f'team-workspaces',
            method='get'
        ).data

    def assign_workspace(self, workspace_id, access):
        """
        https://www.terraform.io/docs/cloud/api/team-access.html#add-team-access-to-a-workspace
        """
        payload = {
            "data": {
                "attributes": {
                    "access": access
                },
                "relationships": {
                    "workspace": {
                    "data": {
                        "type":"workspaces",
                        "id": workspace_id
                    }
                },
                "team": {
                    "data": {
                        "type":"teams",
                        "id": self.id
                    }
                    }
                },
                "type":"team-workspaces"
            }
        }
        return self._api_handler.call(
            uri=f'team-workspaces',
            method='post',
            json=payload).data
    
    def assign_user(self, user):
        """
        This method adds multiple users to a team.
        Both users and teams must already exist.
        https://www.terraform.io/docs/cloud/api/team-members.html#add-a-user-to-team
        """
        payload = {
            "data": {
                {
                    "type": "users",
                    "id": user
                }
            }
        }
        return self._api_handler.call(
            uri=f'teams/{self.id}/relationships/users',
            method='post',
            json=payload).data
            
    def delete_user(self, user):
        """
        This method removes multiple users from a team.
        Both users and teams must already exist
        This DOES NOT delete the user; it only removes them from this team.
        https://www.terraform.io/docs/cloud/api/team-members.html#delete-a-user-from-team
        """
        payload = {
        "data": {
            {
                "type": "users",
                "id": user
            }
        }
    }
    return self._api_handler.call(
        uri=f'teams/{self.id}/relationships/users',
        method='delete',
        json=payload).data