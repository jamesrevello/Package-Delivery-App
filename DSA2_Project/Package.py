import datetime
class Package:
    def __init__(self, Id, address, city, state, Zip, deadline, weight, status="At Hub"):
        self.Id = Id
        self.address = address
        self.city = city
        self.state = state
        self.Zip = Zip
        self.deadline = deadline
        self.weight = weight
        self.status = status  # TODO: ensure status == delivered (including time) or NOT delivered
        self.delivery_time = None
        self.left_hub_at = None
        self.truck_loaded_on = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.Id,
            self.truck_loaded_on,
            self.address,
            self.city,
            self.state,
            self.Zip,
            self.deadline,
            self.weight,
            self.status,
            )

# Checks provided user time against package delivery time/departure to determine package status for return
    def set_package_status(self, user_time):
        if user_time <= datetime.timedelta(hours=10, minutes=20) and self.Id == 9:
            self.address = "300 State St"
        if self.delivery_time < user_time:
            self.status = "Delivered at " + str(self.delivery_time)
        elif self.left_hub_at < user_time:
            self.status = "En route"
        else:
            self.status = "At Hub"


