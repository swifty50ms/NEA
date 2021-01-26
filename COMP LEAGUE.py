win_ars = ('Arsenal to win!!!')
win_asv = ('Aston Villa to win!!!')
win_bha = ('Brighton to win!!!')
win_bur = ('Burnley to win!!!')
win_che = ('Chelsea to win!!!')
win_cry = ('Crystal Palace to win!!!')
win_eve = ('Everton to win!!!')
win_ful = ('Fulham to win!!!')
win_lee = ('Leeds to win!!!')
win_lei = ('Leicester to win!!!')
win_liv = ('Liverpool to win!!!')
win_mc = ('Man City to win!!!')
win_mu = ('Man Utd to win!!!')
win_new = ('Newcastle to win!!!')
win_shu = ('Sheffield Utd to win!!!')
win_sou = ('Southampton to win!!!')
win_ths = ('Spurs to win!!!')
win_wba = ('West Brom to win!!!')
win_whu = ('West Ham to win!!!')
win_wol = ('Wolves to win!!!')
win_draw = ('A Draw!!!')
ars = ()
asv = ()
bha = ()
bur = ()
che = ()
cry = ()
eve = ()
ful = ()
lee = ()
lei = ()
liv = ()
mc = ()
mu = ()
new = ()
shu = ()
sou = ()
ths = ()
wba = ()
whu = ()
wol = ()

score = 0

#game 1
predict_game_1 = ()
predict_home_1 = (win_wol)
predict_draw = (win_draw)
predict_away_1 = (win_ths)
print('Wolves v Spurs')
home_game_1 = wol
away_game_1 = ths
print_home_1 = ('Wolves ')
print_away_1 = ('Spurs ')
#user input

try:
    home_game_1 = int(input(print_home_1))
    away_game_1 = int(input(print_away_1))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_1, home_game_1, "VS", away_game_1, print_away_1)


#game 2
predict_game_2 = ()
predict_home_2 = (win_liv)
predict_draw = (win_draw)
predict_away_2 = (win_wba)
print('Liverpool v West Brom')
home_game_2 = liv
away_game_2 = wba
print_home_2 = ('Liverpool ')
print_away_2 = ('West Brom ')
#user input

try:
    home_game_2 = int(input(print_home_2))
    away_game_2 = int(input(print_away_2))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_2, home_game_2, "VS", away_game_2, print_away_2)


#game 3
predict_game_3 = ()
predict_home_3 = (win_whu)
predict_draw = (win_draw)
predict_away_3 = (win_bha)
print('West Ham v Brighton')
home_game_3 = whu
away_game_3 = bha
print_home_3 = ('West Ham ')
print_away_3 = ('Brighton ')

#user input
try:
    home_game_3 = int(input(print_home_3))
    away_game_3 = int(input(print_away_3))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_3, home_game_3, "VS", away_game_3, print_away_3)

#game 4
predict_game_4 = ()
predict_home_4 = (win_lee)
predict_draw = (win_draw)
predict_away_4 = (win_bur)
print('Leeds v Burnley ')
home_game_4 = lee
away_game_4 = bur
print_home_4 = ('Leeds ')
print_away_4 = ('Burnley ')

#user input
try:
    home_game_4 = int(input(print_home_4))
    away_game_4 = int(input(print_away_4))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_4, home_game_4, "VS", away_game_4, print_away_4)

#game 5
predict_game_5 = ()
predict_home_5 = (win_mc)
predict_draw = (win_draw)
predict_away_5 = (win_new)
print('Man city v Newcastle')
home_game_5 = mc
away_game_5 = new
print_home_5 = ('Man city ')
print_away_5 = ('Newcastle ')

#user input
try:
    home_game_5 = int(input(print_home_5))
    away_game_5 = int(input(print_away_5))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_5, home_game_5, "VS", away_game_5, print_away_5)

#game 6
predict_game_6 = ()
predict_home_6 = (win_shu)
predict_draw = (win_draw)
predict_away_6 = (win_eve)
print('Sheffield v Everton')
home_game_6 = shu
away_game_6 = eve
print_home_6 = ('Sheffield ')
print_away_6 = ('Everton ')

#user input
try:
    home_game_6 = int(input(print_home_6))
    away_game_6 = int(input(print_away_6))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_6, home_game_6, "VS", away_game_6, print_away_6)

#game 7
predict_game_7 = ()
predict_home_7 = (win_ars)
predict_draw = (win_draw)
predict_away_7 = (win_che)
print('Arsenal V Chelsea')
home_game_7 = ars
away_game_7 = che
print_home_7 = ('Arsenal ')
print_away_7 = ('Chelsea ')

#user input
try:
    home_game_7 = int(input(print_home_7))
    away_game_7 = int(input(print_away_7))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_7, home_game_7, "VS", away_game_7, print_away_7)

#game 8
predict_game_8 = ()
predict_home_8 = (win_asv)
predict_draw = (win_draw)
predict_away_8 = (win_cry)
print('Villa v Palace')
home_game_8 = asv
away_game_8 = cry
print_home_8 = ('Villa ')
print_away_8 = ('Palace ')

#user input
try:
    home_game_8 = int(input(print_home_8))
    away_game_8 = int(input(print_away_8))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_8, home_game_8, "VS", away_game_8, print_away_8)

#game 9
predict_game_9 = ()
predict_home_9 = (win_ful)
predict_draw = (win_draw)
predict_away_9 = (win_sou)
print('Fulham v Southampton')
home_game_9 = ful
away_game_9 = sou
print_home_9 = ('Fulham ')
print_away_9 = ('Southampton ')

#user input
try:
    home_game_9 = int(input(print_home_9))
    away_game_9 = int(input(print_away_9))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_9, home_game_9, "VS", away_game_9, print_away_9)

#game 10
predict_game_10 = ()
predict_home_10 = (win_lei)
predict_draw = (win_draw)
predict_away_10 = (win_mu)
print('Leicester v Man Utd')
home_game_10 = lei
away_game_10 = mu
print_home_10 = ('Leicester ')
print_away_10 = ('Man Utd ')

#user input
try:
    home_game_10 = int(input(print_home_10))
    away_game_10 = int(input(print_away_10))
except ValueError:
    print("This is not a whole number.")
else:
    print("Your guess: ", print_home_10, home_game_10, "VS", away_game_10, print_away_10)

###################################################################################

print('game 1')
print("Your guess: ", print_home_1, home_game_1, "VS", away_game_1, print_away_1)
#calculating the winning team user prediction   
if away_game_1 > home_game_1:
    predict_game_1 = predict_away_1
if away_game_1 == home_game_1:
    predict_game_1 = predict_draw
if away_game_1 < home_game_1:
    predict_game_1 = predict_home_1
    
print(predict_game_1)


#manually input the correct score
################################################################
correct_home_1 = 1
correct_away_1 = 1
print("correct score: ", print_home_1, correct_home_1, "VS", correct_away_1, print_away_1)
###############################################################################
#who won
if correct_away_1 > correct_home_1:
    winning_team_1 = predict_away_1
    print(print_away_1, "won!!")
if correct_away_1 == correct_home_1:
    winning_team_1 = win_draw
    print("it was a draw!!")
if correct_away_1 < correct_home_1:
    winning_team_1 = predict_home_1
    print(print_home_1, "won!!")
    

#points for correct goals
if home_game_1 == correct_home_1:
    score = score + 1
    print('+1 for home goals')

if away_game_1 == correct_away_1:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_1 == winning_team_1:
    score = score + 3
    print('+3 for correct team')
    
if home_game_1 == correct_home_1 and away_game_1 == correct_away_1:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")




#######################################################################################################################
#game 2


#user input

print('game 2')
print("Your guess: ", print_home_2, home_game_2, "VS", away_game_2, print_away_2)
#calculating the winning team user prediction   
if away_game_2 > home_game_2:
    predict_game_2 = predict_away_2
if away_game_2 == home_game_2:
    predict_game_2 = predict_draw
if away_game_2 < home_game_2:
    predict_game_2 = predict_home_2
    
print(predict_game_2)


#manually input the correct score
################################################################
correct_home_2 = 1
correct_away_2 = 1
print("correct score: ", print_home_2, correct_home_2, "VS", correct_away_2, print_away_2)
###############################################################################
#who won
if correct_away_2 > correct_home_2:
    winning_team_2 = predict_away_2
    print(print_away_2, "won!!")
if correct_away_2 == correct_home_2:
    winning_team_2 = win_draw
    print("it was a draw!!")
if correct_away_2 < correct_home_2:
    winning_team_2 = predict_home_2
    print(print_home_2, "won!!")
    

#points for correct goals
if home_game_2 == correct_home_2:
    score = score + 1
    print('+1 for home goals')

if away_game_2 == correct_away_2:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_2 == winning_team_2:
    score = score + 3
    print('+3 for correct team')
    
if home_game_2 == correct_home_2 and away_game_2 == correct_away_2:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")

#######################################################################################################################
#game 3


#user input
print('game 3')
print("Your guess: ", print_home_3, home_game_3, "VS", away_game_3, print_away_3)


#calculating the winning team user prediction   
if away_game_3 > home_game_3:
    predict_game_3 = predict_away_3
if away_game_3 == home_game_3:
    predict_game_3 = predict_draw
if away_game_3 < home_game_3:
    predict_game_3 = predict_home_3
    
print(predict_game_3)


#manually input the correct score
################################################################
correct_home_3 = 2
correct_away_3 = 2
print("correct score: ", print_home_3, correct_home_3, "VS", correct_away_3, print_away_3)
###############################################################################
#who won
if correct_away_3 > correct_home_3:
    winning_team_3 = predict_away_3
    print(print_away_3, "won!!")
if correct_away_3 == correct_home_3:
    winning_team_3 = win_draw
    print("it was a draw!!")
if correct_away_3 < correct_home_3:
    winning_team_3 = predict_home_3
    print(print_home_3, "won!!")
    

#points for correct goals
if home_game_3 == correct_home_3:
    score = score + 1
    print('+1 for home goals')

if away_game_3 == correct_away_3:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_3 == winning_team_3:
    score = score + 3
    print('+3 for correct team')
    
if home_game_3 == correct_home_3 and away_game_3 == correct_away_3:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")


#game 4
#user input
print('game 4')
print("Your guess: ", print_home_4, home_game_4, "VS", away_game_4, print_away_4)


#calculating the winning team user prediction   
if away_game_4 > home_game_4:
    predict_game_4 = predict_away_4
if away_game_4 == home_game_4:
    predict_game_4 = predict_draw
if away_game_4 < home_game_4:
    predict_game_4 = predict_home_4
    
print(predict_game_4)


#manually input the correct score
################################################################
correct_home_4 = 1
correct_away_4 = 0
print("correct score: ", print_home_4, correct_home_4, "VS", correct_away_4, print_away_4)
###############################################################################
#who won
if correct_away_4 > correct_home_4:
    winning_team_4 = predict_away_4
    print(print_away_4, "won!!")
if correct_away_4 == correct_home_4:
    winning_team_4 = win_draw
    print("it was a draw!!")
if correct_away_4 < correct_home_4:
    winning_team_4 = predict_home_4
    print(print_home_4, "won!!")
    

#points for correct goals
if home_game_4 == correct_home_4:
    score = score + 1
    print('+1 for home goals')

if away_game_4 == correct_away_4:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_4 == winning_team_4:
    score = score + 3
    print('+3 for correct team')
    
if home_game_4 == correct_home_4 and away_game_4 == correct_away_4:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")

#game 5
#user input
print('game 5')
print("Your guess: ", print_home_5, home_game_5, "VS", away_game_5, print_away_5)


#calculating the winning team user prediction   
if away_game_5 > home_game_5:
    predict_game_5 = predict_away_5
if away_game_5 == home_game_5:
    predict_game_5 = predict_draw
if away_game_5 < home_game_5:
    predict_game_5 = predict_home_5
    
print(predict_game_5)


#manually input the correct score
################################################################
correct_home_5 = 2
correct_away_5 = 0
print("correct score: ", print_home_5, correct_home_5, "VS", correct_away_5, print_away_5)
###############################################################################
#who won
if correct_away_5 > correct_home_5:
    winning_team_5 = predict_away_5
    print(print_away_5, "won!!")
if correct_away_5 == correct_home_5:
    winning_team_5 = win_draw
    print("it was a draw!!")
if correct_away_5 < correct_home_5:
    winning_team_5 = predict_home_5
    print(print_home_5, "won!!")
    

#points for correct goals
if home_game_5 == correct_home_5:
    score = score + 1
    print('+1 for home goals')

if away_game_5 == correct_away_5:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_5 == winning_team_5:
    score = score + 3
    print('+3 for correct team')
    
if home_game_5 == correct_home_5 and away_game_5 == correct_away_5:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")

#game6
#user input
print('game 6')
print("Your guess: ", print_home_6, home_game_6, "VS", away_game_6, print_away_6)
#print("Your guess: ", print_home_5, home_game_5, "VS", away_game_5, print_away_5)

#calculating the winning team user prediction   
if away_game_6 > home_game_6:
    predict_game_6 = predict_away_6
if away_game_6 == home_game_6:
    predict_game_6 = predict_draw
if away_game_6 < home_game_6:
    predict_game_6 = predict_home_6
    
print(predict_game_6)


#manually input the correct score
################################################################
correct_home_6 = 0
correct_away_6 = 1
print("correct score: ", print_home_6, correct_home_6, "VS", correct_away_6, print_away_6)
###############################################################################
#who won
if correct_away_6 > correct_home_6:
    winning_team_6 = predict_away_6
    print(print_away_6, "won!!")
if correct_away_6 == correct_home_6:
    winning_team_6 = win_draw
    print("it was a draw!!")
if correct_away_6 < correct_home_6:
    winning_team_6 = predict_home_6
    print(print_home_6, "won!!")
    

#points for correct goals
if home_game_6 == correct_home_6:
    score = score + 1
    print('+1 for home goals')

if away_game_6 == correct_away_6:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_6 == winning_team_6:
    score = score + 3
    print('+3 for correct team')
    
if home_game_6 == correct_home_6 and away_game_6 == correct_away_6:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")

#game7
#user input
print('game 7')
print("Your guess: ", print_home_7, home_game_7, "VS", away_game_7, print_away_7)


#calculating the winning team user prediction   
if away_game_7 > home_game_7:
    predict_game_7 = predict_away_7
if away_game_7 == home_game_7:
    predict_game_7 = predict_draw
if away_game_7 < home_game_7:
    predict_game_7 = predict_home_7
    
print(predict_game_7)


#manually input the correct score
################################################################
correct_home_7 = 3
correct_away_7 = 1
print("correct score: ", print_home_7, correct_home_7, "VS", correct_away_7, print_away_7)
###############################################################################
#who won
if correct_away_7 > correct_home_7:
    winning_team_7 = predict_away_7
    print(print_away_7, "won!!")
if correct_away_7 == correct_home_7:
    winning_team_7 = win_draw
    print("it was a draw!!")
if correct_away_7 < correct_home_7:
    winning_team_7 = predict_home_7
    print(print_home_7, "won!!")
    

#points for correct goals
if home_game_7 == correct_home_7:
    score = score + 1
    print('+1 for home goals')

if away_game_7 == correct_away_7:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_7 == winning_team_7:
    score = score + 3
    print('+3 for correct team')
    
if home_game_7 == correct_home_7 and away_game_7 == correct_away_7:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")

#game8
#user input
print('game 8')
print("Your guess: ", print_home_8, home_game_8, "VS", away_game_8, print_away_8)


#calculating the winning team user prediction   
if away_game_8 > home_game_8:
    predict_game_8 = predict_away_8
if away_game_8 == home_game_8:
    predict_game_8 = predict_draw
if away_game_8 < home_game_8:
    predict_game_8 = predict_home_8
    
print(predict_game_8)


#manually input the correct score
################################################################
correct_home_8 = 3
correct_away_8 = 0
print("correct score: ", print_home_8, correct_home_8, "VS", correct_away_8, print_away_8)
###############################################################################
#who won
if correct_away_8 > correct_home_8:
    winning_team_8 = predict_away_8
    print(print_away_8, "won!!")
if correct_away_8 == correct_home_8:
    winning_team_8 = win_draw
    print("it was a draw!!")
if correct_away_8 < correct_home_8:
    winning_team_8 = predict_home_8
    print(print_home_8, "won!!")
    

#points for correct goals
if home_game_8 == correct_home_8:
    score = score + 1
    print('+1 for home goals')

if away_game_8 == correct_away_8:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_8 == winning_team_8:
    score = score + 3
    print('+3 for correct team')
    
if home_game_8 == correct_home_8 and away_game_8 == correct_away_8:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")


#game9
#user input
print('game 9')
print("Your guess: ", print_home_9, home_game_9, "VS", away_game_9, print_away_9)


#calculating the winning team user prediction   
if away_game_9 > home_game_9:
    predict_game_9 = predict_away_9
if away_game_9 == home_game_9:
    predict_game_9 = predict_draw
if away_game_9 < home_game_9:
    predict_game_9 = predict_home_9
    
print(predict_game_9)


#manually input the correct score
################################################################
correct_home_9 = 0
correct_away_9 = 0
print("correct score: ", print_home_9, correct_home_9, "VS", correct_away_9, print_away_9)
###############################################################################
#who won
if correct_away_9 > correct_home_9:
    winning_team_9 = predict_away_9
    print(print_away_9, "won!!")
if correct_away_9 == correct_home_9:
    winning_team_9 = win_draw
    print("it was a draw!!")
if correct_away_9 < correct_home_9:
    winning_team_9 = predict_home_9
    print(print_home_9, "won!!")
    

#points for correct goals
if home_game_9 == correct_home_9:
    score = score + 1
    print('+1 for home goals')

if away_game_9 == correct_away_9:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_9 == winning_team_9:
    score = score + 3
    print('+3 for correct team')
    
if home_game_9 == correct_home_9 and away_game_9 == correct_away_9:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")


#game 10
#user input
print('game 10')
print("Your guess: ", print_home_10, home_game_10, "VS", away_game_10, print_away_10)


#calculating the winning team user prediction   
if away_game_10 > home_game_10:
    predict_game_10 = predict_away_10
if away_game_10 == home_game_10:
    predict_game_10 = predict_draw
if away_game_10 < home_game_10:
    predict_game_10 = predict_home_10
    
print(predict_game_10)


#manually input the correct score
################################################################
correct_home_10 = 2
correct_away_10 = 2
print("correct score: ", print_home_10, correct_home_10, "VS", correct_away_10, print_away_10)
###############################################################################
#who won
if correct_away_10 > correct_home_10:
    winning_team_10 = predict_away_10
    print(print_away_10, "won!!")
if correct_away_10 == correct_home_10:
    winning_team_10 = win_draw
    print("it was a draw!!")
if correct_away_10 < correct_home_10:
    winning_team_10 = predict_home_10
    print(print_home_10, "won!!")
    

#points for correct goals
if home_game_10 == correct_home_10:
    score = score + 1
    print('+1 for home goals')

if away_game_10 == correct_away_10:
    score = score + 1
    print('+1 for away goals')
    
if predict_game_10 == winning_team_10:
    score = score + 3
    print('+3 for correct team')
    
if home_game_10 == correct_home_10 and away_game_10 == correct_away_10:
    score = score + 2
    print('+2 for perfect prediction')

print("Your score is: ", score, "points")


print('YOUR FINAL SCORE FOR THE WEEK IS:', score, 'points! WELL DONE!!')


