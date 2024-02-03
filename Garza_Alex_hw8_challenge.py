#Created by Alex Garza CS303E 
#4/3/2023

import random

class Car:
    num_cars = 0
    
    def __init__(self):
        Car.num_cars += 1
        self.name = f"Car {Car.num_cars}"
        self.speed = random.uniform(60, 80)  # mph
        self.max_distance = random.uniform(200, 300)  # miles
        
    def __str__(self):
        return f"{self.name} Speed: {self.speed:.2f} mph Max Distance: {self.max_distance:.2f} miles"
    

class Race:
    
    def __init__(self, distance):
        self.distance = distance
        self.racers = []
        
    def start_race(self, num_racers):
        self.racers = [Car() for _ in range(num_racers)]
        
    def determine_winner(self):
        winner = None
        max_speed = 0
        for racer in self.racers:
            if racer.speed > max_speed and racer.max_distance >= self.distance:
                max_speed = racer.speed
                winner = racer
        return winner.name if winner else "No winner"
    

def main():
    race = Race(250)
    print(f"Race Distance: {race.distance}")
    
    race.start_race(5)
    for racer in race.racers:
        print(racer)
    print(f"Winner: {race.determine_winner()}")
    
    race.start_race(8)
    for racer in race.racers:
        print(racer)
    print(f"Winner: {race.determine_winner()}")

if __name__ == '__main__':
    main()
