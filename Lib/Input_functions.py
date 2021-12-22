from .RPS_encoding import RPS_encode, RPS_decode, RPSpair_encode, RPSpair_decode
import tensorflow as tf
from .Feature_engineering import get_dist, normalise_dist

def Get_Prediction_LSTM(model, opponent_history, player_history):
    input_raw = [x + y if x != '' and y != '' else 'PR' for (x,y) in zip(player_history, opponent_history)]
    #print(input_raw)
    #format history for input
    input_eval = [RPSpair_encode(c) for c in input_raw]
    input_eval = tf.expand_dims(input_eval, 0)
    
    #high temperature  => suprising output
    #low temperature => predictable output
    temperature = 0.1; 
    
    model.reset_states()
    
    prediction = model(input_eval)
    prediction = tf.squeeze(prediction, 0)
    
    prediction = prediction / temperature
    predicted_id = tf.random.categorical(prediction, num_samples = 1)[-1,0].numpy()
    #print(predicted_id)
    #print("Guessing: " + RPSpair_decode(predicted_id))
    return RPSpair_decode(predicted_id)[0]

def LSTM_player(prev_play, opponent_history = [], play_history=[''], model = [None]):
    #Load model if not loaded
    if model[0] == None:
        model[0] = tf.keras.models.load_model('Models/LSTM_BalancedTraining_GameHistoryBased_Quincy_Kris_Mrugesh')
        print("LSTM Model Loaded")
    
    if len(play_history) > 1000: 
        opponent_history.clear()
        play_history.clear()
        play_history.append('')
    opponent_history.append(prev_play)
    #print("Actual: " + prev_play) 
    guess = Get_Prediction_LSTM(model[0], opponent_history, play_history)
    #print(guess)
    play_history.append(guess)
    return guess

def Get_Prediction_DNN(model, player_history):
    keys = ['0','1','2']
    #format history for input
    input_eval = [RPS_encode(c) for c in player_history]
    input_eval = get_dist(input_eval, 2, keys)
    input_eval = normalise_dist(input_eval, 2, keys)
    RPS = {'R':[1,0,0],'P':[0,1,0],'S':[0,0,1]}
    input_eval = RPS[player_history[-1]] + input_eval
    
    #print(input_eval)
    
    input_eval = tf.expand_dims(input_eval, 0)
    
    #high temperature  => suprising output
    #low temperature => predictable output
    temperature = 0.1; 
    
    model.reset_states()
    
    prediction = model(input_eval)
    #prediction = tf.squeeze(prediction, 0)
    
    prediction = prediction / temperature
    predicted_id = tf.random.categorical(prediction, num_samples = 1)[-1,0].numpy()

    return RPS_decode(predicted_id)[0]


def DNN_player(prev_play, opponent_history = [], play_history = ['R'], model = [None]):
    #Load model if not loaded
    if model[0] == None:
        model[0] = tf.keras.models.load_model('Models/DNN_PlayerPastInputFrequency_Abbey')
        print("DNN Model Loaded")
    
    if len(play_history) > 1000: 
        opponent_history.clear()
        play_history.clear()
        play_history.append('R')

    opponent_history.append(prev_play)
    #print("Actual: " + prev_play) 
    guess = Get_Prediction_DNN(model[0], play_history)
    #print(guess)
    play_history.append(guess)
    return guess
