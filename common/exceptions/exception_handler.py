from common.base.base_test import BaseTest
from functools import wraps
from common.utils.screenshots.screenshot_utils import take_screenshot
from common.utils.logs.logger import setup_logger
from common.exceptions.custom_exceptions import *
from common.base.base_test import BaseTest
from selenium.common.exceptions import TimeoutException, NoSuchElementException

logger = setup_logger(__name__)

def handle_exceptions(func):
    @wraps(func)
    def wrapper(self: BaseTest, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)

        except TimeoutException as e:
            self.capture_screenshot("timeout")
            logger.error(f"⏱ TimeoutException in {func.__name__}: {e}")
            raise PageLoadTimeoutException(str(e))

        except NoSuchElementException as e:
            self.capture_screenshot("nosuch")
            logger.error(f"🔍 NoSuchElementException in {func.__name__}: {e}")
            raise ElementNotFoundException(str(e))

        except AssertionError as e:
            self.capture_screenshot("assert")
            logger.error(f"❌ AssertionError in {func.__name__}: {e}")
            raise AssertionFailureException(str(e))

        except Exception as e:
            self.capture_screenshot("failed")
            logger.exception(f"‼️ Unknown error in {func.__name__}: {e}")
            raise UnknownAutomationException(str(e))

    return wrapper  # type: ignore