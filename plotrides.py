import sys
import signal
import os
from numpy import *
import matplotlib.pyplot as plt
import datetime
import time

def sig(a,b):
    print("got sigint, exiting")
    os._exit(0)

def timercb(e):
    print("tick")
    
signal.signal(signal.SIGINT,sig)
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
        fig = plt.figure(1,figsize = (9,9))
        ax = plt.gca()
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
        timer = fig.canvas.new_timer(interval=5000)
        timer.add_callback(timercb,ax)
        timer.start()
        try:
            plt.show()
        except KeyboardInterrupt:
            sys.exit(0)
    
    
