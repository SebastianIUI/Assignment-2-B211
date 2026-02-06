import numpy as np
import os

csv_path = os.path.join(os.path.expanduser('~'), 'Downloads', 'players_stats_by_season_full_details.csv')

data = np.genfromtxt(csv_path, delimiter=',', skip_header=1, dtype=str, invalid_raise=False,ndmin=2,)


Field_Goal_Accuracy = data[:,8].astype(float)
print("Field Goal Accuracy:", Field_Goal_Accuracy)

Free_Throw_Accuracy = data[:,10].astype(float)
print("Free Throw Accuracy:", Free_Throw_Accuracy)

Three_Point_Accuracy = data[:,12].astype(float)
print("Three Point Accuracy:", Three_Point_Accuracy)

Average_Points = data[:, 21].astype(float) / data[:, 6].astype(float)
print("Average Points scored by minute:", Average_Points)

Shooting_Accuracy = (Field_Goal_Accuracy + Free_Throw_Accuracy + Three_Point_Accuracy) / 3
print("Shooting Accuracy:", Shooting_Accuracy)

Average_Blocks = data[:, 20].astype(float) / data[:, 5].astype(float)
print("Average Blocks per game:", Average_Blocks)

Average_Steals = data[:, 19].astype(float) / data[:,5].astype(float)
print("Average Steals per game:", Average_Steals)

Player_Names = data[:,1]

Season = data[:,3]	


Top_100_Field = np.argsort(Field_Goal_Accuracy)[-100:][::-1] 
print("Top 100 players based on Field Goal Accuracy:", Top_100_Field, Player_Names[Top_100_Field], Season[Top_100_Field], Field_Goal_Accuracy[Top_100_Field])	

Top_100_Throw = np.argsort(Free_Throw_Accuracy)[-100:][::-1] 
print("Top 100 players based on Free Throw Accuracy:", Top_100_Throw, Player_Names[Top_100_Throw], Season[Top_100_Throw], Free_Throw_Accuracy[Top_100_Throw])	

Top_100_Three = np.argsort(Three_Point_Accuracy)[-100:][::-1] 
print("Top 100 players based on Three Point Accuracy:", Top_100_Three, Player_Names[Top_100_Three], Season[Top_100_Three], Three_Point_Accuracy[Top_100_Three])	

Top_100_Average = np.argsort(Average_Points)[-100:][::-1] 
print("Top 100 players based on Average Points scored by minute:", Top_100_Average, Player_Names[Top_100_Average], Season[Top_100_Average], Average_Points[Top_100_Average])	

Top_100_Shooting = np.argsort(Shooting_Accuracy)[-100:][::-1] 
print("Top 100 players based on Shooting Accuracy:", Top_100_Shooting, Player_Names[Top_100_Shooting], Season[Top_100_Shooting], Shooting_Accuracy[Top_100_Shooting])	

Top_100_Blocks = np.argsort(Average_Blocks)[-100:][::-1] 
print("Top 100 players based on Average Blocks per game:", Top_100_Blocks, Player_Names[Top_100_Blocks], Season[Top_100_Blocks], Average_Blocks[Top_100_Blocks])	

Top_100_Steals = np.argsort(Average_Steals)[-100:][::-1] 
print("Top 100 players based on Average Steals per game:", Top_100_Steals, Player_Names[Top_100_Steals], Season[Top_100_Steals], Average_Steals[Top_100_Steals])

