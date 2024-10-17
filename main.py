import json
import matplotlib.pyplot as plt

with open('teams.json', 'r') as file:
    data = json.load(file)

teams = [team['name'] for team in data['teams']]
points = [team['points'] for team in data['teams']]

total_points = sum(points)
percentage = [(point / total_points) * 100 for point in points]

plt.figure(figsize=(10, 8))
plt.pie(percentage, labels=teams, autopct='%1.1f%%', startangle=140)

plt.title('Розподіл очок команд у відсотках')

plt.axis('equal')
plt.show()
