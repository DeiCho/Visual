# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import matplotlib.pyplot as plt


# url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"


# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser') #reikalingas pasiimti produkto informacija

# week_days = soup.find_all('span', class_='date')[1:] 

# temperatures = soup.find_all('span', class_='big up-from-zero')[::2]

# night_temp = [temperature.get_text() for temperature in temperatures]

# week_day = [day.get_text() for day in week_days]

# temp_list = []
# for temperture in temperatures:
#     temp_text = temperture.get_text().replace('°C', '')
#     temp_values = int(temp_text[:-1])
#     temp_list.append(temp_values)

# min_length = min(len(week_day), len(temp_list))

# reorder_weekdays = week_day[:min_length]

# reorder_temperature = temp_list[:min_length]

# week_day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(reorder_temperature)
# # # print(temperatures)

# data = {
#     'weekday': reorder_weekdays,
#     'temperature': reorder_temperature
# }

# df = pd.DataFrame(data)

# df_sorted = df.sort_values(by=['weekday'], key=lambda x: pd.Categorical(x, categories=week_day_order, ordered=True))

# plt.figure(figsize=(12, 5))
# plt.bar(df_sorted['weekday'], df_sorted['temperature'])

# plt.xlabel('savaites diena')
# plt.ylabel('temperatura')
# plt.title('Oru prognoze Vilniuje')
# plt.show()

# print(df)