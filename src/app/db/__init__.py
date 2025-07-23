def run_migrations():

    import os
    from alembic.config import Config
    from alembic import command

    from ..core.config import settings

    BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    )

    ALEMBIC_INI_PATH = os.path.join(BASE_DIR, "alembic.ini")

    alembic_cfg = Config(ALEMBIC_INI_PATH)

    alembic_cfg.set_main_option(
        "sqlalchemy.url",
        settings.sql_connection_string,
    )

    print("Running migrations...")

    command.upgrade(alembic_cfg, "head")
