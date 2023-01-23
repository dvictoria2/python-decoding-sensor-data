from load_info import load_sensor_data
#from house_info import HouseInfo
#from datetime import datetime, date

# Module 3: Create an instance of sensor data

class HousInfo(object):
    def __init__(self, data):
        self.data = data
        
    def get_data_by_area (self, field, rec_area=0):
        field_data = []
        for record in self.data:
            if rec_area == 0:
              field.data.append(record[field])
            elif rec_area == int((record['area'])):
                field.data.append(record[field])
        return field_data

    def get_data_by_date (self, field, rec_date =dare.today()):
        field_data = []

        for record in self.data:
            if rec_date.strftime("%m/%d/%y") == record['date']:
                field_data.append(record[field])
        return field_data

