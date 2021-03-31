from numpy import *
import matplotlib.pyplot as plt


from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
#grab the first cycling workout, other types don't have resistance
for workout in workouts:
    if workout.metrics_type == 'cycling':
        metrics = workout.metrics
        resistance = metrics.resistance
        break

plt.plot(resistance.values)
plt.show()

    
    
