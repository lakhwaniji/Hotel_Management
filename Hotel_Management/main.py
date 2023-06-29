import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")


class Hotel:
    def __init__(self, id):
        self.id = id
        self.name = df.loc[df["id"] == id]["name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.id, "available"] = "no"  # <------ IMPORTANT POINT TO NOTE
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.id]["available"].squeeze()
        if (availability == "yes"):
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, cus_name, hot_obj):
        self.cus_name = cus_name
        self.hotel = hot_obj

    def generate(self):
        content = f'''
        Thank You for using our service 
        Here are your details
        Name={self.cus_name}
        Hotel Name={self.hotel.name}'''
        return content


class CreditCard:
    def __init__(self, num):
        self.number = num

    def validate(self, expiration, cvc, holder):
        dict = {"number": self.number, "expiration": expiration, "cvc": cvc, "holder": holder}
        print(dict)
        print(df_cards[0])
        if dict in df_cards:
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_hotel(self):
        pass


class SpaTicket:
    def __init__(self, cus_name, hotel_object):
        self.customer_name = cus_name
        self.hotel = hotel_object

    def generate_ticket(self):
        result = f"""
                Your Spa registration is confirmed 
                Here are the details 
                Name--> {self.customer_name}
                Hotel-->{self.hotel.name}"""
        return result


hotel_id = input("Enter id of the hotel")
hotel = SpaHotel(hotel_id)
if (hotel.available()):
    credit_card = CreditCard("1234")
    if (credit_card.validate("12/26", "123", "JOHN SMITH")):
        hotel.book()
        name = input("Enter the name of the customer")
        ticket = ReservationTicket(name, hotel)
        print(ticket.generate())
        spa = input("Would you like to add the spa package to your current package")
        if spa == "yes":
            hotel.book_spa_hotel()
            spa_ticket = SpaTicket(name, hotel)
            print(spa_ticket.generate_ticket())
    else:
        print("Credit Card Declined")

else:
    print("Sorry the selected hotel not available")
