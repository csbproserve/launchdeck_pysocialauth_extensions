from social_core.backends.azuread_tenant import AzureADTenantOAuth2


class LaunchDeckAzureADTenantOAuth2(AzureADTenantOAuth2):
    """
    Custom Azure AD OAuth2 backend for LaunchDeck.
    """

    name = "launchdeck-azuread-tenant-oauth2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redirect_uri = self.setting("REDIRECT_URI")
        self.redirect_uri = self.strategy.absolute_uri(self.redirect_uri)
    
    def request_access_token(self, *args, **kwargs):
        print("Requesting access token with args:", args, "and kwargs:", kwargs)
        access_token =  super().request_access_token(*args, **kwargs)
        print("Access token received:", access_token)
        return access_token
    
    def user_data(self, *args, **kwargs):
        response = super().user_data(*args, **kwargs)
        print("User data received:", response)
        return response
    
    def auth_complete(self, *args, **kwargs):
        print("Completing authentication with args:", args, "and kwargs:", kwargs)
        auth_repsonse = super().auth_complete(*args, **kwargs)
        print("Authentication response:", auth_repsonse)
        return auth_repsonse