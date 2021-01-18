#Damage calculator for the Legend of Zelda: Breath of the Wild

import math

baseDamage = 0 #base weapon damage
attackModifier = 0 #attack up modifier
attackUp = 0 #attack up level multiplier
enemyBonus = 0 #bonus damage vs guardians
setBonus = 0 #ancient proficiency/bone attack up
critHit = 0 #critical hit/sneakstrike/headshot/shatter
elementalDamage = 0 #elemental damage

def main():
	baseDamage = int(input('Enter Base Damage\n'))
	attackModifier = int(input('Enter Attack Up Modifier\n'))
	attackUp = float(attackUpMult(int(input('Enter Attack Up Level (0 if None)\n'))))

	weaponType = int(int(input('Is Weapon Guardian/Ancient/Bone (0 = Neither, 1 = Guardian, 2 = Ancient, 3 = Bone)\n')))
	if weaponType == 1 or weaponType == 2:
		enemyBonus = float(enemyBonusMult(weaponType))
		ancientProf = input('With Ancient Proficiency (y/n)\n')
		if ancientProf.upper() == 'Y':
			setBonus = 0.8
	elif weaponType == 3:
		enemyBonus = 0
		boneAttack = input('With Bone Attack Up (y/n)\n')
		if boneAttack.upper() == 'Y':
			setBonus = 0.8
	else:
		enemyBonus = 0
		setBonus = 0

	critHit = int(critical(int(input('0 = None, 1 = Critical Hit, 2 = Sneakstrike, 3 = Shatter\n'))))

	if critHit != 3 and critHit != 8: #Sneakstrike and Shatter ovveride Elemental Damage
		elementalDamage = elemental()
	else:
		elementalDamage = 0

	totalDamage = baseDamage + attackModifier
	totalDamage = totalDamage + (totalDamage * attackUp)
	totalDamage = totalDamage + (totalDamage * enemyBonus)
	totalDamage = math.floor(totalDamage + (totalDamage * setBonus))
	if critHit != 0:
		totalDamage = totalDamage * critHit
	totalDamage += elementalDamage

	print('Total Damage: ' + str(int(totalDamage)))
	print()

def attackUpMult(level):
	if level == 1:
		return 0.2
	elif level == 2:
		return 0.3
	elif level == 3:
		return 0.5
	else:
		return 0

def enemyBonusMult(weaponType):
	guardian = input('Is Enemy a Guardian/Blight/Ganon (y/n)\n')
	if guardian.upper() == 'Y':
		if weaponType == 1:
			return 0.3
		elif weaponType == 2:
			return 0.5
	else:
		return 0

def critical(crit):
	if crit == 1:
		return 2
	elif crit == 2:
		return 8
	elif crit == 3:
		return 3
	else:
		return 0

def elemental():
	element = int(input('Enter Weapon Element (0 - None, 1 - Fire, 2 - Ice, 3 - Electric\n'))
	if element == 0:
		return 0
	immune = input('Is Enemy Immune to Elemental Damage (y/n)\n')
	if immune.upper() == 'Y':
		return 0
	enemyState = int(input('Is Enemy under Elemental Damage Already (0 - None, 1 - Fire, 2 - Ice, 3 - Electric)\n'))
	if enemyState == element:
		return 0

	if element == 1 or element == 2:
		return 10
	if element == 3:
		return 20

def reset():
	baseDamage = 0 #base weapon damage
	attackModifier = 0 #attack up modifier
	attackUp = 0 #attack up level multiplier
	enemyBonus = 0 #bonus damage vs guardians
	setBonus = 0 #ancient proficiency/bone attack up
	critHit = 0 #critical hit/sneakstrike/headshot/shatter
	elementalDamage = 0 #elemental damage

while 1 == 1:
	main()
	reset()