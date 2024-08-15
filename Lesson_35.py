# Task 1: Analyzing Weather Data. You have a JSON file weather_data.json that contains information about the weather in different cities for a week. The data includes date, city name, temperature, humidity, and weather condition (sunny, rainy, cloudy, etc.). You need to identify the city with the highest average temperature for the week and print its name along with the average temperature.

import json

with open('./JSON/weather.json', 'r') as forecast_file:
    data_from_json = json.load(forecast_file)

city_temp_sums = {}
city_temp_counts = {}

for key in data_from_json["weather"]:
    town = key["city"]
    temperature = key["temperature"]

    if town not in city_temp_sums:
        city_temp_sums[town] = 0
        city_temp_counts[town] = 0

    city_temp_sums[town] += temperature
    city_temp_counts[town] += 1
for first_city in city_temp_sums:
    break

max_avg_temp = city_temp_sums[first_city] / city_temp_counts[first_city]
hottest_city = first_city

for city in city_temp_sums:
    avg_temp = city_temp_sums[city] / city_temp_counts[city]

    if avg_temp > max_avg_temp:
        max_avg_temp = avg_temp
        hottest_city = city

print(
    f"The city with the highest average temperature is {hottest_city} with an average temperature of {max_avg_temp}°C.")

# Task 2: Processing Movie Data. You have a JSON file movies.json containing information about movies. Each record includes the movie title, director, year of release, rating, and a list of genres. Your task is to create a new JSON file filtered_movies.json containing only those movies that were released after 2015 and have a rating higher than 7.

import json

with open('./JSON/movies.json', 'r') as movie_file:
    data_from_json = json.load(movie_file)

top_movies = []
for movie in data_from_json['movies']:
    title = movie['title']
    year = movie['year']
    rating = movie['rating']

    if title not in top_movies:
        if year > 2015 and rating > 7:
            top_movies.append(title)

with open('filtered_movies.json', 'w') as filtered_movies:
    json.dump(f'The movies by your criteria are: {top_movies}', filtered_movies)

# Task 3: Creating Sales Reports. You have a JSON file sales.json that contains information about sales in a store. Each record includes a sales ID, product name, number of units sold, and the sale amount. You need to create a report that shows the total revenue of the store and the number of units sold for each product. The result should be written to a new JSON file sales_report.json .

import json

with open('./JSON/sales.json', 'r') as shop_file:
    data_from_json = json.load(shop_file)
quantity_of_the_items = sum([])
cost_of_the_items = sum([])

for item in data_from_json['sales']:
    qua = item["quantity"]
    cost = item['total']
    quantity_of_the_items += qua
    cost_of_the_items += cost

print(quantity_of_the_items)
print(cost_of_the_items)

with open('sales_report.json', 'w') as file:
    json.dump(f'Quantity of the items is: {str(quantity_of_the_items)} and Cost of the items is: {str(cost_of_the_items)}', file)
