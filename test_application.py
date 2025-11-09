import unittest
from application import application # znaszego pliku cala nasza aplikacja zaimportuj


#teraz piszemy testy

class FlaskAppTest(unittest.TestCase):
    def setUp(self):
        self.app = application.test_client()#zeby miec dostep do tej aplikacji
        self.app.testing = True #zeby miec dostep do tej aplikacji

    #definiume test
    def test_home_page(self):
        response = self.app.get('/') #sprawdz co pobierzesz na sciece glwonej - to jest zapytanie
        data = response.data.decode('utf-8') #dobierz sie do tych danych jak juz pobraels
        self.assertIn('Witaj swiecie! ibig data z pythonem', data) #sprawdz czy cos znajduje sie w tym

if __name__ == '__main__':
    unittest.main()