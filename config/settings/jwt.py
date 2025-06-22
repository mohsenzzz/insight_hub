import datetime

from config.env import env

# For more settings
# Read everything from here - https://styria-digital.github.io/django-rest-framework-jwt/#additional-settings

# Default to 7 days


# JWT (JSON Web Token) Configuration
# Settings for token-based authentication using SimpleJWT
SIMPLE_JWT = {
    # Token lifetime settings
    # Access token expiration time
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(
        minutes=int(env("LIFETIME_ACCESS_TOKEN_MINUTES"))
    ),
    # Refresh token expiration time
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(
        days=int(env("LIFETIME_REFRESH_TOKEN_DAYS"))
    ),
    # Token rotation settings
    "ROTATE_REFRESH_TOKENS": True,  # Generate new refresh token with every refresh
    # User identification settings
    "USERNAME_FIELD": "username",  # Field used for user identification
    "USERNAME_CLAIM": "username",  # Claim name in the JWT payload
}


