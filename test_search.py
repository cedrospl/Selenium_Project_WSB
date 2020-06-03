# Import niezbędnych bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from locators import HomePageLocators
from locators import AfterSearchLocators


make = "Ferrari"
model = "Hurakan"
price_from = "50000"
price_to = "500000"
year_from = "2017"
year_to = "2020"
mileage_from = "20000"
mileage_to = "250000"
fuel = "benzyna"


class OtoMotoTestSearchForCheapLamborghini(unittest.TestCase):

    """Ustawiam driver"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    """Uruchamiam przeglądarkę ze stroną OtoMoto"""
    def test_runChromeBrowserWithOtoMoto(self):
        driver = self.driver
        driver.get("https://otomoto.pl")
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(HomePageLocators.MARKA_POJAZDU))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(HomePageLocators.MARKA_POJAZDU))
        assert "OTOMOTO - nowe i używane samochody i motocykle" in self.driver.title
        print("Weryfikacja strony OTOMOTO")
        marka = self.driver.find_element(*HomePageLocators.MARKA_POJAZDU)
        marka.send_keys(make)
        marka.send_keys(Keys.RETURN)
        cena_od = self.driver.find_element(*HomePageLocators.CENA_OD)
        cena_od.send_keys(price_from)
        cena_od.send_keys(Keys.RETURN)
        cena_do = self.driver.find_element(*HomePageLocators.CENA_DO)
        cena_do.send_keys(price_to)
        cena_do.send_keys(Keys.RETURN)
        rok_od = self.driver.find_element(*HomePageLocators.ROK_OD)
        rok_od.send_keys(year_from)
        rok_od.send_keys(Keys.RETURN)
        rok_do = self.driver.find_element(*HomePageLocators.ROK_DO)
        rok_do.send_keys(year_to)
        rok_do.send_keys(Keys.RETURN)
        przebieg_od = self.driver.find_element(*HomePageLocators.PRZEBIEG_OD)
        przebieg_od.send_keys(mileage_from)
        przebieg_od.send_keys(Keys.RETURN)
        przebieg_do = self.driver.find_element(*HomePageLocators.PRZEBIEG_DO)
        przebieg_do.send_keys(mileage_to)
        przebieg_do.send_keys(Keys.RETURN)
        rodzaj_paliwa = self.driver.find_element(*HomePageLocators.RODZAJ_PALIWA)
        rodzaj_paliwa.send_keys(fuel)
        rodzaj_paliwa.send_keys(Keys.RETURN)
        numer_vin = self.driver.find_element(*HomePageLocators.NUMER_VIN)
        numer_vin.click()
        WebDriverWait(driver, 5)
        przycisk_pokaż = self.driver.find_element(*HomePageLocators.POKAŻ_btn)
        przycisk_pokaż.click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(AfterSearchLocators.BRAK_WYNIKÓW))
        brak_wyników = driver.find_element(*AfterSearchLocators.BRAK_WYNIKÓW)
        print(brak_wyników.text)
        self.assertEqual(brak_wyników.text, "Brak wyników wyszukiwania.")

    """Zamykam przeglądarkę"""
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
