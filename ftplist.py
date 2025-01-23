from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
print("Date,FTP Score (kj),Max Heartrate")
for workout in workouts:
    if workout.ride.title == '20 min FTP Test Ride':
        metrics = workout.metrics
        print("%s, %0.2f, %d" % (workout.created.strftime("%m-%d-%Y"),metrics.output.average *.95, metrics.heart_rate.max))
        

    
