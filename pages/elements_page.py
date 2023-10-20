from locators.elements_page_locator import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from .base_page import BasePage
from generator.generator import generated_person
from selenium.webdriver.common.by import By
import random


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_field(self):
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):
        out_full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        out_email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        out_current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        out_permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return out_full_name, out_email, out_current_address, out_permanent_address


class CheckBoxPage(BasePage):

    locators = CheckBoxPageLocators()

    def open_full_list(self):
        self.element_is_visible(self.locators.EXPAND_ALL).click()

    def click_random_checkbox(self):
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        for i in range(21):
            item = random.choice(item_list)
            self.go_to_element(item)
            item.click()

    def get_checked_checkboxes(self):
        checked_list = self.elements_are_present(self.locators.CHECKED_ITEMS)
        data = [box.find_element(By.XPATH, self.locators.TITLE_ITEM).text.lower() for box in checked_list]
        return str(data).replace(' ', '').replace('.doc', '')

    def get_output_result(self):
        result_list = self.elements_are_present(self.locators.SELECTED_ITEMS)
        data_out_titles = [item.text.lower() for item in result_list]
        return str(data_out_titles).replace(' ', '').lower()


class RadioButtonPage(BasePage):

    locators = RadioButtonPageLocators()

    def click_radio_button(self, choice):
        choices = {
            'yes': self.locators.YES_RADIO_BUTTON,
            'no': self.locators.NO_RADIO_BUTTON,
            'impressive': self.locators.IMPRESSIVE_RADIO_BUTTON
        }
        self.element_is_visible(choices[choice]).click()

    def get_radio_button_result(self):
        return self.element_is_present(self.locators.OUTPUT_RESULT).text
