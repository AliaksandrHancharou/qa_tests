from selenium.webdriver.common.by import By


class TextBoxPageLocators:
    FULL_NAME = (By.CSS_SELECTOR, "input[id='userName']")
    EMAIL = (By.CSS_SELECTOR, "input[id='userEmail']")
    CURRENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='currentAddress']")
    PERMANENT_ADDRESS = (By.CSS_SELECTOR, "textarea[id='permanentAddress']")
    SUBMIT = (By.CSS_SELECTOR, "button[id='submit']")

    CREATED_FULL_NAME = (By.CSS_SELECTOR, "#output #name")
    CREATED_EMAIL = (By.CSS_SELECTOR, "#output #email")
    CREATED_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    CREATED_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")


class CheckBoxPageLocators:
    EXPAND_ALL = (By.CSS_SELECTOR, "button[title='Expand all']")
    ITEM_LIST = (By.CSS_SELECTOR, "span[class='rct-title']")
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class='rct-icon rct-icon-check']")
    TITLE_ITEM = ".//ancestor::span[@class='rct-text']"
    SELECTED_ITEMS = (By.CSS_SELECTOR, "span[class='text-success']")


class RadioButtonPageLocators:
    YES_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='yesRadio']")
    IMPRESSIVE_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='impressiveRadio']")
    NO_RADIO_BUTTON = (By.CSS_SELECTOR, "label[for='noRadio']")
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class='text-success']")


class WebTablesPageLocators:
    # add person form
    ADD_BUTTON = (By.CSS_SELECTOR, "button#addNewRecordButton")
    FIRST_NAME_INPUT = (By.CSS_SELECTOR, "input#firstName")
    LAST_NAME_INPUT = (By.CSS_SELECTOR, "input#lastName")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input#userEmail")
    AGE_INPUT = (By.CSS_SELECTOR, "input[id='age']")
    SALARY_INPUT = (By.CSS_SELECTOR, "input#salary")
    DEPARTMENT_INPUT = (By.CSS_SELECTOR, "input#department")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")

    # table
    PERSON_LIST = (By.CSS_SELECTOR, "div.rt-tr-group")
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[id='searchBox']")
    DELETE_BUTTON = (By.CSS_SELECTOR, "span[title='Delete']")
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    NO_ROWS_FOUND = (By.CSS_SELECTOR, "div[class='rt-noData']")
    COUNT_ROW_LIST = (By.CSS_SELECTOR, "select[aria-label='rows per page']")

    # update
    EDIT_BUTTON = (By.CSS_SELECTOR, "span[title='Edit']")


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='doubleClickBtn']")
    RIGHT_CLICK_BUTTON = (By.CSS_SELECTOR, "button[id='rightClickBtn']")
    JUST_CLICK = (By.XPATH, "//*[text()='Click Me']")

    # Results
    DOUBLE_CLICK_CHECK = (By.CSS_SELECTOR, "p[id='doubleClickMessage']")
    RIGHT_CLICK_CHECK = (By.CSS_SELECTOR, "p[id='rightClickMessage']")
    JUST_CLICK_CHECK = (By.CSS_SELECTOR, "p[id='dynamicClickMessage']")
