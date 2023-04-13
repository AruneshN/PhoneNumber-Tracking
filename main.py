#get phonenumber detail
import tkinter as tk
from tkinter import*
import phonenumbers
from phonenumbers import timezone,carrier,geocoder
from phonenumbers import phonemetadata

from PIL import ImageTk,Image
import geopy
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim
import urllib3
# pip install opencage
root=tk.Tk()
root.geometry("800x660+40+0")
root.title("Tracker")
root.config(bg="#0e1b30")
bg=tk.PhotoImage(file="C:\\Users\ELCOT\Desktop\py projects\phonenumberdetails\Top.png")
Label(root,image=bg).pack()
Label(root,text="Enter Number",bg="#0e1b30",fg="white",font=("times new roman",18,"bold")).place(x=200,y=461)
number=tk.Entry(root,bg="white",justify=tk.CENTER,font=("times new roman",15))
number.place(x=400,y=465)

promos = tk.Toplevel()
promos.geometry("300x200+1000+0")
promos.title("About me")
promos.config(bg="black")
ln=tk.PhotoImage(file="C:\\Users\ELCOT\Desktop\py projects\phonenumberdetails\IN.png")
Label(promos,image=ln).place(x=40,y=30)
Label(promos,text="ARUNESH .N",bg="black",fg="white",font=("times new roman",17,"bold")).place(x=130,y=40)
insta=tk.PhotoImage(file="C:\\Users\ELCOT\Desktop\py projects\phonenumberdetails\INSTAS.png")
Label(promos,image=insta).place(x=40,y=100)
Label(promos,text="arunesh2205",bg="black",fg="white",font=("times new roman",17,"bold")).place(x=130,y=110)

def search():
    map=tk.Toplevel()
    map.geometry("850x800+300+0")
    map.title("LOCATION")
    map.config(bg="#0e1b30")
    bgm = Image.open("C:\\Users\ELCOT\Desktop\py projects\phonenumberdetails\map.png")
    resize = bgm.resize((800, 800), Image.ANTIALIAS)
    news = ImageTk.PhotoImage(bgm)
    Label(map, image=news).pack()
    mobile=phonenumbers.parse(number.get().strip())
    # __________________________________________MAP__________________________________________________________________
    def count():
        maps = tk.Toplevel()
        maps.geometry("850x800+300+0")
        maps.title("LOCATION")
        maps.config(bg="#0e1b30")
        map_wid=TkinterMapView(maps,width=600,height=400,corner_radius=0)
        map_wid.pack(fill="both",expand=True)
        map_wid.set_address(country, marker=True)
    def Loc():
        maps = tk.Toplevel()
        maps.geometry("850x800+300+0")
        maps.title("LOCATION")
        maps.config(bg="#0e1b30")
        loc.wid=TkinterMapView(maps,width=600,height=400,corner_radius=0)
        loc.wid.pack(fill="both",expand=True)
        loc.wid.set_address(GetLoc,marker=True)
    def latti():
        lati = tk.Toplevel()
        lati.geometry("850x800+300+0")
        lati.title("LOCATION")
        lati.config(bg="#0e1b30")
        lati.wid = TkinterMapView(lati, width=600, height=400, corner_radius=0)
        lati.wid.pack(fill="both", expand=True)
        lati.wid.set_address(lat, marker=True)
    def contin():
        cont = tk.Toplevel()
        cont.geometry("850x800+300+0")
        cont.title("LOCATION")
        cont.config(bg="#0e1b30")
        cont.wid = TkinterMapView(cont, width=600, height=400, corner_radius=0)
        cont.wid.pack(fill="both", expand=True)
        cont.wid.set_address(time, marker=True)
    #get time zone a phone number
    time=timezone.time_zones_for_number(mobile)
    times=Button(map,text=time,bg="#0e1b30",relief=FLAT,fg="white",activeforeground='black',command=contin,
                 activebackground="blue",font=("times new roman",12,"bold"))
    times.place(x=230-50,y=369)
    Label(map,text="Continent:",bg="#0e1b30",fg="white",font=("times new roman",13,"bold")).place(x=50-20,y=373)
    # getting carrier of phone number
    Sim=carrier.name_for_number(mobile,"en")
    sim=Button(map,text=Sim,relief=FLAT,bg="#0e1b30",fg="white",activeforeground='black',activebackground="blue",font=("times new roman",12,"bold"))
    sim.place(x=230-50,y=451)
    Label(map,text="NetWork:",bg="#0e1b30",fg="white",font=("times new roman",13,"bold")).place(x=50-20,y=455)
    #___________________________________country_______________________________________
    # getting region information
    country=geocoder.description_for_number(mobile,"en")
    Country=Button(map,text=country,relief=FLAT,bg="#0e1b30",fg="white",command=count,
                   activeforeground='black',activebackground="blue",font=("times new roman",12,"bold"))
    Country.place(x=230-50,y=492)
    Label(map,text="Country:",bg="#0e1b30",fg="white",font=("times new roman",13,"bold")).place(x=50-20,y=496)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>countryNAME>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    code=phonenumbers.region_code_for_number(mobile)
    Code=Button(map,text=code,bg="#0e1b30",relief=FLAT,fg="white",activeforeground='black',activebackground="blue",font=("times new romman",12,"bold"))
    Code.place(x=230-50,y=542-9)
    Label(map,text="Country Code:",bg="#0e1b30",fg='white',font=("times new roman",13,"bold")).place(x=50-20,y=546-9)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>service>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    num=Button(map,text=mobile,bg="#0e1b30",relief=FLAT,activeforeground='black',activebackground="blue",fg="white",font=("times new roman",12,"bold"))
    num.place(x=230-50,y=575)
    Label(map,text="Phone Carrier:",bg="#0e1b30",fg="white",font=("times new roman",13,"bold")).place(x=50-20,y=591-9)
    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>geopy>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    loc=Nominatim(user_agent="GetLoc")
    # entering location name
    # GetLoc=loc.geocode("germany")
    GetLoc = loc.geocode(country)
    print(GetLoc.address)
    Loc = Button(map, text=GetLoc, bg="#0e1b30", relief=FLAT, fg="white",command=Loc,
                 activeforeground='black', activebackground="blue", font=("times new roman", 12, "bold"))
    Loc.place(x=230-50, y=410)
    Label(map, text="Location :", bg="#0e1b30", fg="white", font=("times new roman", 13, "bold")).place(x=50-20,y=423-10)
    lat=GetLoc.latitude,GetLoc.longitude
    # print("Latitude = ",GetLoc.latitude,"\n"),print("Longitude = ",GetLoc.longitude)
    Label(map, text="Latitude &\nLongitude :", bg="#0e1b30", fg="white",font=("times new roman", 13, "bold")).place(x=50-20,y=645-9)
    lats=Button(map,text=lat,bg="#0e1b30",fg="white",relief=FLAT,activeforeground='black',command=latti,
                activebackground="blue",font=("times new roman",12,"bold"))
    lats.place(x=230-50,y=632)
    map.mainloop()
sear=tk.Button(root,text="Track",highlightbackground="red",highlightthickness=1,activebackground="blue",
               bg="#0e1b30",fg="white",command=search,activeforeground='black',
               font=("times new roman",17,"bold"))
sear.place(x=340,y=600)
promos.mainloop()

root.mainloop()
