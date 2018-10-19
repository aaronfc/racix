#!/usr/env python3
from time import sleep

class Helpers:
    @staticmethod
    def kmh2ms(kmh):
        return kmh*1000./3600
    @staticmethod
    def ms2kmh(ms):
        return ms/1000.*3600
    @staticmethod
    def ms2s(ms):
        return ms/1000.

class Car:
    def __init__(self, engine):
        self.distance = 0
        self.speed = 0
        self.acceleration = 0
        self.engine = engine

    def update(self):
        self.acceleration = self.engine.max_acceleration

    def simulate(self, delta):
        final_speed = self.speed + self.acceleration * Helpers.ms2s(delta)
        final_speed = min(final_speed, self.engine.max_speed)
        self.distance += 0.5*(final_speed + self.speed) * Helpers.ms2s(delta)
        self.speed = final_speed

    def display(self):
        print("Current speed: {} km/h".format(Helpers.ms2kmh(self.speed)))
        print("Current acceleration: {} m/s".format(self.acceleration))
        print("Distance traveled: {}".format(self.distance))

class Engine:
    def __init__(self):
        self.max_speed = Helpers.kmh2ms(382.182) # Max speed for a F1 engine by last technical specification: https://en.wikipedia.org/wiki/Formula_One_car#Technical%20specifications%20for%202017
        self.max_acceleration = 14.2 # Aproximate value 1.45G https://en.wikipedia.org/wiki/Formula_One_car#Acceleration

engine = Engine()
car = Car(engine)

time = 0
while True:
    print("AT TIME: {}".format(time))
    car.display()
    car.update() # Take decisions
    car.simulate(1000) # Simulate
    time += 1000
    sleep(1)



'''
Worklog:

Currently 4km are done in about 44 seconds. That matches more or less with the record set in Indanapolis_500 (https://en.wikipedia.org/wiki/Indianapolis_500) of 37.895 sec for the 4km length. Set with max speed of 382.182km/h and ours is 360km/h.
AT TIME: 44000
Current speed: 360.0 km/h
Current acceleration: 14.2 m/s
Distance traveled: 4047.6

Increasing max speed to 382.182 gave a 42s time. We are starting from 0, so it could match the Indianapolis_500 record data very well.
AT TIME: 42000
Current speed: 382.182 km/h
Current acceleration: 14.2 m/s
Distance traveled: 4060.177500000003

Starting from 382.182 gave a 38s time, marches perfectly to the Indianapolis 500 reference.
AT TIME: 38000
Current speed: 382.182 km/h
Current acceleration: 14.2 m/s
Distance traveled: 4034.1433333333366

'''
