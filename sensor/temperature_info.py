<<<<<<< Updated upstream
from house_info import HouseInfo
from datetime import date
=======
<<<<<<< Updated upstream
=======
from house_info import HouseInfo
<<<<<<< Updated upstream
from datetime import date, datetime
=======
from datetime import date
>>>>>>> Stashed changes
>>>>>>> Stashed changes

class TemperatureData(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
<<<<<<< Updated upstream
            # Convert string of integers into integers based 10
            recs.append(int(rec, base=10))
        return recs
    
    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("temperature", rec_area)
=======
<<<<<<< Updated upstream
             recs.append(int(rec, base=10))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area('temperature',rec_area)
=======
            # Convert string of integers into integers based 10
            recs.append(int(rec, base=10))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("temperature", rec_area)
>>>>>>> Stashed changes
>>>>>>> Stashed changes
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("temperature", rec_date)
<<<<<<< Updated upstream
        return self._convert_data(recs)
=======
<<<<<<< Updated upstream
        return self._convert_data(recs)
=======
        return self._convert_data(recs)
>>>>>>> Stashed changes
>>>>>>> Stashed changes
>>>>>>> Stashed changes
