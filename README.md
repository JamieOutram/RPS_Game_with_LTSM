# RPS_Game_with_LTSM
My solution to the rock, paper scissors challenge on freeCodeCamp.org as part of the Machine Learning with Python Certification

Solved with 2 strategies:
	
 - LTSM_GameHistoryBased.ipynb - For Quincy, Kris and Mrugesh an LTSM model looking at both previous guesses and responses over the past 100 plays as inputs. This model was trained on a balanced dataset of ideal and random games against all players. 

	Produced Model: LSTM_BalancedTraining_GameHistoryBased_Quincy_Kris_Mrugesh

 - DNN_PastGuessFrequencyBased.ipynb - For abbey a DNN provided with the frequency of past guesses from current state normalised from 0-1 and the one hot encoded previous play as inputs. This model was trained against ideal and random games against abbey only.

	Produced Model: DNN_PlayerPastInputFrequency_Abbey

Run main.py for results

Output from last run:
LSTM Model Loaded
2021-09-02 14:04:25.588115: I tensorflow/stream_executor/cuda/cuda_dnn.cc:369] Loaded cuDNN version 8201
Final results: {'p1': 999, 'p2': 0, 'tie': 1}
Player 1 win rate: 100.0%
DNN Model Loaded
Final results: {'p1': 792, 'p2': 61, 'tie': 147}
Player 1 win rate: 92.84876905041031%
Final results: {'p1': 997, 'p2': 1, 'tie': 2}
Player 1 win rate: 99.8997995991984%
Final results: {'p1': 877, 'p2': 62, 'tie': 61}
Player 1 win rate: 93.39723109691161%

Note: The RPS_game.py file was only modified to fix a bug where abbey would remember all previously played games, the edit allows clearing of abbey's memory through a boolean option inbetween games
