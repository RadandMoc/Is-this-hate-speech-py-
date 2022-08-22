# Is-this-hate-speech-py-
A small application that loads a csv file. It asks for feedback in a window and allows you to evaluate it.

In Polish:

Do uruchomienia programu potrzeba mieć zainstalowaną bibliotekę Pandas

Program po uruchomieniu z konsoli, zarząda wpisania ścieżki do pliku csv z tweetami wraz z pełną nazwą pliku (z tym .csv).
Wyskoczy okno z trzema przyciskami.
Należy przeczytać treść tweeta, po czym ocenić czy jest on mową nienawiści/zawiera ofensywny język

Jeżeli tak:
-To należy nacisnąć przycisk Tak

Jeżeli nie:
-To należy nacisnąć przycisk Nie

Uwaga: Ocena wpisana do pliku jest uzależniona od ostatniego kliknięcia w przycisk Tak/Nie

Opcja dodatkowa: (kolejny tweet)
-Jeżeli chcesz załadować kolejne tweety bez konieczności ponownego uruchamiania programu i wpisywania ścieżki,
to można nacisnąć przycisk "kolejny tweet". Jest on niezależny względem dwóch pozostałych i po jednym naciśnięciu tego przycisku,
kiedy zamknie się okno, to wyskoczy kolejne z kolejnym tweetem.

Funkcje ukryte:
Plik csv nie musi mieć kolumny z odpowiedziami. Program ten jest w stanie samemu taką kolumnę stworzyć.
Tweety wybierane są po kolei od plku zerowego, jednak użytkownik jest informowany że to jest tweet o 1 większy.
Liczbę zopiniowanych tweetów zapisuje się w kolumnie "sprtweety" słownika, w pierwszym wierszu. Umożliwia to kontynuację pracy po zamkięciu programu lub zmianie urządzenia bez zbędnych obliczeń\sprawdzań.
Jeżeli chcesz zmienić styl wyświetlania tweetów na losowy, to trzeba w pliku usunąć i dodać komentarze napisane w 20 linii kodu.
Jeżeli użytkownik wpisze nieprawidłową ścieżkę do pliku, to program o tym poinformuje i się wyłączy.
Stworzyłem motyw ciemny, oraz zablokowałem możliwość rozszerzania GUI w pionie.


In English:

You need to have the Pandas library installed to run the program

After starting the program from the console, it asks you to enter the path to the csv file with tweets along with the full name of the file (including .csv).
A window with three buttons will pop up.
Read the tweet and assess whether it is hate speech / offensive language

If so:
-Then press the "Tak" button

Unless:
-Then press the "Nie" button

Note: The rating entered in the file depends on the last click on the "Tak" / "Nie" button

Additional option: (another tweet)
-If you want to load more tweets without having to restart the program and enter the path,
then you can press the button "Kolejny tweet". It is independent of the other two and after one press of this button,
when the window closes, another one will pop up with another tweet.

Hidden functions:
The csv file does not need to have an answer column. This program is able to create such a column by itself.
Tweets are selected one by one from the null file, but the user is informed that it is a tweet 1 larger.
The number of reviewed tweets is entered in the "sprtweets" column of the dictionary, in the first line. This allows you to continue work after closing the program or changing the device without unnecessary calculations \ checks.
If you want to change the display style of tweets to random, you need to delete and add comments written in 20 lines of code in the file.
If the user enters an incorrect path to the file, the program will inform about it and shut down.
I created a dark theme and blocked the possibility of extending the GUI vertically.
