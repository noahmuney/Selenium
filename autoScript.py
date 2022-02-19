from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def chrome_walla():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.headless = True
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    browser.get("https://www.walla.co.il")
    title1 = browser.title
    browser.refresh()
    title2 = browser.title
    assert title1 == title2, "Error"
    browser.quit()


def firefox_ynet():
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.get("https://www.ynet.co.il")
    title1 = browser.title
    browser.refresh()
    title2 = browser.title
    assert title1 == title2, "Error"
    browser.quit()


def chrome_other():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.headless = True
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    browser.get("https://translate.google.com")
    # first locator
    browser.find_element(By.XPATH,
                         "/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea").send_keys(
        "ראשון")
    browser.get("https://www.youtube.com")
    search_box = browser.find_element(By.XPATH,
                                      "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")
    search_box.click()
    search_box.send_keys("never gonna give you up")
    browser.find_element(By.ID, "search-icon-legacy").click()
    browser.get("https://translate.google.com")
    # second and third locators
    text_box = browser.find_element(By.CLASS_NAME, "er8xn")
    text_box.send_keys("שני")
    text_box.clear()
    browser.find_element(By.TAG_NAME, "textarea").send_keys("שלישי")
    print(text_box)
    browser.get("https://www.facebook.com")
    browser.find_element(By.ID, "email").send_keys("email@example.com")
    browser.find_element(By.ID, "pass").send_keys("password")
    browser.find_element(By.NAME, "login").click()
    browser.delete_all_cookies()
    cookies = browser.get_cookies()
    print(cookies)
    browser.get("https://www.github.com")
    github_search = browser.find_element(By.NAME, "q")
    github_search.send_keys("Selenium" + Keys.ENTER)


def disable_extensions():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("https://www.google.com/")
    # firefox extensions are disabled by default
    from selenium.webdriver.firefox.options import Options
    options = Options()
    options.add_argument("-headless")
    browser = webdriver.Firefox(options=options)
    browser.get("https://www.google.co.il")
    # how can IE run in the container?
    # I couldn't find any info on IE extensions


chrome_walla()
firefox_ynet()
chrome_other()
disable_extensions()
