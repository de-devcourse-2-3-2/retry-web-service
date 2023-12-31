# from .settings import DATABASES  # for local
# from musinsa_trend.settings import DATABASES  # 이거 없으면 희한하게 계속 에러남. for linux
from musinsa_trend.musinsa_trend.settings import DATABASES
TEST_RUNNER = 'musinsa_trend.test_runner.TestRunner'
