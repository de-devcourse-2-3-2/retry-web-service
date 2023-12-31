from django.test.runner import DiscoverRunner
import sqlite3


class TestRunner(DiscoverRunner):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            self.sqlite_conn = sqlite3.connect("/Users/wonkyungkim/Documents/pythondev/retry-web-service/data/sqlite3/musinsa.db")
        except:
            self.sqlite_conn = sqlite3.connect("musinsa.db")
        self.test_DB_cursor = self.sqlite_conn.cursor()

    # Creates the test databases by calling setup_databases()
    def setup_databases(self, **kwargs):
        try:
            self.sqlite_conn = sqlite3.connect(
                "/Users/wonkyungkim/Documents/pythondev/retry-web-service/data/sqlite3/musinsa.db")
        except:
            self.sqlite_conn = sqlite3.connect("musinsa.db")
        self.test_DB_cursor = self.sqlite_conn.cursor()

    # Destroys the test databases, restoring pre-test conditions by calling teardown_databases()
    def teardown_databases(self, old_config, **kwargs):
        # self.sqlite_conn.close()
        pass
