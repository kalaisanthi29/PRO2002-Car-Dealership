"""
Support module to establish and cleanup the temp SQLite db for integration tests. 
"""
import sqlite3
import tempfile
from pathlib import Path
import pytest


class IntegrationDatabase:
    """
    This establishes an isolated SQLite db for the integration tests. 
    NOTE: We use the same SQL schema as before, data only affect the test db now, not the production db. 
    See example from Module (5.4 Integration Testing for APIs and Persistence) for reference. 
    """

    def __init__(self):
        """
        This function establishes a temp db file and initializes the db. 
        NOTE: A bit different from the example in Module 5.4.
        """

        # Uses "with" to automatically handle closing of the file after establishing it.
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            self.path = Path(temp_file.name)
        self._initialize_db()

    def _initialize_db(self) -> None:
        """
        This function establishes the test db with our SQL schema:`schema.sql` 
        """

        # Goes to the root dir for the project to find the schema
        sql_path = Path(__file__).parents[2] / "car_dealership_api" / "data" / "schema.sql"
        sql = sql_path.read_text()

        conn = sqlite3.connect(self.path)
        try:
            conn.executescript(sql)
            conn.commit()
        finally:
            conn.close()

    def cleanup_db(self) -> None:
        """
        Simple function to delete the temp db file after the test is complete
        """
        self.path.unlink(missing_ok=True)


@pytest.fixture
def db_test():
    """
    The pytest.fixture helps to prepare the what the test needs before running.
    
    How it works visually {
        Start: Establishes a temp test db 
        -> yield provides db to test and pauses the fixture
        -> The test runs and either fail or passes
        End: The test completes and the fixture continues and finally deletes the db with cleanup_db()
    }
    
    This approach is better as it cleanup the temp db even if the test fails.
    """
    test_db = IntegrationDatabase()

    try:
        yield test_db
    finally:
        test_db.cleanup_db()
        print("Db deleted: ", not test_db.path.exists())
