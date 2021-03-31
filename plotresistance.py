from numpy import *
import matplotlib.pyplot as plt


from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
workout = workouts[2]
metrics = workout.metrics
resistance = metrics.resistance.values
plt.plot(resistance)
    
