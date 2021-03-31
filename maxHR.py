#!/usr/bin/env python3
from numpy import *
import matplotlib.pyplot as plt

hrs = []
kjoules  = []
duration = []
hrmax =0
isodate =""

from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
for workout in workouts:
    if workout.metrics_type == "cycling":
        metrics = workout.metrics
        try:
            hr = metrics.heart_rate.max
            if hr >hrmax:
                hrmax = hr
                isodate = workout.start_time.isoformat()
            hrs.append(metrics.heart_rate.max)
            kjoules.append(metrics.output_summary.value)
            duration.append(metrics.workout_duration)
#            print ("%d,%d,%d" %(metrics.heart_rate.max, metrics.output_summary.value,metrics.workout_duration))
        except:
            pass
#plt.plot(hrs)
print("%s, max_heart_rate %d" % (isodate,hrmax))
#plt.show()
        

    
