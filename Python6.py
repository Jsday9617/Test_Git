alien_0 = {"color": "green", "points": 5}
print(alien_0["color"])
print(alien_0["points"])
#example of a dictionary
new_points = alien_0["points"]
print("You just earned " + str(new_points) + " points!")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "point": 10}
alien_2 = {"color": "red", "point": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#make 30 green aliens
#aliens = []
#for alien_number in range(30):
#   new_alien = {"color": "green", "points: 5", "speed": "slow"}
#  aliens.append(new_alien)


