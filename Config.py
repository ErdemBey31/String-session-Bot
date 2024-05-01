import os

ENVIRONMENT = False

if ENVIRONMENT:
    try:
        API_ID = 94575
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = "a3406de8d171bb422bb6ddf3bbd800e2"
    BOT_TOKEN = "7189521804:AAH8B6Yv92I-1N2m4wIsLDMjS63IvZJGDDc"
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = "Anonymous_Ch_Tr"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 94575
    API_HASH = "a3406de8d171bb422bb6ddf3bbd800e2"
    BOT_TOKEN = "7189521804:AAH8B6Yv92I-1N2m4wIsLDMjS63IvZJGDDc"
    DATABASE_URL = "postgresql://postgre_9kfd_user:15RVHcUF8SPQTBIstGpZMb5XqQ6x3Nxi@dpg-cop4js779t8c7382lcc0-a.oregon-postgres.render.com/postgre_9kfd"
    DATABASE_URL = DATABASE_URL
    MUST_JOIN = "@Anonymous_Tr_Ch"
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
