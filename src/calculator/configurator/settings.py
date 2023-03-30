import os


class Settings:
    # Imagine this is a true production database connection
    db_uri = (
        "sqlite:///tutorial.db"
        if os.getenv("TEST_RUN")
        else "postgresql://postgres:postgres@localhost:5432/postgres"
    )


def get_database_uri() -> str:
    return Settings.db_uri
