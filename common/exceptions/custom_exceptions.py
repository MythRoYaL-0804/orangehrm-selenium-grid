from selenium.common.exceptions import TimeoutException, NoSuchElementException

class NavigationException(Exception):
    """Exception khi xảy ra lỗi điều hướng trang."""

class ElementNotFoundException(NoSuchElementException):
    """Exception khi không tìm thấy phần tử trên trang."""

class PageLoadTimeoutException(TimeoutException):
    """Exception khi trang không load xong trong thời gian cho phép."""

class AssertionFailureException(AssertionError):
    """Exception khi assertion thất bại, custom để log đẹp hơn."""

class UnknownAutomationException(Exception):
    """Exception cho các lỗi không xác định trong quá trình test."""
