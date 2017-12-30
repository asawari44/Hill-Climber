import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))


def reset_climber(climber):
    climber.position_index =np.random.randint(climber.step,climber.terrain.shape[1]-climber.n_input-climber.step-1)#i%975 + 3 #
    climber.old_input = climber.terrain[0,climber.position_index:climber.position_index + climber.n_input].reshape(climber.n_input,1)
    climber.input = climber.terrain[0,climber.position_index:climber.position_index + climber.n_input].reshape(climber.n_input,1)
    climber.output = None
    climber.y = 0
    
    climber.position_switch_counter = climber.position_switch_counter + 1
    print("-------NEW POSITION-------")