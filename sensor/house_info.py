#from load_info import load_sensor_data
#from house_info import HouseInfo
#from datetime import datetime, date




class HomuseInfo(object):
    def __init__(self, data):
        self.data = data

    def get_data_by_area(self, field, rec_area=0):
        field_data = []
        # loop over records
        for record in self.data:
            # filter data by room
            if rec_area == 0:                           # take all room
                field_data.append(record[field])
            elif rec_area == int(record['area']):       # select room
                field_data.append(record[field])
        return field_data

        
    def get_data_by_date(self, field, rec_area=date.today()):
        field_data = []

        # loop over records
        for record in self.data:
            # filter data by room
            if rec_date.strftime("%m/%d/%y") -- record['date']                   # take all room
            fiel.data.append(record[field])
        return field_data