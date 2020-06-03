from selenium.webdriver.common.by import By

class HomePageLocators():
    """Selektory strony głównej"""
    POKAŻ_btn = (By.CSS_SELECTOR, 'button[data-testid="submit-btn"]')
    MARKA_POJAZDU = (By.CSS_SELECTOR, 'input[id="filter_enum_make"]')
    MODEL_POJAZDU = (By.CSS_SELECTOR, 'input[id="filter_enum_make"][class="ds-select"]')
    CENA_OD = (By.CSS_SELECTOR, 'input[id="filter_float_price:from"]')
    CENA_DO = (By.CSS_SELECTOR, 'input[id="filter_float_price:to"]')
    ROK_OD = (By.CSS_SELECTOR, 'input[id="filter_float_year:from"]')
    ROK_DO = (By.CSS_SELECTOR, 'input[id="filter_float_year:to"]')
    PRZEBIEG_OD = (By.CSS_SELECTOR, 'input[id="filter_float_mileage:from"]')
    PRZEBIEG_DO = (By.CSS_SELECTOR, 'input[id="filter_float_mileage:to"]')
    RODZAJ_PALIWA = (By.CSS_SELECTOR, 'input[id="filter_enum_fuel_type"]')
    NUMER_VIN = (By.CSS_SELECTOR, 'label[for="filter_enum_has_vin"]')

class AfterSearchLocators():
    OBSERWUJ_btn = (By.CSS_SELECTOR, 'div[class="favorite-box ds-favorite-block"]')
    BRAK_WYNIKÓW = (By.XPATH, '//h1[text()="Brak wyników wyszukiwania."]')
