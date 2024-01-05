import os

SECRET_KEY = os.environ["SECRET_KEY"]

class Config:
    LOGIN_API_ENDPOINT = os.environ["LOGIN_API_ENDPOINT"]
    ACCOUNT_API_ENDPOINT = os.environ["ACCOUNT_API_ENDPOINT"]
    ENQUIRY_API_ENDPOINT = os.environ["ENQUIRY_API_ENDPOINT"]
    CDN_URL = os.environ['CDN_URL']

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
