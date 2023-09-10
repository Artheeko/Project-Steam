import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import json
import requests
from urllib.request import urlopen

# dient voor de user status voor TI
x = False


# Dashboard(functie 2)
def func2():
    # window settings
    window = Tk()
    window.geometry("1000x900")
    window.title("Steam Dashboard")
    window.configure(background="#1b2838")

    # Steam-logo
    # we openen het bestand
    steam_logo = Image.open("steam-logo-black-transparent.png")
    # we resizen het logo
    resize = steam_logo.resize((75, 75), Image.ANTIALIAS)
    resized_steam_logo = ImageTk.PhotoImage(resize)
    # we zetten het logo als widget
    label1 = Label(image=resized_steam_logo, width=75, height=75, bg="#1b2838", fg="white")
    label1.place(x=3, y=3)

    # Dashboard Header
    header = Label(window, text="Dashboard", font=('Arial', 30), bg="#1b2838", fg="white")
    header.place(x=380, y=7)

    def func1():
        json_bestand = open("../steam.json", "r")
        data = json.load(json_bestand)
        # we zetten de data in een lijst
        data_lst = []
        for i in data:
            data_lst.append(i)
        return data

        # Naam van eerste spel weergeven(functie 3)

    def func3():
        spel_namen = []
        for i in func1():
            spel_namen.append(i['name'])
        # Eerste spelnaam
        eerste_spelnaam = spel_namen[0]
        naam_label = Label(window, text="spel 1: {}".format(eerste_spelnaam), font=('Arial', 17), bg="#1b2838",
                           fg="white")
        naam_label.place(x=367, y=65)

    # Elk soort data van het JSON-bestand gesorteerd weergeven returnen(functie 4)
    def func4():
        data = []
        # Hier returnen we bijvoorbeeld alle gamenamen gesorteerd
        for i in func1():
            data.append(i['naam'])
        sorted_lst = sorted(data)
        return sorted_lst

    func3()
    # Persoonlijk scherm met data uit Steam API
    # user input steam-ID
    header2 = Label(window, text="Steam-ID:", font=('Arial', 16), bg="#1b2838", fg="white", )
    header2.place(x=270, y=103)
    # input veld voor de gebruiker
    input_field_ID = Entry(window, width=25, borderwidth=5)
    input_field_ID.place(x=370, y=103)

    # met deze functie checken we of de gebruiker een geldig steam-ID invoert
    def check():
        # we converten de user input naar een string
        int_steam_id = int(input_field_ID.get())
        # we halen user data uit de steam API
        response1 = requests.get(
            "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=D5CD00FABF80551EE4549D881CFA8A4A&steamids={}".format(
                int_steam_id))
        player_data = response1.json()
        # We zetten de steam data in de lijst
        player_data_lst = []
        for i in player_data['response']['players']:
            player_data_lst.append(i)

        # User scherm bij geldige input
        def user_display():
            # frame lengte en breedte
            user_display_frame = LabelFrame(window, width=850, height=475, bg="#1b2838")
            # deze lijn heb ik van https://stackoverflow.com/questions/39580739/python-tkinter-label-in-frame
            user_display_frame.pack_propagate(False)
            # we geven het frame een positie
            user_display_frame.place(x=85, y=140)
            # header
            display_header = Label(user_display_frame,
                                   text="Welkom terug, {}".format(player_data_lst[0]['personaname']),
                                   font=('Arial', 20), bg="#1b2838", fg="white")
            display_header.place(x=200, y=7)

            # functie die images uit de steam api netjes weergeeft
            def steam_img(frame, url, x, y):
                image_url = url
                u = urlopen(image_url)
                raw_data = u.read()
                u.close()
                photo = ImageTk.PhotoImage(data=raw_data)
                label = tk.Label(frame, image=photo)
                label.image = photo
                label.place(x=x, y=y)

            # user avatar
            steam_img(user_display_frame, player_data_lst[0]['avatarmedium'],
                      0, 0)

            # user status
            def online_status(status):
                global x
                if status == 0:
                    offline = Label(user_display_frame, text="Offline", font=('Arial', 10), bg="#1b2838", fg="red")
                    offline.place(x=75, y=7)
                    x = False
                else:
                    online = Label(user_display_frame, text="Online", font=('Arial', 10), bg="#1b2838", fg="green")
                    online.place(x=75, y=7)
                    x = True
            online_status(player_data_lst[0]['personastate'])
            print(x)

            # top 5 recent gespeelde games weergeven op dashboard

            # frame voor de games
            recent_games_frame = LabelFrame(user_display_frame, width=450, height=180, bg="#1b2838")
            # deze lijn heb ik van https://stackoverflow.com/questions/39580739/python-tkinter-label-in-frame
            recent_games_frame.pack_propagate(False)
            # we geven het frame een positie
            recent_games_frame.place(x=175, y=50)

            # we halen de data uit de api
            response2 = requests.get(
                "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=D5CD00FABF80551EE4549D881CFA8A4A&steamid={}".format(
                    int_steam_id))
            games_data = response2.json()
            # we zetten alle nuttige steam data in een lijst
            recent_game_data_lst = []
            for i in games_data['response']['games']:
                recent_game_data_lst.append(i)

            # app id's
            five_appid = []
            for i in range(5):
                five_appid.append(recent_game_data_lst[i]['appid'])
            # logo's
            five_logos = []
            for i in range(5):
                five_logos.append(recent_game_data_lst[i]['img_icon_url'])
            # logo's als geldige link
            logos_link = []
            for i in range(5):
                logos_link.append(
                    "http://media.steampowered.com/steamcommunity/public/images/apps/{}/{}.jpg".format(five_appid[i],
                                                                                                       five_logos[i]))

            # json bestand
            json_bestand = open("../steam.json", "r")
            json_data = json.load(json_bestand)
            json_data_lst = []
            for i in json_data:
                json_data_lst.append(i)

            recent_game_names = []
            recent_game_logos = []
            for i in five_appid:
                for j in range(len(json_data_lst)):
                    if json_data_lst[j]['appid'] == i:
                        recent_game_names.append(json_data_lst[j]['name'])
                        recent_game_logos.append(
                            "http://media.steampowered.com/steamcommunity/public/images/apps/{}/{}.jpg".format(i,
                                                                                                               five_logos[
                                                                                                                   five_appid.index(
                                                                                                                       i)]))

            # de data displayen op dashboard
            # namen
            y_naam = 10
            for i in recent_game_names:
                name_label = Label(recent_games_frame, text=i, font=('Arial', 10), bg="#1b2838", fg="white")
                name_label.place(x=120, y=y_naam)
                y_naam += 40
            # logos
            y_logo = 10
            for i in recent_game_logos:
                steam_img(recent_games_frame, i, 315, y_logo)
                y_logo += 40

            # Aanvullend onderdeel 11(sorteren)
            # Met deze functionaliteit kan de gebruiker de top 5 best beoordeelde games zien
            # Header
            header2 = Label(user_display_frame, text="Top 5 best rated games", font=('Arial', 16), bg="#1b2838",
                            fg="white", )
            header2.place(y=240, x=160)

            # sorteeralgoritme(selection sort)
            def sort(lst):
                for i in range(0, len(lst) - 1):
                    min_index = i
                    for j in range(i + 1, len(lst)):
                        if lst[j] > lst[min_index]:
                            min_index = j
                    lst[i], lst[min_index] = lst[min_index], lst[i]
                return lst

            # Dit krijgt de gebruiker te zien wanneer hij op de knop drukt
            def best_rated_games():
                # dit zorgt ervoor dat je maar één keer kan klikken op de knop
                button1.configure(state=DISABLED)
                # frame lengte en breedte
                best_rated_games_frame = LabelFrame(user_display_frame, width=275, height=150, bg="#1b2838")
                # deze lijn heb ik van https://stackoverflow.com/questions/39580739/python-tkinter-label-in-frame
                best_rated_games_frame.pack_propagate(False)
                # we geven het frame een positie
                best_rated_games_frame.place(x=150, y=310)
                # we slaan alle games met hun rating op in een lijst
                games_lst = []
                for i in func1():
                    games_lst.append((i['positive_ratings'], i['name']))
                # We sorteren alle games met het sorteeralgoritme
                sorted_games_lst = sort(games_lst)
                # we laten de games zien op het dashboard
                for i in range(5):
                    label3 = Label(best_rated_games_frame, text="#{} {}".format(i + 1, sorted_games_lst[i][1]),
                                   font=('Arial', 10),
                                   bg="#1b2838", fg="white", )
                    label3.pack()

            func3()
            # De top 5 best rated games worden weergegeven als de gebruiker op de knop drukt
            button1 = Button(user_display_frame, text="toon top 5 best rated games", font=('Arial', 9), bg="#1b2838",
                             fg="white",
                             command=best_rated_games)
            button1.place(y=275, x=200)

            # Aanvullend onderdeel 12(zoeken)
            # deze functionaliteit laat de gebruiker zoeken naar games op basis van leeftijd
            # Header
            header3 = Label(user_display_frame, text="Zoek games op age rating", font=('Arial', 16), bg="#1b2838",
                            fg="white", )
            header3.place(y=240, x=400)
            # input veld voor de gebruiker
            input_field_age = Entry(user_display_frame, width=25, borderwidth=5)
            input_field_age.place(y=275, x=400)

            # Dit krijgt de gebruiker te zien wanneer hij op de knop drukt
            def age_games():
                # frame
                age_games_frame = LabelFrame(user_display_frame, width=350, height=125, bg="#1b2838")
                # deze lijn heb ik van https://stackoverflow.com/questions/39580739/python-tkinter-label-in-frame
                age_games_frame.pack_propagate(False)
                age_games_frame.place(x=300, y=310)
                # we slaan de input van de gebruiker op in een variable
                input_age = int(input_field_age.get())

                # Aanvullend onderdeel AI 13. We maken gebruik van dit algoritme als we de leeftijden gaan sorteren
                def merge_sort(lst):
                    if len(lst) > 1:
                        linker_lst = lst[:len(lst) // 2]
                        rechter_lst = lst[len(lst) // 2:]
                        merge_sort(linker_lst)
                        merge_sort(rechter_lst)
                        l = 0
                        r = 0
                        t = 0
                        while l < len(linker_lst) and r < len(rechter_lst):
                            if linker_lst[l] < rechter_lst[r]:
                                lst[t] = linker_lst[l]
                                l += 1
                            else:
                                lst[t] = rechter_lst[r]
                                r += 1
                            t += 1

                        while l < len(linker_lst):
                            lst[t] = linker_lst[l]
                            l += 1
                            t += 1
                        while r < len(rechter_lst):
                            lst[t] = rechter_lst[r]
                            r += 1
                            t += 1
                        return lst

                # we maken een lijst met alle gamenamen en leeftijd
                games_lst = []
                for i in func1():
                    games_lst.append((i['required_age'], i['name']))
                # we maken lijst met alle mogelijke game-leeftijden
                age_ratings = []
                for i in func1():
                    age_ratings.append(i['required_age'])
                # we filteren de lijst van duplicaten en sorteren de lijst met het sorteeralgoritme
                age_ratings = list(dict.fromkeys(age_ratings))
                age_ratings = merge_sort(age_ratings)
                '''' als de gebruiker een leeftijd invoert wordt met behulp van het binaire algoritme
                gezocht naar de eerste vijf games van die leeftijdscategorie. Deze worden dn getoond
                op het dashboard'''

                def binair_search(age_lst, lijst, target):
                    low = 0
                    high = len(age_lst)
                    age_game_lst = []
                    while low <= high:
                        mid = (low + high) // 2
                        if age_lst[mid] == target:
                            for j in lijst:
                                if j[0] == target:
                                    age_game_lst.append(j)
                            for k in range(5):
                                label4 = Label(age_games_frame, text="{}".format(age_game_lst[k][1]),
                                               font=('Arial', 10),
                                               bg="#1b2838", fg="white", )
                                label4.pack()
                            break
                        elif target > age_lst[mid]:
                            low = mid + 1
                        else:
                            high = mid - 1
                    return False

                binair_search(age_ratings, games_lst, input_age)

            # als de gebruiker drukt op de knop draait de code in age_games()
            button2 = Button(user_display_frame, text="zoek", font=('Arial', 9), bg="#1b2838",
                             fg="white",
                             command=age_games)
            button2.place(y=275, x=570)

            # vriendenlijst
            # top 5 recent gespeelde games
            friends_frame = LabelFrame(user_display_frame, width=191, height=300, bg="#1b2838")
            # deze lijn heb ik van https://stackoverflow.com/questions/39580739/python-tkinter-label-in-frame
            friends_frame.pack_propagate(False)
            # we geven het frame een positie
            friends_frame.place(x=655, y=0)
            # Header
            header4 = Label(friends_frame, text="Vriendenlijst", font=('Arial', 16), bg="#1b2838", fg="white")
            header4.place(x=27, y=5)
            # we halen de data uit de api
            # friendlist
            friends = requests.get(
                "http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=D5CD00FABF80551EE4549D881CFA8A4A&steamid={}&relationship=friend".format(
                    int_steam_id))
            data = friends.json()
            # friends in lst
            friends_lst = []
            for i in range(5):
                friends_lst.append(data['friendslist']['friends'][i]['steamid'])
            # convert steamid naar naam met bijbehorende avatar
            namen = []
            avatars = []
            status = []
            for i in friends_lst:
                player_data = requests.get(
                    "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=D5CD00FABF80551EE4549D881CFA8A4A&steamids={}".format(
                        i))
                player_data_json = player_data.json()
                namen.append(player_data_json['response']['players'][0]['personaname'])
                avatars.append(player_data_json['response']['players'][0]['avatar'])
                # online status
                if player_data_json['response']['players'][0]['personastate'] == 0:
                    status.append("offline")
                else:
                    status.append('online')

            # first recent played for each friend
            recent_played_game = []
            for i in friends_lst:
                data_friend = requests.get(
                    "http://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v0001/?key=D5CD00FABF80551EE4549D881CFA8A4A&steamid={}&format=json".format(
                        i))
                data_friend_json = data_friend.json()
                if len(data_friend_json['response']) < 2:
                    recent_played_game.append("no recent game")
                else:
                    recent_played_game.append(data_friend_json['response']['games'][0]['name'])
            # we displayen alle data op het dashboard
            # avatars
            y_avatar = 40
            for i in avatars:
                steam_img(friends_frame, i, 17, y_avatar)
                y_avatar += 50

            # namen
            y_name = 40
            for i in namen:
                naam_label = Label(friends_frame, text=i, font=('Arial', 9), bg="#1b2838", fg="white")
                naam_label.place(x=57, y=y_name)
                y_name += 50
            # recent bespeelde game
            y_recent = 55
            for i in recent_played_game:
                naam_label = Label(friends_frame, text=i, font=('Arial', 7), bg="#1b2838", fg="white")
                naam_label.place(x=57, y=y_recent)
                y_recent += 50
            y_status = 67
            # online status
            for i in status:
                if i == 'online':
                    online_label = Label(friends_frame, text=i, font=('Arial', 7), bg="#1b2838", fg="green")
                    online_label.place(x=57, y=y_status)
                    y_status += 50
                else:
                    offline_label = Label(friends_frame, text=i, font=('Arial', 7), bg="#1b2838", fg="red")
                    offline_label.place(x=57, y=y_status)
                    y_status += 50

                # User scherm bij ongeldige input

        def user_display_error():
            # frame lengte en breedte
            user_display_frame = LabelFrame(window, width=825, height=375, bg="#1b2838")
            # deze lijn heb ik van https://stackoverflow.com/questions/39580739/python-tkinter-label-in-frame
            user_display_frame.pack_propagate(False)
            # we geven het frame een positie
            user_display_frame.place(x=85, y=140)
            error_label = Label(user_display_frame, text="Ongeldig Steam-ID", font=('Arial', 16), bg="#1b2838",
                                fg="white", )
            error_label.pack()

        # afhankelijk van de geldigheid van ht steam-ID wordt een user scherm getoond.
        if len(player_data_lst) == 0:
            button1 = Button(window, text="user_display", font=('Arial', 12), bg="#1b2838", fg="white",
                             command=user_display_error)
            button1.place(x=625, y=103)
        else:
            button1 = Button(window, text="user_display", font=('Arial', 12), bg="#1b2838", fg="white",
                             command=user_display)
            button1.place(x=625, y=103)

    # input steam-ID wordt bevestigd
    button1 = Button(window, text="bevestig", font=('Arial', 12), bg="#1b2838", fg="white",
                     command=check)
    button1.place(x=550, y=103)

    window.mainloop()


func2()
