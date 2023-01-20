# Runner script for all modules

from load_data import load_sensor_data
##############################
# Do not remove these two lines
# They are needed to validate your unittest
data = []
print("Sensor Data App")
##############################

# Module 1 code here:
data = load_sensor_data()
print('loaded records: {}'.format(len(data)))


# Module 2 code here:
house_info = HouseInfo(data)
test_area = 1
recs = house_info.get_data_by_area("id", rec_area=test_area)
print("\nHouse sensor records for area {} = {}".format(test_area, len(recs)))

test_data = datetime.stoptime ("s/9/20", "%m/%d/%y")
recs = hpuse_info.get_data_by_date("id", rec_datev= test_data)
print("House sensor records for date {} = {}".format(test_date.strftime("%m/%d/%y")))
# Module 3 code here:
# Module 4
print("\nProcessing Temperature Information")
home_temp = TemperatureData(data)
room1_temp = home_temp.get_data("temperature", 1)
room2_temp = home_temp.get_data("temperature", 2)
rooms_temp = home_temp.get_data("temperature")
print(f"Max Room 1 {max(room1_temp)}, min {min(room1_temp)}, avg {mean(room1_temp)}, records {len(room1_temp)}")
print(f"Max Room 2 {max(room2_temp)}, min {min(room2_temp)}, avg {mean(room2_temp)}, records {len(room2_temp)}")
print(f"Rooms Avg {mean(rooms_temp)}, records {len(rooms_temp)}")

# Module 5
print("\nProcessing Humidity Information")
home_humi = HumidityData(data)
room1_humi = home_humi.get_data("humidity", 1)
room2_humi = home_humi.get_data("humidity", 2)
rooms_humi = home_humi.get_data("humidity")
print(f"Max Room 1 {max(room1_humi)}%, min {min(room1_humi)}%, avg {mean(room1_humi)}%, records {len(room1_humi)}")
print(f"Max Room 2 {max(room2_humi)}%, min {min(room2_humi)}%, avg {mean(room2_humi)}%, records {len(room2_humi)}")
print(f"Rooms Avg {mean(rooms_humi)}%, records {len(rooms_humi)}")

# Module 6
print("\nProcessing ParticleCounter Information")
home_pc = ParticleData(data)
rooms_pc = home_pc.get_data("particulate")
rooms_aq = home_pc.get_concentrations(rooms_pc)
print("Good Air Quality Recs: {0}".format(rooms_aq["good"]))
print("Moderate Air Quality Recs: {0}".format(rooms_aq["moderate"]))
print("Bad Air Quality Recs: {0}".format(rooms_aq["bad"]))

# Module 7
print("\nProcessing Energy Consumption")
home_energy = EnergyData(data)
rooms_energy = home_energy.get_data("energy_usage")
print("Rooms records {0}".format(len(rooms_energy)))
energy = home_energy.calculate_energy_usage(rooms_energy)
print("Energy Consumption: {0:.2E} watts ".format(energy))