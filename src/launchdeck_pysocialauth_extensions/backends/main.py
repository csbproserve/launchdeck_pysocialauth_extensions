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
