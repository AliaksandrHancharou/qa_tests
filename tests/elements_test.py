from pages.elements_page import *


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
            text_box_page.open()
            input_data = [text_box_page.fill_all_field()]  # full_name, email, current_address, permanent_address
            output_data = [text_box_page.check_filled_form()]  # output_full_name, output_email,
            # output_current_address, output_permanent_address
            error_msg = ['the full name does not match', 'the email does not match',
                         'the current address does not match', 'the permanent address does not match',]
            for i in range(len(input_data)):
                assert input_data[i] == output_data[i], error_msg[i]

    class TestCheckBox:
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
            check_box_page.open()
            check_box_page.open_full_list()
            check_box_page.click_random_checkbox()
            list_in = check_box_page.get_checked_checkboxes()
            list_out = check_box_page.get_output_result()
            assert list_in == list_out

    class TestRadioButton:
        def test_radio_button(self, driver):
            radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
            radio_button_page.open()
            radio_button_page.click_radio_button('yes')
            radio_button_result_yes = radio_button_page.get_radio_button_result()
            radio_button_page.click_radio_button('impressive')
            radio_button_result_impressive = radio_button_page.get_radio_button_result()
            radio_button_page.click_radio_button('no')
            radio_button_result_no = radio_button_page.get_radio_button_result()

            assert radio_button_result_yes == 'Yes'
            assert radio_button_result_impressive == 'Impressive'
            assert radio_button_result_no == 'No'

    class TestLinksPage:
        def test_check_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            href_link, current_url = links_page.check_new_tab_simple_link()
            assert href_link == current_url

        def test_broken_link(self, driver):
            links_page = LinksPage(driver, 'https://demoqa.com/links')
            links_page.open()
            response_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert response_code == 400
