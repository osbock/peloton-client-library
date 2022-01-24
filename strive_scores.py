from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
#grab the first cycling workout, other types don't have resistance
strive_record = 0.0
workout_title = ""
record_workout =""
for workout in workouts:
    if workout.metrics_type == 'cycling':
        if workout.strive_score is not None:
            strive_score = workout.strive_score
            workout_title ="%s\n %s" % (workout.ride.title,workout.start_time.strftime("%m/%d.%Y"))
            print(workout_title)
            print("strive_score: %0.1f" %strive_score)
            if strive_score > strive_record:
                strive_record = strive_score
                record_workout = workout_title
print("strive record: %s \n strive_score: %f" % (record_workout, strive_record))         
    
    
