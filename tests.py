import logging
import time


def test_step1(test_page):
    logging.info("Test 1 Starting")
    test_page.go_to_site()
    test_page.enter_login("test")
    test_page.enter_pass("test")
    test_page.click_login_button()
    assert test_page.get_error_text() == "401"


def test_step2(test_page, test_data):
    logging.info("Test 2 Starting")
    test_page.go_to_site()
    test_page.enter_login(test_data["login"])
    test_page.enter_pass(test_data["password"])
    test_page.click_login_button()
    assert test_page.get_text_blog() == "Blog"


def test_step3(test_page, test_data):
    # 1 login
    logging.info("Test 3 Starting")
    test_page.go_to_site()
    test_page.enter_login(test_data["login"])
    test_page.enter_pass(test_data["password"])
    test_page.click_login_button()
    assert test_page.get_text_blog() == "Blog"

    # 2 create new post
    time.sleep(1)
    test_page.click_new_post()
    time.sleep(1)
    new_post_title_expected = "test post title"
    test_page.enter_new_post_title(new_post_title_expected)
    time.sleep(1)
    test_page.click_save_new_post()

    # 3 check new post
    time.sleep(1)
    assert test_page.get_post_title() == new_post_title_expected


def test_step4(test_page, test_data, email_report):
    logging.info("Test 4 Starting")
    test_page.go_to_site()

    # 1 login
    logging.info("1. Login")
    test_page.enter_login(test_data["login"])
    test_page.enter_pass(test_data["password"])
    test_page.click_login_button()
    assert test_page.get_text_blog() == "Blog"

    # 2 Contact
    logging.info("2. Contact")
    test_page.click_contact_button()
    time.sleep(1)

    # 3 Fill form
    logging.info("3. Fill form")
    test_page.enter_contact_name("Tester")
    test_page.enter_contact_email("some_email@test.com")
    test_page.enter_contact_content("some text")
    test_page.click_contact_contact_us_button()
    time.sleep(1)

    # 4 Check alert
    logging.info("4. Check alert")
    assert test_page.get_alert_text() == "Form successfully submitted"