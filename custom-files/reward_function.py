prev_steering_angle = None

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
    return float(reward)