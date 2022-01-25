from peloton import PelotonWorkout
workouts = PelotonWorkout.list()
#grab the first cycling workout, other types don't have resistance
strive_record = 0.0
workout_title = ""
records = {
    '5'  : { 'Class' : "", 'Strive': 0.0},
    '10' : { 'Class' : "", 'Strive': 0.0},
    '15' : { 'Class' : "", 'Strive': 0.0},
    '20' : { 'Class' : "", 'Strive': 0.0},
    '30' : { 'Class' : "", 'Strive': 0.0},
    '45' : { 'Class' : "", 'Strive': 0.0},
    '60' : { 'Class' : "", 'Strive': 0.0},
    '75' : { 'Class' : "", 'Strive': 0.0},
    '90' : { 'Class' : "", 'Strive': 0.0}
    }

for workout in workouts:
    if workout.metrics_type == 'cycling':
        if workout.strive_score is not None:
            duration = workout.ride.duration/60
            ride_length = "%d" %duration
            strive_score = workout.strive_score
            workout_title ="%s with %s on %s" % (workout.ride.title,workout.ride.instructor,workout.start_time.strftime("%m/%d/%Y"))
#            print(workout_title)
#            print("strive_score: %0.1f" %strive_score)
            if strive_score > records[ride_length]['Strive']:
                records[ride_length]['Class'] = workout_title
                records[ride_length]['Strive'] = strive_score
for time_workout in records:
    print("%s Minute Record: %s, %.1f" % (time_workout, records[time_workout]['Class'], records[time_workout]['Strive']))
    
    
