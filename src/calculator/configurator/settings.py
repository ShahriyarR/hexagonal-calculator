class Settings:
    # Imagine this is a true production database connection
    db_uri = "postgresql://postgres:postgres@localhost:5432/postgres"


def get_database_uri() -> str:
    return Settings.db_uri
