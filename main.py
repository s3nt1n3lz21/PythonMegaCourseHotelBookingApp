import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel():
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availabile = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availabile == "yes":
            return True
        else:
            return False

class ReservationTicket():
    def __init__(self, customer_name, hotel):
        self.customer_name = customer_name
        self.hotel = hotel

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        """
        return content

if __name__ == '__main__':
    print(df)
    hotel_id = input("Enter the id of the hotel:")
    hotel = Hotel(hotel_id)

    if hotel.available():
        hotel.book()
        customer_name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(customer_name, hotel)
        print(reservation_ticket.generate())
    else:
        print("Hotel has no rooms available")
