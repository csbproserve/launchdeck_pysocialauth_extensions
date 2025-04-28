from social_core.backends.azuread_tenant import AzureADTenantOAuth2, AzureADV2TenantOAuth2

class LaunchDeckAzureADTenantOAuth2(AzureADTenantOAuth2):
    name = "launchdeck-azuread-tenant-oauth2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redirect_uri = self.setting("REDIRECT_URI")
        self.redirect_uri = self.strategy.absolute_uri(self.redirect_uri)
    

class LaunchDeckAzureADV2TenantOAuth2(AzureADV2TenantOAuth2):
    name = "launchdeck-azuread-v2-tenant-oauth2"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redirect_uri = self.setting("REDIRECT_URI")
        self.redirect_uri = self.strategy.absolute_uri(self.redirect_uri)
 