import requests 
import time
from win10toast import ToastNotifier
from requests.exceptions import ConnectionError

toaster = ToastNotifier()
i = 0

for i in range(48):
    try:
        response = requests.get("https://ecab.charleystaxi.com/Reservations/LogIn.aspx")
        toaster.show_toast("Connected Successfully")

    except ConnectionError:
        toaster.show_toast("Error Connecting")

    time.sleep(1800)
