from numpy import *
import matplotlib.pyplot as plt
import datetime

player_url = "https://members.onepeloton.com/classes/player/"
from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
#grab the first cycling workout, other types don't have resistance
for workout in workouts:
    if workout.ride.instructor.last_name == "Thompson Rule":
        print("%s\n %s" % (workout.ride.title,workout.ride.original_air_time.strftime("%m/%d.%Y")))
        print("%s%s" % (player_url,workout.ride.id))

    
    
