import requests
import tkinter
from tkinter import messagebox
import webbrowser

def callback(url):
   webbrowser.open_new_tab(url)

def start_history():
    if(value_inside.get() == "Select Account Region"):
        messagebox.showerror("Error", "Please select region")
    elif(ent_username.get() == ""):
        messagebox.showerror("Error", "Please enter your laegue of legends username")
    else:
        api_key = str(ent_apikey.get())
        api_accinfo = "https://" + value_inside.get().lower() + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"
        api_getmatches = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/"
        api_getmatchesdetails = "https://europe.api.riotgames.com/lol/match/v5/matches/"

        entery_user = ent_username.get()
        matchcount = 0
        mathcount_end = 10

        with open("api_key.txt", "w") as f:
            f.write(ent_apikey.get())
            f.close()
        def accinfo():
            username = entery_user.replace(" ", "%20")
            rqlink = api_accinfo + username + "?api_key=" + api_key
            rq = requests.get(rqlink)
            return rq.json()

        getaccinfo = accinfo()

        while mathcount_end > matchcount:

            def matches():
                puuid = getaccinfo["puuid"]
                rqlink = api_getmatches + puuid + "/ids?api_key=" + api_key
                rq = requests.get(rqlink)
                getmatches = rq.json()
                getmatches_link = api_getmatchesdetails + getmatches[matchcount] + "?api_key=" + api_key
                getmatches_rq = requests.get(getmatches_link)
                return getmatches_rq.json()

            getmatches = matches()
            userpuuid = getaccinfo["puuid"]

            champlist = getmatches["info"]['participants']
            counter = 0

            for x in champlist:
                if(getmatches["info"]['participants'][counter]["puuid"] == userpuuid):
                    break
                else:
                    counter += 1
            def matchhistory():
                kills = getmatches["info"]['participants'][counter]['kills']
                deaths = getmatches["info"]['participants'][counter]['deaths']
                assists = getmatches["info"]['participants'][counter]['assists']
                champselect = getmatches["info"]['participants'][counter]['championName']
                win = getmatches["info"]['participants'][counter]["win"]
                return ls1.insert("end", f"Champion: {champselect}, Kill: {kills}, Death: {deaths}, Assists: {assists}, Win: {assists}")

            matchhistory()
            matchcount += 1

def read_api():
    try:
        with open("api_key.txt" , "r") as f:
            read_api = f.read()
            f.close()
            return  read_api
    except FileNotFoundError:
        pass

get_read_api = read_api()

#WINDOW

window = tkinter.Tk()
window.configure(background='orange')
window.title = "safasfa"

window_height = 450
window_width = 430

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

options_list = ["BR1", "EUN1", "EUW1", "JP1", "KR", "LA1", "LA2", "NA1", "OC1", "PH2", "RU", "SG2", "TH2", "TR1", "TW2", "VN2"]

link = tkinter.Label(window, text="https://developer.riotgames.com/",font=('Helveticabold', 10), fg="blue", cursor="hand2")
link.pack(padx=10, pady=10)
link.bind("<Button-1>", lambda e:
callback("https://developer.riotgames.com/"))

lb1 = tkinter.Label(text="Enter your DEVELOPMENT API KEY:")
lb1.pack(padx=5, pady=5)

ent_apikey = tkinter.Entry(width=43)
ent_apikey.insert(tkinter.END, str(get_read_api))
ent_apikey.pack(padx=5, pady=5)


value_inside = tkinter.StringVar(window)

value_inside.set("Select Account Region")

opt1 = tkinter.OptionMenu(window, value_inside, *options_list)
opt1.pack(padx=5, pady=5)

lb0 = tkinter.Label(text="Enter your nickname: ")
lb0.pack(padx=5, pady=5)

ent_username = tkinter.Entry()
ent_username.pack()

btn1 = tkinter.Button(text="Get last matches", command=start_history)
btn1.pack(padx=5, pady=5)

ls1 = tkinter.Listbox(width=60)
ls1.pack()




window.mainloop()














