from django.test.runner import DiscoverRunner


class TestRunner(DiscoverRunner):
    # Creates the test databases by calling setup_databases()
    def setup_databases(self, **kwargs):
        pass

    # Destroys the test databases, restoring pre-test conditions by calling teardown_databases()
    def teardown_databases(self, old_config, **kwargs):
        pass