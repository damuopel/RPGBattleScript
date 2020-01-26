from classes.game import Person,bcolors

magic = [{'name':'Fire','cost':10,'dmg':100},
		 {'name':'Thunder','cost':10,'dmg':124},
		 {'name':'Blizzard','cost':10,'dmg':100}]

player = Person(460,65,60,34,magic)		
enemy = Person(1200,65,45,25,magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
	print('=========================')
	player.choose_action()
	index = int(input("Choose action:"))-1

	if index == 0:
		dmg = player.generate_damage()
		enemy.take_damage(dmg)
		print("You attacked for ",dmg," point of damage")
	elif index == 1:
		player.choose_magic()
		magic_choice = int(input("Choose magic:"))-1
		magic_dmg = player.generate_damage(magic_choice)
		spell = player.get_spell_name(magic_choice)
		cost = player.get_spell_mp_cost(magic_choice)

		current_mp = player.get_mp()

		if cost > current_mp:
			print(bcolors.FAIL+"\nNot enough MP\n" +bcolors.ENDC)
			continue

		plyer.reduce_mp(cost)
		enemy.take_damage(magic_dmg)
		print(bcolors.OKBLUE + '\n' + spell + " deals",str(magic_dmg),"points of damage" + bcolors.ENDC)

	enemy_choice = 1
	enemy_dmg = enemy.generate_damage()
	player.take_damage(enemy_dmg)
	print("Enemy attacks for ",enemy_dmg," point of damage")

	print("--------------------------------------")
	print("Enemy HP :" bcolors.FAIL + str(enemey.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

	print("Player HP :" bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
	print("Player MP :" bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC + "\n")

	if enemy.get_hp()==0:
		print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
		running = False
	else:
		print(bcolors.FAIL + "Your enemy has defeated you!" + bcolors.ENDC)
		running = False
