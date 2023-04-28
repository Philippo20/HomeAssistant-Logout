import logging

DOMAIN = 'logout_control'

async def async_setup(hass, config):

    async def handle_refresh_token_clear(call):
        user = await hass.auth.async_get_user(hass.user.id)

        tokens = list(user.refresh_tokens.values())

        for token in tokens:
            await hass.auth.async_remove_refresh_token(token)

    hass.services.async_register(DOMAIN, 'clear_refresh_tokens', handle_refresh_token_clear)

    # Return boolean to indicate that initialization was successful.
    return True
