from abc import abstractmethod
from contextlib import AbstractAsyncContextManager
from typing import Any, Protocol


class Browser(Protocol):
    async def new_page(self) -> None: ...
    async def close(self) -> None: ...


class WebClient(AbstractAsyncContextManager):
    @abstractmethod
    async def __aenter__(self):
        """Enter the async context"""
        pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Exit the async context"""
        pass

    @abstractmethod
    async def new_page(self) -> Any:
        """Create new page for scraping"""
        pass

    @abstractmethod
    async def goto(self, page: Any, url: str) -> None:
        """Navigate to URL"""
        pass

    @abstractmethod
    async def close_page(self, page: Any) -> None:
        """Close page"""
        pass

    @abstractmethod
    async def get_browser(self) -> Browser:
        """Returns a browser instance"""
        pass
