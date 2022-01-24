from numpy import *
import matplotlib.pyplot as plt
import datetime

from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
#grab the first cycling workout, other types don't have resistance
for workout in workouts:
    if workout.metrics_type == 'cycling':
        metrics = workout.metrics
        resistance = metrics.resistance
        output = metrics.output
        heart_rate= metrics.heart_rate
        cadence = metrics.cadence
        break

plt.figure(1,figsize = (9,9))
plt.suptitle("%s\n %s" % (workout.ride.title,workout.start_time.strftime("%m/%d.%Y")))
plt.subplot(411)
plt.ylabel("resistance")
plt.plot(resistance.values)
plt.subplot(412)
plt.ylabel("cadence")
plt.plot(cadence.values)
plt.subplot(413)
plt.ylabel("output")
plt.plot(output.values)
plt.subplot(414)
plt.ylabel("heart rate")
plt.plot(heart_rate.values)
plt.show()

    
    
