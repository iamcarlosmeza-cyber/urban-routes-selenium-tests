# Urban Routes — UI Test Automation

End-to-end UI tests for Urban Routes, a taxi-booking web app. The suite covers the full ride-request flow, from setting the route to the driver-search modal.

## Stack
- Python 3 · Selenium WebDriver · pytest
- Page Object Model: locators and page actions live in `UrbanRoutesPage`, separate from the tests
- Explicit waits (`WebDriverWait` + Expected Conditions) for dynamic elements
- Chrome DevTools Protocol (CDP) to intercept the SMS confirmation code

## What's tested
Tests live in the `TestUrbanRoutes` class in `test_main.py`.

| Test | Checks |
|---|---|
| `test_set_route` | Origin and destination are set |
| `test_select_comfort_tariff` | Comfort tariff is selected |
| `test_fill_phone_number` | Phone number is added and confirmed with the SMS code |
| `test_add_credit_card` | A credit card is added |
| `test_write_driver_message` | A message for the driver is saved |
| `test_request_blanket_and_tissues` | Blanket and tissues are requested |
| `test_order_2_ice_creams` | Two ice creams are added |
| `test_taxi_search_modal_appears` | The driver-search modal appears |

## Run it
Requires Python 3 and Google Chrome. Selenium 4.6+ downloads ChromeDriver automatically.

```bash
pip install -r requirements.txt
```

The app ran on a temporary TripleTen test server. Set the server URL in `data.py`:

```python
urban_routes_url = 'https://<your-server-url>?lng=es'
```

Then run from the project root:

```bash
pytest test_main.py -v
```

Built as part of the TripleTen QA Engineering program.
