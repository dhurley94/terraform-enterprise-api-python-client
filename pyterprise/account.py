from .handler import APICaller
from ._api_response_object import object_helper

class Account(object):
    def __init__(self, account, api_handler):
        self._api_handler = api_handler
        self.id = account.id
        attributes = account.attributes
        self.username = attributes.username
        self.is_service_account = attributes.is_service_account
        self.is_site_admin = attributes.is_site_admin
        self.is_sso_login = attributes.is_sso_login
        self.email = attributes.email
        self.unconfirmed_email = attributes.unconfirmed_email
        self.permissions = account.permissions
        self.relationships = account.relationships
        self.links = account.links
    
    def details(self):
        return self._api_handler.call(
            uri="account/details"
        )
    
    def update(self):
        payload = {
            "data": {
            "type": "users",
                "attributes": {
                    "email": self.email,
                    "username": self.username
                }
            }
        }
        return self._api_handler.call(
            method='patch',
            uri="account/update"
        )
    
    def change_password(self, current_password, new_password):
        payload = {
            "data": {
            "type": "users",
            "attributes": {
                    "current-password": current_password,
                    "password": new_password,
                    "password-confirmation": new_password,
                }
            }
        }
            return self._api_handler.call(
            method='patch',
            uri="account/password"
        )

