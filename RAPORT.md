> **Michał Lechowicz GL.02**

# Mastermind - projekt z przedmiotu Języki Symboliczne

### Dokumentacja

## Temat projektu:

Tematem projekty jest **gra Mastermind**. Program odtwarza grę Mastermind wynalezioną przez Mordechaja Meirowitza. Celem
gry jest odgadnięcie kodu wylosowanego przez komputer, w ciągu 12 rund.
[Wikipedia](https://pl.wikipedia.org/wiki/Mastermind_(gra_planszowa)).

## Reguły gry:

1. Gracz wpisuje 4 cyfrowy kod złożony z liczb od 1 do 6;
2. Następnie komputer sprawdza czy kod jest prawidłowy:
    * Jeśli liczba jest tożsama z kodem, gracz wygrywa i gra się kończy.
    * Jeśli nie do pola odpwiedzi dopisywana jest odpowiedź zawierająca:
        * Liczbę wpisaną przez gracza;
        * Liczbę cyfr na poprawnych pozycjach;
        * Liczbę cyfr występujących w kodzie, ale na złych pozycjach.
    * Jeśli po 12 rundach gracz nie odgadł kodu, przegrywa.
3. W grze zaimplementowano również nieuczciwe reguły gry, w których komputer oszukuje;
4. Gracz nie wie, według których reguł (opisanych wyżej, czy tych nieuczciwych) toczona jest rozgrywka;
5. Jeśli ma pewność, że gra jest sfałszowana może kliknąć przycisk oszust, wtedy:
    * Jeśli miał rację gra kończy się informacją *Złapałeś/łaś mnie!* ;
    * Jeśli gra toczyła się według właściwych reguł wyświetlany jest komunikat *Tere fere* wraz z wylosowanym kodem.

## Opis interfejsu:

Gra posiada interfejs graficzny, służący do obsługi. Kod jest wpisywany z klawiatury. Istnieje również możliwość
zresetowania gry. Wtedy gra toczy się według od nowa wylosowanych reguł z nowym kodem do ogadnięcia.

Po uruchomieniu okno programu podzielone jest na dwa bloki:

1. Lewy blok służący do interakcji z programem. Podzielony jest na dwa podbloki:

* Na czerwonym tle znajdują się przyciski służące do gry;
* Na niebieskim tle znajdują się informacje o programie oraz skrócona instrukcja obsługi;

2. Prawy blok składa się z miejsca na odpowiedzi udzielone przez użytkownika

Jeśli użytkownik wpisze błędny kod (za krótki, za długi, z niewłaściwymi znakami, cyframi), wtedy program odrzuca kod, a
użytkownik nie traci tury. Na dole okna wyświetlana jest na pasku informacja, z jakiego powodu kod został odrzucony.

## Składowe projektu:

### Plik [main](https://github.com/ichal6/Mastermind/blob/master/src/main.py)

Moduł startowy programu. Zawiera w sobie klasę **App** służącą do inicjalizacji aplikacji.

- Klasa [App](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/main.py#L14):
  Odpowiada za inicjalizację GUI, wykorzystując **tkinter**. Tworzy obiekty klasy **SecretCode**, losuje zestaw reguł **
  RuleGame**, inicjalizuje **TkInterView** oraz **ControllerGame**.

### Klasa [View](https://github.com/ichal6/Mastermind/blob/master/src/Views/View.py)

Klasa abstrakcyjna. Dziedziczą po niej **ConsoleView** oraz **TkInterView**. Odpowiada za wyświetlenie interfejsu oraz
inicjuje wszystkie interakcje z użytkownikiem.

Metody:

- [__init__](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/View.py#L6):
  Inicjalizuje interfejs. Tworzy zmienną prywatną __controller
- [set_controller](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/View.py#L8):
  Ustawia wartość zmiennej __controller
- [controller (property)](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/View.py#L11-L13):
  Metoda służąca do pobierania controllera
- [is_cheater](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/View.py#L15-L26):
  Metoda służąca do sprawdzenia, według których reguł toczona jest rozgrywka.
- [Pozostałe metody](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/View.py#L28-L65):
  abstrakcyjne, zostaną omówione przy klasie *TkInterView*

### Klasa [TkInterView](https://github.com/ichal6/Mastermind/blob/master/src/Views/TkInterView.py)

- [Funkcja messagebox](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L10-L14):
  Służy do wyświetlania popup-a informacyjnego. Poza ciałem klasy.

Klasa dziedzicąca z **View**. Odpowiada za interakcje z użytkownikiem za pomocą biblioteki tkinter:

Metody:

- [answer](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L90-L100):
  Wyświetla odpowiedź od programu, dodając ją do listy odpowiedzi.
- [__
  init__](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L18-L28):
  Metoda inicjalizuje **Frame** i dodaje go do głównego okna programu. Wywyołuje szereg podmetod do inicjalizacji
  interfejsu
- [metody inicjalizujące](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L30-L88):
  Metody służące do inicjalizacji głównego okna programu
- [metody win oraz game_over](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L102-L108):
  Używają funkcji messagebox, by wyświetlić komunikat o wygranej lub przegranej i zrestartrować program.
- [check_button_clicked](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L110-L112):
  Metoda służąca do wywoływania, na *ControllerGame*, metody sprawdzającej kod, wprowadzony przez użytkownika.
- [reset](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L114-L121):
  Metoda restartuje grę
- [show_error](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L123-L127):
  Metoda wyświetla ostrzeżenie dotyczące nieprawidłowego kodu
- [__hide_error](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L129-L135):
  Metoda chowa ostrzeżenie
- [metody po kliknięciu przycisku oszust](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L137-L143):
  Metody wyświetlają komunikat *Tere fere* albo *Złapałeś/aś mnie*

### Moduł [lang_pl](https://github.com/ichal6/Mastermind/blob/master/src/Views/lang_pl.py)

Przechowuje słownik z napisami wykorzystywanymi do popup-ów.

### Klasa [DataValidation](https://github.com/ichal6/Mastermind/blob/master/src/Validations/DataValidation.py)

Klasa służąca do walidacji danych od użytkownika.

Zawiera jedną
metodę: [validate_secret_code_dict](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Validations/DataValidation.py#L9-L29):
Metoda zwraca własny wyjątek *IncorrectSecretCodeError* jeśli kod, przekazany jako wartość słownikowa, jest
nieprawidłowy.

### Klasa [GameService](https://github.com/ichal6/Mastermind/blob/master/src/Services/GameService.py)

Jest to klasa pomocnicza do klasy *GameController*.

Metody:

- [build_secret_code](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Services/GameService.py#L32-L57):
  Metoda pobiera kod jako string i próbuje stworzyć obiekt klasy SecretCode. Jeśli operacja się powiedzie metoda zwraca
  stworzoną instancję. Jesli nie zwracany jest *IncorrectSecretCodeError* z komunikatem o błędzie.
- [build_game_rule](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Services/GameService.py#L59-L72):
  Metoda tworzy nową grę z losowo wybranymi zasadami.

### Klasa [RuleGame](https://github.com/ichal6/Mastermind/blob/master/src/Models/RuleGame.py)

Klasa abstrakcyjna z regułami gry.

Metody:

- [__
  init__](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/RuleGame.py#L6-L9):
  Metoda ustawia pobrany jako parmetr obiekt **SecretCode**, maksymalną liczbę podejść na 12 oraz zeruje licznik
  podejść.
- [increase_attempt_number](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/RuleGame.py#L30-L31):
  Zwiększa licznik podejść o 1
- [get_code_value](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/RuleGame.py#L36-L37):
  Zwraca reprezentację stringową obiektu SecretCode

Metody abstrakcyjnę zostaną omówione przy **FairGame**

### Klasa [FairGame](https://github.com/ichal6/Mastermind/blob/master/src/Models/FairGame.py)

Odpowiada za przeprowadzanie gry według zasad

Metody:

- [check](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/FairGame.py#L9-L11):
  Za pomoca metody *equal_code* z *SecretCode* sprawdza czy kod wprowadzony przez użytkownika jest tożsamy z kodem
  wylosowanym. Zwiększa licznik. Zwraca wartość *bool*
- [get_count_correct_position](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/FairGame.py#L13-L14):
  Zwraca liczby na poprawnych pozycjach
- [get_count_incorrect_position](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/FairGame.py#L16-L17):
  Zwraca liczby na niepoprawnych pozycjach

### Klasa [CheatGame](https://github.com/ichal6/Mastermind/blob/master/src/Models/CheatGame.py)

Odpowiada za przeprowadzanie oszukańczej rozgrywki

Metody:

- [check](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/CheatGame.py#L27-L29):
  Zwiększa licznik. Zwraca wartość *False*
- [get_count_correct_position](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/CheatGame.py#L31-L33):
  Zwraca liczby na poprawnych pozycjach na podstawie generatora
- [get_count_incorrect_position](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/CheatGame.py#L35-L37):
  Zwraca liczby na niepoprawnych pozycjach na podstawie generatora
- [__
  init__](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/CheatGame.py#L6-L25):
  Z użyciem generatorów i list comprehension inicjalizuje nieuczciwą grę

### Klasa [SecretCode](https://github.com/ichal6/Mastermind/blob/master/src/Models/SecretCode.py)

Odpowiada za tworzenie obiektu przechowującego sekretny kod.

Metody:

- [__
  init__](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/SecretCode.py#L7-L13):
  Jako parametr przesłany jest słownik z wartościami kodu. Jeśli słownik nie zostanie przekazany, wtedy za pomocą
  dictionary comprehension tworzy nowy słownik z polami na kod oraz wypełnia go losowymi wartościami. Przekazany słownik
  podlega walidacji.
- [count_correct_position](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/SecretCode.py#L31-L36):
  Porównuje przesłany obiekt SecretCode z przechowywanym słownikiem i zwraca ilość cyfr na tych samych pozycjach
- [count_incorrect_position](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/SecretCode.py#L38-L52):
  Porównuje aktualną instancję z przesłaną oraz zwraca ilość cyfr na niepoprawnych pozycjach.

### Klasa [IncorrectSecretCodeError](https://github.com/ichal6/Mastermind/blob/master/src/Exceptions/IncorrectSecretCodeError.py)

Własna klasa wyjątku służąca do walidacji danych.

### Klasa [ControllerGame](https://github.com/ichal6/Mastermind/blob/master/src/Controllers/ControllerGame.py)

Klasa odpowiadająca za sterowanie logiką gry.

Metody:

- [check](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Controllers/ControllerGame.py#L14-L23):
  Metoda pobiera kod od *View* i sprawdza warunek zwycięstwa. Jeśli gracz wygrał, za pomoca *View* wyświetla informację
  o wygranej. Jesli nie sprawdza czy ilość prób nie została przekroczona. Jeśli nie została wywołuje answer z *View*.
  Jesli została, wywołuje komunikat game over z *View*.
- [check_from_string](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Controllers/ControllerGame.py#L25-L37):
  Metoda pobiera kod jako string, za pomoca *GameService* buduje obiekt *SecretCode*. Jesli kod był błędny, wtedy za
  pomoca *View* wyświetla komunikat o błędnym kodzie. Jeśli był poprawny wywołuje *check* na *SecretCode*
- [is_cheater](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Controllers/ControllerGame.py#L39-L40):
  Sprawdza czy gra toczy się według nieuczciwych zasad. Zwraca *bool*
- [display_code](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Controllers/ControllerGame.py#L42-L43):
  Wywołuje metodę konwerującą *SecretCode* na *str*
- [reset](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Controllers/ControllerGame.py#L45-L46):
  Wywołuje metodę budującą nowy obiekt gry z *GameService* i przypisuje ją do zmeinnej prywatnej *game*

## [Testy](https://github.com/ichal6/Mastermind/blob/master/tests/testMain.py)

Wykorzystuje bibliotekę do testów: **unittest** oraz implementację **ConsoleView** klasy abstrakcyjnej *View* do
wyświetlania informacji.

### [test_1](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L13-L33)

Wyświetlenie (wypisanie w konsoli) wylosowanego kodu, wpisanie odpowiedzi z błędnymi cyframi - oczekiwana informacja o
braku poprawnych trafień.

### [test_2](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L35-L53)

Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z poprawnymi cyframi w złych miejscach - oczekiwana informacja o
niepoprawnym położeniu.

### [test_3](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L55-L74)

Wyświetlenie wylosowanego kodu, wpisanie odpowiedzi z dwoma poprawnymi cyframi w dobrych miejscach i dwoma poprawnymi w
złych miejscach - oczekiwana informacja o dwóch trafieniach i dwóch złych pozycjach.

### [test_4](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L76-L98)

Wyświetlenie wylosowanego kodu, wpisanie poprawnej odpowiedzi - oczekiwana informacja o wygranej.

### [test_5](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L100-L120)

Wpisanie 12 razy niepoprawnego kodu - oczekiwana informacja o przegranej

### [test_6](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L122-L140)

Próba wpisania niepoprawnego kodu do pola odpowiedzi (mniej lub więcej niż 4 znaki, znaki nie będące cyframi od 1 do 6)
- oczekiwane nieuznanie kodu (gracz nie traci tury).

### [test_7](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L142-L154)

Wciśnięcie przycisku „Oszust” przy poprawnych zasadach gry - oczekiwana informacja „tere fere”.

### [test_8](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L156-L168)

Wciśnięcie przycisku „Oszust” przy niepoprawnych zasadach gry - oczekiwana informacja o oszukiwaniu przez komputer.

### [test_9](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L170-L188)

Wpisanie 10 kodów, resetowanie gry, wpisanie 5 kodów - oczekiwane normalne działanie gry (czy licznik tur resetuje się
po wciśnięciu „Reset”).

### [test_10](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/testMain.py#L190-L207)

Rozegranie próbnej gry w 6 próbach. Porównanie stosownej listy nieprawidłowych pozycji do uzyskanej z programu.

### [Test GameRule](https://github.com/ichal6/Mastermind/blob/master/tests/ModelsTest/testGameRule.py):

Próba zwiększenia licznika podejść. Oczekiwany rezultat 1 próba.

### [Testy FairGame](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/tests/ModelsTest/testFairGame.py#L18):

Zaimplementowano trzy testy jednostkowe, sprawdzające poprawność działania klasy.

### [Testy SecretCode](https://github.com/ichal6/Mastermind/blob/master/tests/ModelsTest/testSecretCode.py):

Zaimplementowano siedem testów jednostkowych, sprawdzające poprawność działania klasy.

### [CommonUse](https://github.com/ichal6/Mastermind/blob/master/tests/CommonUse.py):

Moduł użyta jako klasa pomocnicza dla testów.

## Wymagane Elementy języka Python:

### Wyrażenia Lambda:

- [TkInterView](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L42-L53):
  Wyrażenia lambda zostały uzyte to obsługi klawiszy w klasie odpowiedzialnej za interfejs.

### List comprehensions lub dictionary comprehensions:

- [SecretCode](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/SecretCode.py#L10):
  Wykorzystane do budowy słownika z wylosowanym kodem
- [SecretCode](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/SecretCode.py#L8):
  Wykorzystane do budowy kluczy do słownika
- [GameService](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Services/GameService.py#L51-L52):
  Użyte do budowy klucza oraz słownika
- [CheatGame](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/CheatGame.py#L20-L22):
  Wykorzystane przy inicjalizacji generatorów

### Generatory:

- [CheatGame](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Models/CheatGame.py#L24-L25):
  Wykorzystane do generowania błędnych informacji dla użytkownika

### Dekoratory:

- [RuleGaame](https://github.com/ichal6/Mastermind/blob/master/src/Models/RuleGame.py):
  Wykorzystano *@property* oraz *@abstractmethod*
- [SecretCode](https://github.com/ichal6/Mastermind/blob/master/src/Models/SecretCode.py):
  Wykorzystano *@property*
- [GameService](https://github.com/ichal6/Mastermind/blob/master/src/Services/GameService.py):
  Wykorzystano *@staticmethod*
- [DataValidation](https://github.com/ichal6/Mastermind/blob/master/src/Validations/DataValidation.py):
  Wykorzystano *@staticmethod*
- [View](https://github.com/ichal6/Mastermind/blob/master/src/Views/View.py):
  Użyto *property*, *@abstractmethod* oraz *@staticmethod*
- [TkInterView](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/TkInterView.py#L137-L143):
  Zastosowano *@staticmethod*
- [ConsoleView](https://github.com/ichal6/Mastermind/blob/f3999ff2a0b260b680decd2e479428876c21ee84/src/Views/ConsoleView.py#L32-L38):
  Zastosowano *@staticmethod*
