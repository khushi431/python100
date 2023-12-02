travel_log = [
  {
      "country" : "Japan",
      "visits" : 9,
      "cities" : ["tokoyo", "kosaba", "kobe"]
  },
  {
      "country" : "America",
      "visits" : 4,
      "cities" : ["austin", "boston", "portland"]
  },
  {
      "country" : "India",
      "visits" : 8,
      "cities" : ["powai", "amritsar", "Jalandhar"]
  }
]

def add_new_country(country, visits, cities):
  new_con = {}
  new_con["country"] = country
  new_con["visits"] = visits
  new_con["cities"] = cities

  travel_log.append(new_con)

print(travel_log)
add_new_country("Russia", 30, ["ff", "bd", "efg"])
print()
print(travel_log)