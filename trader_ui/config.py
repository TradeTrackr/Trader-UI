import os

class Config:

    def convert_to_bool(value):
        if value == "True":
            return True
        elif value == "False":
            return False

    ALLOW_HTTPS_TRAFFIC_ONLY = convert_to_bool(
        os.environ.get("ALLOW_HTTPS_TRAFFIC_ONLY", "True")
    )

    APP_NAME = os.environ["APP_NAME"]
    SECRET_KEY = os.environ["SECRET_KEY"]
    password_photo = os.environ["password_photo"]
    reset_photo = os.environ["reset_photo"]
    login_photo = os.environ["login_photo"]
    SESSION_COOKIE_SECURE = convert_to_bool(os.environ["SESSION_COOKIE_SECURE"])
    REMEMBER_COOKIE_SECURE = convert_to_bool(os.environ["REMEMBER_COOKIE_SECURE"])

    # APIs
    LOGIN_API_URL = os.environ["LOGIN_API_URL"]
    CDN_URL = os.environ["CDN_URL"]
    ACCOUNT_API_URL = os.environ["ACCOUNT_API_URL"]

    # For logging
    FLASK_LOG_LEVEL = os.environ["FLASK_LOG_LEVEL"]

    LOGCONFIG = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {"()": "trader_ui.extensions.JsonFormatter"},
            "audit": {"()": "trader_ui.extensions.JsonAuditFormatter"},
        },
        "filters": {
            "contextual": {"()": "trader_ui.extensions.ContextualFilter"}
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "simple",
                "filters": ["contextual"],
                "stream": "ext://sys.stdout",
            },
            "audit_console": {
                "class": "logging.StreamHandler",
                "formatter": "audit",
                "filters": ["contextual"],
                "stream": "ext://sys.stdout",
            },
        },
        "loggers": {
            "application": {"handlers": ["console"], "level": FLASK_LOG_LEVEL},
            "audit": {"handlers": ["audit_console"], "level": "INFO"},
        },
    }
