import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Parse command args for select language for Chrome browser."""
    parser.addoption('--language', action='store', default='en',
                     help="Choose language for browser")


@pytest.fixture(scope="function")
def browser(request):
    """Start Chrome browser for test-funcs. Add language options from command args.
    End close browser after every test-func."""
    selected_language = request.config.getoption("language")
    browser = None
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': selected_language})
    browser = webdriver.Chrome(options=options)
    print(f'\nStart Chrome browser with "{selected_language}" language')

    yield browser
    print("\nquit browser..")
    browser.quit()
