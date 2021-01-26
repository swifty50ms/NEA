#Team stats for xG poisson distribution
import numpy as np
from matplotlib import pyplot as plt



#Total Home stats 20/21 season
total_home_gs = 232
total_home_matches = 170
avg_home_gs = total_home_gs / total_home_matches

#Total away stats 20/21 season
total_away_gs = 237
total_away_matches = 170
avg_away_gs = total_away_gs / total_away_matches



#1
#Arsenal
#Arsenal Home stats
ars_home_gs = 9
ars_home_gp = 9
ars_avg_home_gs = ars_home_gs / ars_home_gp

#Arsenal away stats
ars_away_gs = 11
ars_away_gp = 9
ars_avg_away_gs = ars_away_gs / ars_away_gp

#Arsenal Home Attack
ars_home_attack = ars_avg_home_gs / avg_home_gs
print('Arsenal Home Attack', ars_home_attack)

#Arsenal Away Attack
ars_away_attack = ars_avg_away_gs / avg_away_gs
print('Arsenal away attack', ars_away_attack)

#Arsenal Home Defence
ars_home_gc = 11
ars_avg_home_gc = ars_home_gc / ars_home_gp
ars_home_def = ars_avg_home_gc / avg_away_gs
print('Arsenal home defence', ars_home_def)

#Arsenal Away Defence
ars_away_gc = 8
ars_avg_away_gc = ars_away_gc / ars_away_gp
ars_away_def = ars_avg_away_gc / avg_home_gs
print('Arsenal away defence', ars_away_def)


#2
#Aston Villa
#Aston Villa Home stats
asv_home_gs = 15
asv_home_gp = 7
asv_avg_home_gs = asv_home_gs / asv_home_gp

#Aston Villa away stats
asv_away_gs = 14
asv_away_gp = 8
asv_avg_away_gs = asv_away_gs / asv_away_gp

#Aston Villa Home Attack
asv_home_attack = asv_avg_home_gs / avg_home_gs
print('Aston Villa Home Attack', asv_home_attack)

#Aston Villa Away Attack
asv_away_attack = asv_avg_away_gs / avg_away_gs
print('Aston Villa away attack', asv_away_attack)

#Aston Villa Home Defence
asv_home_gc = 11
asv_avg_home_gc = asv_home_gc / asv_home_gp
asv_home_def = asv_avg_home_gc / avg_away_gs
print('Aston Villa home defence', asv_home_def)

#Aston Villa Away Defence
asv_away_gc = 5
asv_avg_away_gc = asv_away_gc / asv_away_gp
asv_away_def = asv_avg_away_gc / avg_home_gs
print('Aston Villa away defence', asv_away_def)



#3
#Brighton
#Brighton Home stats
bri_home_gs = 10
bri_home_gp = 9
bri_avg_home_gs = bri_home_gs / bri_home_gp

#Brighton away stats
bri_away_gs = 11
bri_away_gp = 9
bri_avg_away_gs = bri_away_gs / bri_away_gp

#Brighton Home Attack
bri_home_attack = bri_avg_home_gs / avg_home_gs
print('Brighton Home Attack', bri_home_attack)

#Brighton Away Attack
bri_away_attack = bri_avg_away_gs / avg_away_gs
print('Brighton away attack', bri_away_attack)

#Brighton Home Defence
bri_home_gc = 15
bri_avg_home_gc = bri_home_gc / bri_home_gp
bri_home_def = bri_avg_home_gc / avg_away_gs
print('Brighton home defence', bri_home_def)

#Brighton Away Defence
bri_away_gc = 14
bri_avg_away_gc = bri_away_gc / bri_away_gp
bri_away_def = bri_avg_away_gc / avg_home_gs
print('Brighton away def', bri_away_def)

#4
#Burnley
#Burnley Home stats
bur_home_gs = 5
bur_home_gp = 8
bur_avg_home_gs = bur_home_gs / bur_home_gp

#Burnley away stats
bur_away_gs = 4
bur_away_gp = 8
bur_avg_away_gs = bur_away_gs / bur_away_gp

#Burnley Home Attack
bur_home_attack = bur_avg_home_gs / avg_home_gs
print('Burnley Home Attack', bur_home_attack)

#Burnley Away Attack
bur_away_attack = bur_avg_away_gs / avg_away_gs
print('Burnley away attack', bur_away_attack)

#Burnley Home Defence
bur_home_gc = 8
bur_avg_home_gc = bur_home_gc / bur_home_gp
bur_home_def = bur_avg_home_gc / avg_away_gs
print('Burnley home defence', bur_home_def)

#Burnley Away Defence
bur_away_gc = 13
bur_avg_away_gc = bur_away_gc / bur_away_gp
bur_away_def = bur_avg_away_gc / avg_home_gs
print('Burnley away def', bur_away_def)




#5
#Chelsea
#Chelsea Home stats
che_home_gs = 19
che_home_gp = 9
che_avg_home_gs = che_home_gs / che_home_gp

#Chelsea away stats
che_away_gs = 13
che_away_gp = 8
che_avg_away_gs = che_away_gs / che_away_gp

#Chelsea Home Attack
che_home_attack = che_avg_home_gs / avg_home_gs
print('Chelsea Home Attack', che_home_attack)

#Chelsea Away Attack
che_away_attack = che_avg_away_gs / avg_away_gs
print('Chelsea away attack', che_away_attack)

#Chelsea Home Defence
che_home_gc = 11
che_avg_home_gc = che_home_gc / che_home_gp
che_home_def = che_avg_home_gc / avg_away_gs
print('Chelsea home defence', che_home_def)

#Chelsea Away Defence
che_away_gc = 10
che_avg_away_gc = che_away_gc / che_away_gp
che_away_def = che_avg_away_gc / avg_home_gs
print('Chelsea away def', che_away_def)



#6
#Palace
#Palace Home stats
pal_home_gs = 11
pal_home_gp = 9
pal_avg_home_gs = pal_home_gs / pal_home_gp

#Palace away stats
pal_away_gs = 11
pal_away_gp = 9
pal_avg_away_gs = pal_away_gs / pal_away_gp

#Palace Home Attack
pal_home_attack = pal_avg_home_gs / avg_home_gs
print('Palace Home Attack', pal_home_attack)

#Palace Away Attack
pal_away_attack = pal_avg_away_gs / avg_away_gs
print('Palace away attack', pal_away_attack)

#Palace Home Defence
pal_home_gc = 15
pal_avg_home_gc = pal_home_gc / pal_home_gp
pal_home_def = pal_avg_home_gc / avg_away_gs
print('Palace home defence', pal_home_def)

#Palace Away Defence
pal_away_gc = 14
pal_avg_away_gc = pal_away_gc / pal_away_gp
pal_away_def = pal_avg_away_gc / avg_home_gs
print('Palace away defence', pal_away_def)


#7
#Everton
#Everton Home stats
eve_home_gs = 15
eve_home_gp = 8
eve_avg_home_gs = eve_home_gs / eve_home_gp

#Everton away stats
eve_away_gs = 13
eve_away_gp = 9
eve_avg_away_gs = eve_away_gs / eve_away_gp

#Everton Home Attack
eve_home_attack = eve_avg_home_gs / avg_home_gs
print('Everton Home Attack', eve_home_attack)

#Everton Away Attack
eve_away_attack = eve_avg_away_gs / avg_away_gs
print('Everton away attack', eve_away_attack)

#Everton Home Defence
eve_home_gc = 12
eve_avg_home_gc = eve_home_gc / eve_home_gp
eve_home_def = eve_avg_home_gc / avg_away_gs
print('Everton home defence', eve_home_def)

#Everton Away Defence
eve_away_gc = 9
eve_avg_away_gc = eve_away_gc / eve_away_gp
eve_away_def = eve_avg_away_gc / avg_home_gs
print('Everton away def', eve_away_def)


#8
#Fulham
#Fulham Home stats
ful_home_gs = 6
ful_home_gp = 8
ful_avg_home_gs = ful_home_gs / ful_home_gp

#Fulham away stats
ful_away_gs = 8
ful_away_gp = 8
ful_avg_away_gs = ful_away_gs / ful_away_gp

#Fulham Home Attack
ful_home_attack = ful_avg_home_gs / avg_home_gs
print('Fulham Home Attack', ful_home_attack)

#Fulham Away Attack
ful_away_attack = ful_avg_away_gs / avg_away_gs
print('Fulham away attack', ful_away_attack)

#Fulham Home Defence
ful_home_gc = 12
ful_avg_home_gc = ful_home_gc / ful_home_gp
ful_home_def = ful_avg_home_gc / avg_away_gs
print('Fulham home defence', ful_home_def)

#Fulham Away Defence
ful_away_gc = 12
ful_avg_away_gc = ful_away_gc / ful_away_gp
ful_away_def = ful_avg_away_gc / avg_home_gs
print('Fulham away def', ful_away_def)


#9
#Leeds
#Leeds Home stats
lee_home_gs = 13
lee_home_gp = 8
lee_avg_home_gs = lee_home_gs / lee_home_gp

#Leeds away stats
lee_away_gs = 17
lee_away_gp = 9
lee_avg_away_gs = lee_away_gs / lee_away_gp

#Leeds Home Attack
lee_home_attack = lee_avg_home_gs / avg_home_gs
print('Leeds Home Attack', lee_home_attack)

#Leeds Away Attack
lee_away_attack = lee_avg_away_gs / avg_away_gs
print('Leeds away attack', lee_away_attack)

#Leeds Home Defence
lee_home_gc = 13
lee_avg_home_gc = lee_home_gc / lee_home_gp
lee_home_def = lee_avg_home_gc / avg_away_gs
print('Leeds home defence', lee_home_def)

#Leeds Away Defence
lee_away_gc = 20
lee_avg_away_gc = lee_away_gc / lee_away_gp
lee_away_def = lee_avg_away_gc / avg_home_gs
print('Leeds away def', lee_away_def)


#10
#leicester
#leicester Home stats
lei_home_gs = 11
lei_home_gp = 8
lei_avg_home_gs = lei_home_gs / lei_home_gp

#leicster away stats
lei_away_gs = 20
lei_away_gp = 9
lei_avg_away_gs = lei_away_gs / lei_away_gp

#leicester Home Attack
lei_home_attack = lei_avg_home_gs / avg_home_gs
print('leicester Home Attack', lei_home_attack)

#leicester Away Attack
lei_away_attack = lei_avg_away_gs / avg_away_gs
print('leicester away attack', lei_away_attack)

#leicester Home Defence
lei_home_gc = 12
lei_avg_home_gc = lei_home_gc / lei_home_gp
lei_home_def = lei_avg_home_gc / avg_away_gs
print('leicester home defence', lei_home_def)

#leicester Away Defence
lei_away_gc = 9
lei_avg_away_gc = lei_away_gc / lei_away_gp
lei_away_def = lei_avg_away_gc / avg_home_gs
print('leicester away def', lei_away_def)


#11
#liverpool
#liverpool Home stats
liv_home_gs = 21
liv_home_gp = 8
liv_avg_home_gs = liv_home_gs / liv_home_gp

#liverpool away stats
liv_away_gs = 16
liv_away_gp = 9
liv_avg_away_gs = liv_away_gs / liv_away_gp

#liverpool Home Attack
liv_home_attack = liv_avg_home_gs / avg_home_gs
print('liverpool Home Attack', liv_home_attack)

#liverpool Away Attack
liv_away_attack = liv_avg_away_gs / avg_away_gs
print('liverpool away attack', liv_away_attack)

#liverpool Home Defence
liv_home_gc = 8
liv_avg_home_gc = liv_home_gc / liv_home_gp
liv_home_def = liv_avg_home_gc / avg_away_gs
print('liverpool home defence', liv_home_def)

#liverpool Away Defence
liv_away_gc = 13
liv_avg_away_gc = liv_away_gc / liv_away_gp
liv_away_def = liv_avg_away_gc / avg_home_gs
print('liverpool away def', liv_away_def)


#12
#Manchester City
#Manchester City Home stats
mnc_home_gs = 15
mnc_home_gp = 8
mnc_avg_home_gs = mnc_home_gs / mnc_home_gp

#Manchester City away stats
mnc_away_gs = 10
mnc_away_gp = 8
mnc_avg_away_gs = mnc_away_gs / mnc_away_gp

#Manchester City Home Attack
mnc_home_attack = mnc_avg_home_gs / avg_home_gs
print('Manchester City Home Attack', mnc_home_attack)

#Manchester City Away Attack
mnc_away_attack = mnc_avg_away_gs / avg_away_gs
print('Manchester City away attack', mnc_away_attack)

#Manchester City Home Defence
mnc_home_gc = 7
mnc_avg_home_gc = mnc_home_gc / mnc_home_gp
mnc_home_def = mnc_avg_home_gc / avg_away_gs
print('Manchester City home defence', mnc_home_def)

#Manchester City Away Defence
mnc_away_gc = 6
mnc_avg_away_gc = mnc_away_gc / mnc_away_gp
mnc_away_def = mnc_avg_away_gc / avg_home_gs
print('Manchester City away def', mnc_away_def)


#13
#Manchester Utd
#Manchester Utd Home stats
mnu_home_gs = 12
mnu_home_gp = 9
mnu_avg_home_gs = mnu_home_gs / mnu_home_gp

#Manchester Utd away stats
mnu_away_gs = 21
mnu_away_gp = 7
mnu_avg_away_gs = mnu_away_gs / mnu_away_gp

#Manchester Utd Home Attack
mnu_home_attack = mnu_avg_home_gs / avg_home_gs
print('Manchester Utd Home Attack', mnu_home_attack)

#Manchester Utd Away Attack
mnu_away_attack = mnu_avg_away_gs / avg_away_gs
print('Manchester Utd away attack', mnu_away_attack)

#Manchester Utd Home Defence
mnu_home_gc = 13
mnu_avg_home_gc = mnu_home_gc / mnu_home_gp
mnu_home_def = mnu_avg_home_gc / avg_away_gs
print('Manchester Utd home defence', mnu_home_def)

#Manchester Utd Away Defence
mnu_away_gc = 11
mnu_avg_away_gc = mnu_away_gc / mnu_away_gp
mnu_away_def = mnu_avg_away_gc / avg_home_gs
print('Manchester Utd away def', mnu_away_def)



#14
#Newcastle
#Newcastle Home stats
new_home_gs = 10
new_home_gp = 9
new_avg_home_gs = new_home_gs / new_home_gp

#Newcastle away stats
new_away_gs = 8
new_away_gp = 7
new_avg_away_gs = new_away_gs / new_away_gp

#Newcastle Home Attack
new_home_attack = new_avg_home_gs / avg_home_gs
print('Newcastle Home Attack', new_home_attack)

#Newcastle Away Attack
new_away_attack = new_avg_away_gs / avg_away_gs
print('Newcastle away attack', new_away_attack)

#Newcastle Home Defence
new_home_gc = 15
new_avg_home_gc = new_home_gc / new_home_gp
new_home_def = new_avg_home_gc / avg_away_gs
print('Newcastle home def', new_home_def)

#Newcastle Away Defence
new_away_gc = 11
new_avg_away_gc = new_away_gc / new_away_gp
new_away_def = new_avg_away_gc / avg_home_gs
print('Newcastle away def', new_away_def)



#15
#Sheff utd
#Sheff utd Home stats
shef_home_gs = 5
shef_home_gp = 9
shef_avg_home_gs = new_home_gs / new_home_gp

#Sheff utd away stats
shef_away_gs = 4
shef_away_gp = 9
shef_avg_away_gs = shef_away_gs / shef_away_gp

#Sheff utd Home Attack
shef_home_attack = shef_avg_home_gs / avg_home_gs
print('Sheff utd Home Attack', shef_home_attack)

#Sheff utd Away Attack
shef_away_attack = shef_avg_away_gs / avg_away_gs
print('Sheff utd away attack', shef_away_attack)

#Sheff utd Home Defence
shef_home_gc = 12
shef_avg_home_gc = shef_home_gc / shef_home_gp
shef_home_def = shef_avg_home_gc / avg_away_gs
print('Sheff utd home def', shef_home_def)

#Sheff utd Away Defence
shef_away_gc = 17
shef_avg_away_gc = shef_away_gc / shef_away_gp
shef_away_def = shef_avg_away_gc / avg_home_gs
print('Sheff utd away def', shef_away_def)


#16
#Southampton
#Southampton Home stats
sou_home_gs = 14
sou_home_gp = 9
sou_avg_home_gs = sou_home_gs / sou_home_gp

#Southampton away stats
sou_away_gs = 12
sou_away_gp = 8
sou_avg_away_gs = sou_away_gs / sou_away_gp

#Southampton Home Attack
sou_home_attack = sou_avg_home_gs / avg_home_gs
print('Southampton Home Attack', sou_home_attack)

#Southampton Away Attack
sou_away_attack = sou_avg_away_gs / avg_away_gs
print('Southampton away attack', sou_away_attack)

#Southampton Home Defence
sou_home_gc = 9
sou_avg_home_gc = sou_home_gc / sou_home_gp
sou_home_def = sou_avg_home_gc / avg_away_gs
print('Southampton home def', sou_home_def)

#Southampton Away Defence
sou_away_gc = 10
sou_avg_away_gc = sou_away_gc / sou_away_gp
sou_away_def = sou_avg_away_gc / avg_home_gs
print('Southampton away def', sou_away_def)


#17
#Spurs
#Spurs Home stats
ths_home_gs = 14
ths_home_gp = 9
ths_avg_home_gs = ths_home_gs / ths_home_gp

#Spurs away stats
ths_away_gs = 16
ths_away_gp = 8
ths_avg_away_gs = ths_away_gs / ths_away_gp

#Spurs Home Attack
ths_home_attack = ths_avg_home_gs / avg_home_gs
print('Spurs Home Attack', ths_home_attack)

#Spurs Away Attack
ths_away_attack = ths_avg_away_gs / avg_away_gs
print('Spurs away attack', ths_away_attack)

#Spurs Home Defence
ths_home_gc = 9
ths_avg_home_gc = ths_home_gc / ths_home_gp
ths_home_def = ths_avg_home_gc / avg_away_gs
print('Spurs home defence', ths_home_def)

#Spurs Away Defence
ths_away_gc = 7
ths_avg_away_gc = ths_away_gc / ths_away_gp
ths_away_def = ths_avg_away_gc / avg_home_gs
print('Spurs away def', ths_away_def)


#18
#West Brom
#West Brom Home stats
wba_home_gs = 5
wba_home_gp = 9
wba_avg_home_gs = wba_home_gs / wba_home_gp

#West Brom away stats
wba_away_gs = 6
wba_away_gp = 8
wba_avg_away_gs = wba_away_gs / wba_away_gp

#West Brom Home Attack
wba_home_attack = wba_avg_home_gs / avg_home_gs
print('West Brom Home Attack', wba_home_attack)

#West Brom Away Attack
wba_away_attack = wba_avg_away_gs / avg_away_gs
print('West Brom away attack', wba_away_attack)

#West Brom Home Defence
wba_home_gc = 24
wba_avg_home_gc = wba_home_gc / wba_home_gp
wba_home_def = wba_avg_home_gc / avg_away_gs
print('West Brom home defence', wba_home_def)

#West Brom Away Defence
wba_away_gc = 15
wba_avg_away_gc = wba_away_gc / wba_away_gp
wba_away_def = wba_avg_away_gc / avg_home_gs
print('West Brom away def', wba_away_def)


#19
#West Ham
#West Ham Home stats
whu_home_gs = 12
whu_home_gp = 8
whu_avg_home_gs = whu_home_gs / whu_home_gp

#West Ham away stats
whu_away_gs = 12
whu_away_gp = 9
whu_avg_away_gs = whu_away_gs / whu_away_gp

#West Ham Home Attack
whu_home_attack = whu_avg_home_gs / avg_home_gs
print('West Ham Home Attack', whu_home_attack)

#West Ham Away Attack
whu_away_attack = whu_avg_away_gs / avg_away_gs
print('West Ham away attack', whu_away_attack)

#West Ham Home Defence
whu_home_gc = 10
whu_avg_home_gc = whu_home_gc / whu_home_gp
whu_home_def = whu_avg_home_gc / avg_away_gs
print('West Ham home defence', whu_home_def)

#West Ham Away Defence
whu_away_gc = 11
whu_avg_away_gc = whu_away_gc / whu_away_gp
whu_away_def = whu_avg_away_gc / avg_home_gs
print('West Ham away def', whu_away_def)


#20
#Wolves
#Wolves Home stats
wol_home_gs = 10
wol_home_gp = 9
wol_avg_home_gs = wol_home_gs / wol_home_gp

#Wolves away stats
wol_away_gs = 9
wol_away_gp = 9
wol_avg_away_gs = wol_away_gs / wol_away_gp

#Wolves Home Attack
wol_home_attack = wol_avg_home_gs / avg_home_gs
print('Wolves Home Attack', wol_home_attack)

#Wolves Away Attack
wol_away_attack = wol_avg_away_gs / avg_away_gs
print('Wolves away attack', wol_away_attack)

#Wolves Home Defence
wol_home_gc = 10
wol_avg_home_gc = wol_home_gc / wol_home_gp
wol_home_def = wol_avg_home_gc / avg_away_gs
print('Wolves home defence', wol_home_def)

#Wolves Away Defence
wol_away_gc = 16
wol_avg_away_gc = wol_away_gc / wol_away_gp
wol_away_def = wol_avg_away_gc / avg_home_gs
print('Wolves away def', wol_away_def)





#friday
#Fixture 1
wol_xg = wol_home_attack * wba_away_def * avg_home_gs
wba_xg = wba_away_attack * wba_home_def * avg_away_gs
print('wol', wol_xg, 'Vs', 'wba', wba_xg)

#saturday
#Fixture 2
lee_xg = lee_home_attack * bri_away_def * avg_home_gs
bri_xg = bri_away_attack * lee_home_def * avg_away_gs
print('leeds', lee_xg, 'Vs', 'bri', bri_xg)

#Fixture 3
whu_xg = whu_home_attack * bur_away_def * avg_home_gs
bur_xg = bur_away_attack * whu_home_def * avg_away_gs
print('irons', whu_xg, 'Vs', 'burnley', bur_xg)

#Fixture 4
ful_xg = ful_home_attack * che_away_def * avg_home_gs
che_xg = che_away_attack * ful_home_def * avg_away_gs
print('ful', ful_xg, 'Vs', 'chelsea', che_xg)

#Fixture 5
lei_xg = lei_home_attack * sou_away_def * avg_home_gs
sou_xg = sou_away_attack * lei_home_def * avg_away_gs
print('lei', lei_xg, 'Vs', 'sou', sou_xg)

#sunday
#Fixture 6
shef_xg = shef_home_attack * ths_away_def * avg_home_gs
ths_xg = ths_away_attack * shef_home_def * avg_away_gs
print('shef', shef_xg, 'Vs', 'ths', ths_xg)

#Fixture 7
liv_xg = liv_home_attack * mnu_away_def * avg_home_gs
mnu_xg = mnu_away_attack * liv_home_def * avg_away_gs
print('liv', liv_xg, 'Vs', 'mu', mnu_xg)

#Fixture 8
mnc_xg = mnc_home_attack * pal_away_def * avg_home_gs
pal_xg = pal_away_attack * mnc_home_def * avg_away_gs
print('mc', mnc_xg, 'Vs', 'palace', pal_xg)

#Fixture 9
ars_xg = ars_home_attack * new_away_def * avg_home_gs
new_xg = new_away_attack * ars_home_def * avg_away_gs
print('arse', ars_xg, 'Vs', 'new', new_xg)

'''
#monday
#Fixture 10
bri_xg = bri_home_attack * sou_away_def * avg_home_gs
sou_xg = sou_away_attack * bri_home_def * avg_away_gs
print('brighton', bri_xg, 'Vs', 'southampton', sou_xg)

'''


#poisson distribution
shef_xg_pd = plt.hist(np.random.poisson(shef_xg, 100))
print(shef_xg_pd)
plt.grid()
plt.gca().set(title='shef');
plt.show()

ths_xg_pd = plt.hist(np.random.poisson(ths_xg, 100))
print(ths_xg_pd)
plt.grid()
plt.gca().set(title='ths');
plt.show()

