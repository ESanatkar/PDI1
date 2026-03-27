import pandas as pd

'''
Exercise 1

    Concatenation
'''

# Morning air quality readings
morning = pd.DataFrame({
    'station': ['London Marylebone', 'Birmingham Tyburn', 'Leeds Centre'],
    'no2_ugm3': [48.2, 31.5, 27.8]
})

# Afternoon air quality readings
afternoon = pd.DataFrame({
    'station': ['London Marylebone', 'Birmingham Tyburn', 'Leeds Centre'],
    'no2_ugm3': [55.1, 29.3, 31.4]
})

result = pd.concat([morning, afternoon], ignore_index=True)
#print(result)

# With ignore_index=True the index is set to be ordered and aligned with the merged list, rather than keeping its original index.

result1 = pd.concat([morning, afternoon], ignore_index=True, axis="columns")
#print(result1)

# With them being colums, instead of the indexes being ordered and individual for each row, they are now given individual indexes.

'''
Exercise 2

    Left Merge
'''

readings = pd.DataFrame({
    'reading_id': [1001, 1002, 1003, 1004],
    'station_id': ['S01', 'S02', 'S01', 'S04'],
    'no2_ugm3': [48.2,  31.5,  55.1,  27.8 ]
})

stations = pd.DataFrame({
    'station_id': ['S01', 'S02', 'S03'],
    'location':   ['London Marylebone', 'Birmingham Tyburn', 'Leeds Centre']
})

result3 = pd.merge(readings, stations, how="left", on="station_id")
#print(result3)

# Station with ID S04 is NaN, as there is not a location that matches for it.

'''
Exercise 3

    Update vs Combine First
'''

# Team A's readings (some gaps)
team_a = pd.DataFrame({
    'station': ['Cardiff', 'Bristol', 'Exeter'],
    'pm10': [18.4,  None, 22.1],
    'ozone': [None, 61.2, 58.9]
})

# Team B's readings (different gaps, and some different values)
team_b = pd.DataFrame({
    'station': ['Cardiff', 'Bristol', 'Exeter'],
    'pm10': [19.9, 17.5, 21.0],
    'ozone': [63.1, 60.8, None]
})

result5 = team_a.combine_first(team_b)
print(result5)

# All values given by team_a are preserved, with the values from team_b being input where team_a had missing readings.

result6 = team_a.update(team_b)
print(result6)

# Returns None, interesting? doesnt even give any data back.

# The most appropriate is combine_first, as you can alternate which you'd prefer to update to, and which you'd prefer to merge with to keep all data intact.