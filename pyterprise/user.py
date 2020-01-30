
class User(object):
    def __init__(self, user):
        self.id = user.id
        attributes = user.attributes
        self.username = attributes.username
        self.is_service_account = attributes.is_service_account
        self.avatar_url = attributes.avatar_url
        self.v2_only = attributes.v2_only
        self.permissions = attributes.permissions
        relationships = user.relationships
        self.authentication_tokens = relationships.authentication_tokens
        self.links = user.links