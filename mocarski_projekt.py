import pandas as pd
import tkinter as tk
import random

def wynik():
    global odp
    odp=0
    global pjkj
    pjkj+=1

def drugiwynik():
    global odp
    odp=1
    global pjkj
    pjkj+=1

def reset():
    global xd
    xd=1
    #global a                    #odkomentowanie linii 20-23, 29 i 37-38 spowoduje zmiane z kolejnych tweetow na losowe, ale bedzie trzeba jszcze okomentowac za to92-94,59,8,9,14,15
    #a = random.randint(0, 2201)
    #while ((mydata["odpowiedz"][a]==1) or (mydata["odpowiedz"][a]==0)):
    #    a=random.randint(0,2201)

sciezka=input("Podaj sciezke z nazwa pliku ktory zawiera slownik z tweetami w rozszerzeniu csv:\n")

try:
    mydata = pd.read_csv(sciezka) #all-tweets.csv jest zbiorem testowym, wraz z ucietymi niektorymi fragmentami tresci tweeta, dlatego moga pojawiac sie wielokropki wyciete z kontekstu
    #a = random.randint(0,2201)  #Tutaj jest wpisywany zakres ilosci tweetow. Trzeba recznie zmieniac jezeli baza tweetow sie zmieni
    try:
        #print(mydata["odpowiedz"][a])
        a=mydata["sprtweety"][0]
        print(a)
    except:
        mydata["sprtweety"]=0
        mydata["odpowiedz"]=2
    #while ((mydata["odpowiedz"][a]==1) or (mydata["odpowiedz"][a]==0)):
        #a=random.randint(0,2201)

#    print(a)
#    print(mydata["text"][a])
#    print(mydata["created_at"][a])
#    print(mydata["author_id"][a])
#    print(mydata["public_metrics.retweet_count"][a])
#    print(mydata["public_metrics.reply_count"][a])
#    print(mydata["public_metrics.like_count"][a])
#    print(mydata["public_metrics.quote_count"][a])
#jezeli usunie sie okomentowanie powyzszego bloba tuż nad tym komentarzem to bedzie mozna sprawdzic poprawnosc danych wyswietlanych w GUI

except:
    print("Bledna sciezka lub nazwa pliku\n")
    exit()

xd=1
odp=2      #niezbedna deklaracja, bo zawsze raz program przypisuje wartosc zmiennej odp, przy czym uzytkownik moze nie podac odpowiedzi

while(xd==1):
    xd=0
    pjkj=0
    a = mydata["sprtweety"][0]
    window = tk.Tk()
    window.title("Pomóż ocenzurować internet") #tytuł nagłówka
    window.resizable(width=True, height=False)  #te falsy blokują możliwość zmiany szerokości i wysokości otwierającego się okna

    druk="Tweet o numerze: "+str(a+1)+"\no tresci:\n"
    if len(mydata["text"][a]) <= 60:
        druk=druk+mydata["text"][a]
    elif (len(mydata["text"][a]) <= 120) & (len(mydata["text"][a])>60):
        druk=druk+mydata["text"][a][:60]+"\n"+mydata["text"][a][60:]
    elif (len(mydata["text"][a]) <= 180) & (len(mydata["text"][a])>120):
        druk=druk + mydata["text"][a][:60] + "\n" + mydata["text"][a][60:120]+"\n"+mydata["text"][a][120:]
    elif (len(mydata["text"][a]) <= 240) & (len(mydata["text"][a])>180):
        druk = druk + mydata["text"][a][:60] + "\n" + mydata["text"][a][60:120] + "\n" + mydata["text"][a][120:180]+"\n"+mydata["text"][a][180:]
    elif (len(mydata["text"][a]) <= 300) & (len(mydata["text"][a])>240):
        druk = druk + mydata["text"][a][:60] + "\n" + mydata["text"][a][60:120] + "\n" + mydata["text"][a][120:180] + "\n" + mydata["text"][a][180:240]+"\n"+mydata["text"][a][240:]
    druk+="\nstworzony:\n"+str(mydata["created_at"][a])+"\nRetweetowali to: "+str(mydata["public_metrics.retweet_count"][a])+" razy\nOdpowiedzialo: "+str(mydata["public_metrics.reply_count"][a])+" osob\nPolubilo to: "+str(mydata["public_metrics.like_count"][a])+" osob\nCytowalo tego tweeta: "+str(mydata["public_metrics.quote_count"][a])+" osob\nId autora: "+str(mydata["author_id"][a])+"\nCzy jest to mowa nienawisci/ofensywny jezyk?"

    GUI = tk.Label(text=druk, foreground="white", background="black")
    GUI.pack(fill=tk.X)

    tak = tk.Button(window,text='Tak', foreground="white", background="black",command=drugiwynik)
    tak.pack(fill=tk.X)
    nie = tk.Button(window,text='Nie', foreground="white", background="black",command=wynik)
    nie.pack(fill=tk.X)
    lecim=tk.Button(window,text='Kolejny tweet', foreground="white",background="black",command=reset)
    lecim.pack(fill=tk.X)

    window.mainloop()

    mydata["odpowiedz"][a]=odp
    if(pjkj>0):
        pjkj=0
        mydata["sprtweety"][0]+=1
    mydata.to_csv(sciezka)
#    odkomentowanie ponizszej linii sprawdza wpisywana tresc do pliku csv
#    print(mydata["odpowiedz"][a])