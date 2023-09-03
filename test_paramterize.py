import time
import pytest
from playwright.sync_api import Playwright, sync_playwright

@pytest.mark.parametrize("email", ["blaevidavid37@gmail.com", "test123",
                                             pytest.param("fakeemail.com", marks=pytest.mark.xfail),
                                             pytest.param("blaevidavid37@gmail.com", marks=pytest.mark.xfail)])
@pytest.mark.parametrize("password", ["test123",
                                             pytest.param("fakepassword", marks=pytest.mark.xfail),
                                             pytest.param("test123", marks=pytest.mark.xfail)])
def test_user_can_login(page, email, password) -> None:

