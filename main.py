
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

m_count = len(mission_names)
s_count = 0
s_rate = 0
pre_2kmission = []

for i in range(m_count):
    if (mission_years[i] < 2000):
        pre_2kmission.append(mission_names[i])

    if (mission_success[i] == True): 
        s_count += 1


s_rate = s_count/m_count*100


print("Total number of missions: " + str(m_count))
print("Number of successful missions: " + str(s_count))
print("Success rate: " + str(s_rate))

print("Missions launched before the year 2000: ")

for name in pre_2kmission:
    print("- "+ name)

quit()