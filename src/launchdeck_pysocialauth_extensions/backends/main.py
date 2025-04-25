from social_core.backends.azuread_tenant import AzureADTenantOAuth2


class LaunchDeckAzureADTenantOAuth2(AzureADTenantOAuth2):
    """
    Custom Azure AD OAuth2 backend for LaunchDeck.
    """

    name = "launchdeck-azuread-tenant-oauth2"

    @property
    def redirect_uri(self):
        return self.setting("REDIRECT_URI")