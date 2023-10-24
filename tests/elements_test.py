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

    class TestWebTables:
        def test_web_table_add_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            added_persons = list(web_tables_page.add_person(1))
            full_person_list = web_tables_page.get_person_list()
            assert added_persons in full_person_list

        def test_web_table_search_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            key_word = list(web_tables_page.add_person(1))[0]
            web_tables_page.search_person(key_word)
            table_result = web_tables_page.check_search_person()
            assert key_word in table_result

        def test_web_table_update_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            last_name = web_tables_page.add_person()[1]
            web_tables_page.search_person(last_name)
            age = web_tables_page.update_person_info()
            row = web_tables_page.check_search_person()
            assert age in row

        def test_web_table_delete_person(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            email = web_tables_page.add_person()[3]
            web_tables_page.search_person(email)
            web_tables_page.delete_person()
            text = web_tables_page.check_deleted()
            assert text == 'No rows found'

        def test_web_table_change_count_row(self, driver):
            web_tables_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
            web_tables_page.open()
            count = web_tables_page.select_up_to_some_rows()
            assert count == [5, 10, 20, 25, 50, 100], ('The number of rows in the table has not been changed'
                                                       ' or has changed incorrectly')

    class TestButtonsPage:
        def test_buttons_click(self, driver):
            buttons_page = ButtonsPage(driver, 'https://demoqa.com/buttons')
            buttons_page.open()
            double = buttons_page.click_buttons('double')
            right = buttons_page.click_buttons('right')
            click = buttons_page.click_buttons('click')
            assert double == 'You have done a double click'
            assert right == 'You have done a right click'
            assert click == 'You have done a dynamic click'

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
