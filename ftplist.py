from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
for workout in workouts:
    if workout.ride.title == '20 min FTP Test Ride':
        metrics = workout.metrics
        print("Date: %s FTP Score: %0.2f %s, max_heartrate %d" % (workout.created.strftime("%m-%d-%Y"),metrics.output.average *.95,metrics.output_summary.unit, metrics.heart_rate.max))
        

    
