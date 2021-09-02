# RPS_Game_with_LTSM
My solution to the rock, paper scissors challenge on free code camp 

Solved with 2 strategies:
	LTSM_GameHistoryBased.ipynb - For Quincy, Kris and Mrugesh an LTSM model looking at both previous guesses and responses over the past 100 plays as inputs. This model was trained on a balanced dataset of ideal and random games against all players. 
		Produced Model: LSTM_BalancedTraining_GameHistoryBased_Quincy_Kris_Mrugesh
	DNN_PastGuessFrequencyBased.ipynb - For abbey a DNN provided with the frequency of past guesses from current state normalised from 0-1 and the one hot encoded previous play as inputs. This model was trained against ideal and random games against abbey only.
		Produced Model: DNN_PlayerPastInputFrequency_Abbey

run main.py for results

Note: The RPS_game.py file was only modified to fix a bug where abbey would remember all previously played games, the edit allows clearing of abbey's memory through a boolean option inbetween games