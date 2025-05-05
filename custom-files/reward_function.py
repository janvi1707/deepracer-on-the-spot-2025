""" prev_steering_angle = None

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    global prev_steering_angle

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    speed=params['speed']
    reward=0.0;
    steering_angle = params['steering_angle']
    if params['distance_from_center']> 0.5*(params['track_width']):
        reward=1e-3
    if params['is_crashed']:
        reward=1e-3
    
    if prev_steering_angle is None:
        angle_change=0
    else:
        angle_change = abs(steering_angle - prev_steering_angle)

    reward=+speed**2 + 30*(params['progress']/(params['steps']+1));
    if angle_change>25:
        reward*=0.5
    prev_steering_angle= params['steering_angle']
    return float(reward) """

def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:  # REGION 1
        distance_reward= 1.0 
    elif distance_from_center <= marker_2: # REGION 2
        distance_reward= 0.5
    elif distance_from_center <= marker_3: # REGION 3
        distance_reward= 0.1
    else:
        distance_reward= 1e-3  # likely crashed/ close to off track
                                #never set negative or zero rewards

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15 

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        distance_reward*= 0.8

    return float(reward)
    