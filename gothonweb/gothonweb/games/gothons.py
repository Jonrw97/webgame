from gothonweb import planisphere
from random import randint
from gothonweb.user_interface import gothons_ui

central_corridor = planisphere.Room("Central Corridor",
                        gothons_ui.UI['central_corridor'])

laser_weapon_armory = planisphere.Room("Laser Weapon Armory",
                            gothons_ui.UI['laser_weapon_armory'])

the_bridge = planisphere.Room("The Bridge",
                    gothons_ui.UI['the_bridge'])

escape_pod = planisphere.Room("Escape Pod",
                    gothons_ui.UI['escape_pod'])

the_end_winner = planisphere.Room("The End",
                        gothons_ui.UI['the_end_winner'])

the_end_loser = planisphere.Room("The End",
                        gothons_ui.UI['the_end_loser'])

death = {
    1 : "You died.  You kinda suck at this.",
    2 : "Your Mom would be proud...if she were smarter.",
    3 : "Such a luser.",
    4 : "I have a small puppy that's better at this.",
    5 : "You're worse than your Dad's jokes."
}

generic_death = planisphere.Room("Game Over", death[randint(1,5)])

escape_pod.add_paths({
    '2': the_end_winner,
    '*': the_end_loser
})

the_bridge.add_paths({
    'throwbomb': generic_death,
    'placebomb': escape_pod
})

laser_weapon_armory.add_paths({
    '0123': the_bridge,
    '*' : generic_death
})

central_corridor.add_paths({
    'shootguard': generic_death,
    'dodgebullet': generic_death,
    'telljoke': laser_weapon_armory
})

START = central_corridor
START.add_paths({'START':central_corridor})