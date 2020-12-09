import datetime

# Get my current age from my DOB
def get_age():
    dob = datetime.date(1996, 3, 16)
    td = datetime.datetime.now().date()
    return int((td - dob).days / 365.25)
