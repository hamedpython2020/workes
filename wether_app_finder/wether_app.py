import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
#############################


def get_weather():
    try:
        #   location:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        lat = location.latitude
        log = location.longitude
        print(lat, log)

        exclude = "current"
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=log, lat=lat)
        print(result)
        city_label.config(text=result.split("/")[1])
        #   Time :
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock_label.config(text=current_time)
        time_label.config(text="Local Time")
        #   Weather :
        # api_key = " 235805:63c16fec38fe30.01989602 "
        # api = f"https://one-api.ir/weather/?token={api_key}&action=currentbylocation&lat={lat}&lon={log}"
        api_key = "6993e6e009e3e8b9a6b98437bf34f929"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={log}&appid={api_key}"
        print(api)
        json_data = requests.get(api)
        print(json_data)
        json_data = json_data.json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = round(float(json_data["main"]["temp"]-273.15), 2)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]
        temp_label.config(text=f"{temp}°")
        condition_label.config(text=f"{condition} | FEELS LIKE {temp}°")
        wind_label.config(text=wind)
        humidity_label.config(text=humidity)
        description_label.config(text=description)
        pressure_label.config(text=pressure)

    except Exception as error:
        messagebox.showerror("weather App", "فعلا خرابٌم")
        print(error)
        pass

    pass
#############################


root = tk.Tk()
page = tk.Tk()
page.title("just learning")
root.title("WeatherApp")
root.geometry("900x500+300+200")
root.resizable(False, False)
##########################################
                         #########Search_Box
search_image = tk.PhotoImage(file="search.png")
search_image_label = tk.Label(root, image=search_image)
search_image_label.pack(pady=20, side=tk.TOP)
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", fg="white", border=0)
textfield.place(x=280, y=40)
search_icon = tk.PhotoImage(file="icon.png")
search_icon_button = tk.Button(root, image=search_icon, border=0, cursor="hand2", bg="#404040", command=get_weather)
search_icon_button.place(x=590, y=34)
##################
#   Logo
logo_image = tk.PhotoImage(file="logo.png")
logo_label = tk.Label(root, image=logo_image)
logo_label.pack(side=tk.TOP)
#   frame
frame_image = tk.PhotoImage(file="box.png")
frame_label = tk.Label(root, image=frame_image)
frame_label.pack(pady=10, side=tk.BOTTOM)
#   city:
city_label = tk.Label(root, font=("arial", 40, "bold"), fg="#e355cd")
# city_label.place(x=120, y=160)
#   Time:
time_label = tk.Label(root, font=("arial", 20, "bold"), fg="#4b4bcc")
time_label.place(x=120, y=230)
#   Clock
clock_label = tk.Label(root, font=("Helvetica", 20), fg="#4b4bcc")
clock_label.place(x=120, y=270)

#   Labels :
label_1 = tk.Label(root, text="Wind", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
label_1.place(x=120, y=400)

label_2 = tk.Label(root, text="HUMIDITY", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
label_2.place(x=280, y=400)

label_3 = tk.Label(root, text="Description", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
label_3.place(x=450, y=400)

label_4 = tk.Label(root, text="PRESSURE", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
label_4.place(x=670, y=400)

#   Temp:
temp_label = tk.Label(root, font=("arial", 70, "bold"), fg="#e355cd")
temp_label.place(x=590, y=170)

#   Condition :
condition_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", border=False)
condition_label.place(x=590, y=270)
#   Wind:
wind_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
wind_label.place(x=120, y=430)
#   humidity:
humidity_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
humidity_label.place(x=280, y=430)
#   description:
description_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
description_label.place(x=450, y=430)
#   pressure:
pressure_label = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
pressure_label.place(x=670, y=430)
###################################################################################################
# additional label
#   Labels :
# label_12 = tk.Label(root, text="Wind", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
# label_12.place(x=120, y=400)
#
# label_22 = tk.Label(root, text="HUMIDITY", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
# label_22.place(x=280, y=400)
#
# label_32 = tk.Label(root, text="Description", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
# label_32.place(x=450, y=400)
#
# label_42 = tk.Label(root, text="PRESSURE", font=("arial", 15, "bold"), fg="white", bg="#1ab5ef")
# label_42.place(x=670, y=400)
#
# #   Temp:
# temp_label2 = tk.Label(root, font=("arial", 70, "bold"), fg="#e355cd")
# temp_label2.place(x=590, y=170)
#
# #   Condition :
# condition_label2 = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc", border=False)
# condition_label2.place(x=590, y=270)
# #   Wind:
# wind_label2 = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
# wind_label2.place(x=120, y=430)
# #   humidity:
# humidity_label2 = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
# humidity_label2.place(x=280, y=430)
# #   description:
# description_label2 = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
# description_label2.place(x=450, y=430)
# #   pressure:
# pressure_label2 = tk.Label(root, text="...", font=("arial", 20, "bold"), fg="#1ab5ef", bg="#404040")
# pressure_label2.place(x=670, y=430)



root.mainloop()
