import requests
import json
url = "https://v2.whil.blue/platform/teams/detailreport"
headers = {"Authorization": "Bearer eyJjdHkiOiJ0ZXh0XC9wbGFpbiIsImVuYyI6IkExMjhHQ00iLCJleHAiOjE0NzgyMTU0ODMzMjEsImFsZyI6IlJTQTFfNSJ9.VVSAzZOUy8ssxsYjXDfQ5eApT-PQFdS1p3rbLxnsxu0McfpLk5yIG-MpfSyQuW8Ez7dJH8AjFK-DuWqljQwIkD6i9ZbwIdPYHIm41rKq9IYaVyXbqxV4TA_QOielNSaHabVblGu5OoGFEiOH8z2dPyHNPQ5IZednmHZ0DjqRw0o.TWllo-nF6GKnGSq4.j5g_KEcLbcYLxK0N_yJhW9riFBi8bk8tpX9ac014bMmeCq875663fq09FsT0LJkzB4tJOoc_aMgdHJcCA6JgVzDmsj3p4Mtm6xlOJXheGJ0d6TEahLgfZG_3YZaGgLE2wvz0hKYcXYBU-MpRo3LeXOWlOY7FWLuVuntbKgXoBTZFkrUASVne4B137b4h1VroNVe9cF9hKJQFKmQa7F1H7_HPUW9yLjtjFD74AtAyuvEjryP591V8R6Zc859hYhihydlH1NKXDA.X8qdieD0RHsvTa9n6Pi6Mg"}

response = requests.get(url,headers=headers)
# print response.content

jData = json.loads(response.content)

for el in jData["teamDetails"]:
    for users in el["users"]:
        if users["onboardYN"]==True:
            print el["name"], users["email"]