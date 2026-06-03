import data
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    call_taxi_button = (
        By.XPATH,
        "//button[text()='Pedir un taxi']"
    )

    comfort_tariff = (
        By.XPATH,
        "//div[text()='Comfort']"
    )

    phone_button = (
        By.XPATH,
        "//div[text()='Número de teléfono']"
    )
    phone_input = (By.ID, "phone")
    next_button = (
        By.XPATH,
        "//button[text()='Siguiente']"
    )
    sms_code_input = (By.ID, "code")
    confirm_code_button = (
        By.XPATH,
        "//button[text()='Confirmar']"
    )

    payment_method = (
        By.XPATH,
        "//div[contains(@class,'np-button')]"
    )
    add_card = (
        By.XPATH,
        "//div[contains(@class,'pp-plus-container')]"
    )
    card_number = (By.ID, "number")
    card_code = (
        By.XPATH,
        "//div[contains(@class,'card-code')]//input"
    )
    add_card_button = (
        By.XPATH,
        "//button[text()='Agregar']"
    )
    close_payment_modal_button = (
        By.XPATH,
        "//button[contains(@class,'close-button') and contains(@class,'section-close')]"
    )

    driver_message_field = (By.ID, 'comment')

    blanket_switch = (
        By.XPATH,
        "//div[contains(@class,'r-sw-container')]//span[contains(@class,'slider')]"
    )
    blanket_checkbox = (
        By.XPATH,
        "//div[contains(@class,'r-sw-container')]//input[@type='checkbox']"
    )

    ice_cream_plus = (
        By.XPATH,
        "//div[contains(@class,'counter-plus')]"
    )
    ice_cream_count = (
        By.XPATH,
        "//div[contains(@class,'counter-value')]"
    )

    order_taxi_button = (
        By.XPATH,
        "//button[contains(@class,'smart-button')]"
    )

    taxi_search_modal = (
        By.XPATH,
        "//div[contains(@class,'order-header-title')]"
    )

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.from_field)
        ).get_property("value")

    def get_to(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.to_field)
        ).get_property("value")

    def click_call_taxi(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.call_taxi_button)
        ).click()

    def click_comfort(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.comfort_tariff)
        ).click()

    def click_phone_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.phone_button)
        ).click()

    def enter_phone_number(self, phone_number):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.phone_input)
        ).send_keys(phone_number)

    def click_next_button(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.next_button)
        ).click()

    def enter_sms_code(self, code):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.sms_code_input)
        ).send_keys(code)

    def click_confirm_code(self):
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.confirm_code_button)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def get_phone_number_text(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'np-button')]//div[contains(@class,'np-text')]")
            )
        ).text

    def click_payment_method(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.payment_method)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def click_add_card(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.add_card)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def enter_card_number(self, number):
        field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.card_number)
        )
        self.driver.execute_script(
            "var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;"
            "nativeInputValueSetter.call(arguments[0], arguments[1]);"
            "arguments[0].dispatchEvent(new Event('input', {bubbles: true}));",
            field, number
        )

    def enter_card_code(self, code):
        field = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.card_code)
        )
        self.driver.execute_script(
            "var nativeInputValueSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;"
            "nativeInputValueSetter.call(arguments[0], arguments[1]);"
            "arguments[0].dispatchEvent(new Event('input', {bubbles: true}));"
            "arguments[0].dispatchEvent(new Event('blur', {bubbles: true}));",
            field, code
        )

    def click_add_card_button(self):
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.add_card_button)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def close_payment_modal(self):
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.close_payment_modal_button)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def enter_driver_message(self, message):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.driver_message_field)
        ).send_keys(message)

    def get_driver_message(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.driver_message_field)
        ).get_property('value')

    def click_blanket_switch(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.blanket_switch)
        )
        self.driver.execute_script("arguments[0].click();", element)

    def is_blanket_selected(self):
        checkbox = self.driver.find_element(*self.blanket_checkbox)
        return checkbox.get_property('checked')

    def click_ice_cream_plus(self, times=1):
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.ice_cream_plus)
        )
        for _ in range(times):
            self.driver.execute_script("arguments[0].click();", button)

    def get_ice_cream_count(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.ice_cream_count)
        ).text

    def click_order_taxi(self):
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(self.order_taxi_button)
        )
        self.driver.execute_script("arguments[0].click();", button)

    def is_taxi_search_modal_visible(self):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.taxi_search_modal)
        )
        return element.is_displayed()


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(data.urban_routes_url)

    def test_set_route(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_from(data.address_from)
        routes_page.set_to(data.address_to)
        assert routes_page.get_from() == data.address_from
        assert routes_page.get_to() == data.address_to

    def test_select_comfort_tariff(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_call_taxi()
        routes_page.click_comfort()
        comfort_element = self.driver.find_element(
            By.XPATH, "//div[text()='Comfort']"
        )
        assert comfort_element is not None

    def test_fill_phone_number(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_phone_button()
        routes_page.enter_phone_number(data.phone_number)
        routes_page.click_next_button()
        time.sleep(3)
        code = retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(code)
        routes_page.click_confirm_code()
        time.sleep(2)
        assert routes_page.get_phone_number_text() == data.phone_number

    def test_add_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_payment_method()
        time.sleep(2)
        routes_page.click_add_card()
        time.sleep(1)
        routes_page.enter_card_number(data.card_number)
        routes_page.enter_card_code(data.card_code)
        time.sleep(1)
        routes_page.click_add_card_button()
        time.sleep(2)
        card_display = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'pp-value-text')]")
            )
        )
        assert card_display is not None
        routes_page.close_payment_modal()
        time.sleep(1)

    def test_write_driver_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_driver_message(data.message_for_driver)
        assert routes_page.get_driver_message() == data.message_for_driver

    def test_request_blanket_and_tissues(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_switch()
        assert routes_page.is_blanket_selected() == True

    def test_order_2_ice_creams(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_ice_cream_plus(times=2)
        assert routes_page.get_ice_cream_count() == '2'

    def test_taxi_search_modal_appears(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_order_taxi()
        time.sleep(3)
        assert routes_page.is_taxi_search_modal_visible()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()