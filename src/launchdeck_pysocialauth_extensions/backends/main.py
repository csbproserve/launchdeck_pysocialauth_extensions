from social_core.backends.azuread_tenant import AzureADTenantOAuth2


class LaunchDeckAzureADTenantOAuth2(AzureADTenantOAuth2):
    """
    Custom Azure AD OAuth2 backend for LaunchDeck.
    """

    name = "launchdeck-azuread-tenant-oauth2"

    @property
    def redirect_uri_override(self):
        return self.setting("REDIRECT_URI")
    
    @redirect_uri_override.setter
    def redirect_uri_override(self):
        self.redirect_uri = self.setting("REDIRECT_URI")