from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import psycopg2
import time

conn = psycopg2.connect(database = 'BusTransportationSystem', user = 'postgres', password='0000', host='127.0.0.1', port='5432')
cur = conn.cursor() 
#cur.execute()  conn.commit()   


def GetGPSCoordinates(Place):  #"Hamra Street, Beirut, Lebanon" Example
    geolocator = Nominatim(user_agent="BusTransportationSystem")
    location = geolocator.geocode(f"{Place}")
    Coordinate = (location.latitude, location.longitude)
    #print(Coordinate)
def CreateNewUser(Username, Email, PhoneNumber): 
    try: 
        cur.execute(f"INSERT INTO Passenger(Username, Email, Phone_Number, ChosenPlan , SubscriptionDate) VALUES
                        ('{Username}', '{Email}', '{PhoneNumber}', NULL, NULL);")
        return 0 
    except Exception as e: 
        print(e)
        return 1
    pass
def DisplayInformation(UserName): 
    cur.execute(f"SELECT ticketid, finalprice, purchaseDate, BusStop.busstopid, BusStopLocation.stop_location, Visits.visitingbusid
FROM ticket
JOIN passenger ON ticketholdingpassenger = username
JOIN isfoundat ON ifa_passengerid = username
JOIN BusStop ON ifa_busstopid = busstopid
Left JOIN BusStopLocation ON BusStopLocation.busstopid = BusStop.busstopid JOIN Visits ON Visits.visitedbusStopID = BusStop.busstopid JOIN Bus ON Visits.visitingbusid = busnumber
WHERE username = '{UserName}';")
    
    
    
    
    pass




print("Welcome Yalla Tla3!")
Account = input("Do you have an account? (Y/N) : ")
SignIn = False
SignUp = False
Admin = False
while True: 
    if Account.lower() == "y": 
        SignIn = True
        break
    elif Account.lower() == "n":
        SignUp = False
        break
    else: 
        Account = input("Do you have an account? (Y/N) : ")

if SignUp == True: 
    while True: 
        UserN = input("Enter Username: ")
        Em = input("Enter Email: ")
        PhoneNum = input("Enter Phone Number: ")
        ReturnStat = SignUp(UserN,Em, PhoneNum)
        if  ReturnStat == 0: 
            break

#Get UserName 
UserName = UserN
while True: 
    print(f"Welcome {UserName}! What would you like to do? \n")
    print("1: View Your Tickets and their Information")
    print("2: Purchase Ticket")
    print("3: Subscribe to a Plan")
    print("4: View Personal Information")
    print("5: View Nearby Bus Stops and the Timings of Buses passing by")
    print("6: Log out")

    Input = input("Input: ")
    if Input == 1: 
        DisplayInformation(UserName)
        pass
    if Input == 2: 
        pass
    if Input == 3: 
        pass
    if Input == 4: 
        pass
    if Input == 5: 
        pass
    if Input == 6: