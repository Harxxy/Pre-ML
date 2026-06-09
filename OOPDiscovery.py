import random

difficulty = 0
difficulty_list = ["goblin", "goblin", "goblin", "orc", "orc", "orc", "goblin", "dragon", "orc", "dragon", "dragon", "dragon"]

class Character:

    def __init__(self, name, hp, max_hp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.xp = 0
        self.level = 1
    
    def take_damage(self, amt, stunned, penetrated):
        if amt == 0:
            actual_damage = 0
            print("Attack failed, leading to 0 damage.")
        elif penetrated:
            actual_damage = amt
        else:
            actual_damage = max(1, amt - self.defense)
        if self.hp <= actual_damage:
            self.hp = 0
        else:
            self.hp -= actual_damage
        return actual_damage, stunned
    
    def is_alive(self):
        return self.hp > 0
    
    def heal(self):
        self.hp += 30
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def basic_attack(self):
        return (self.attack, False, False)
    
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= 100:
            self.xp -= 100
            self.level += 1
            self.heal()
            print(f"{self.name} leveled up and healed!")
            self.max_hp *= 1.05
            self.max_hp = int(self.max_hp)
            self.attack += 1
            self.defense += 1
            if self.archetype == "mage":
                self.mana += 50

    def __str__(self):
        return f"{self.name} | HP : {self.hp}/{self.max_hp} | ATT : {self.attack} | DEF : {self.defense} | LVL : {self.level} | XP : {self.xp}/100"

class Warrior(Character):

    def __init__(self, name, hp = 120, max_hp = 120, attack = 35, defense = 30):
        super().__init__(name, hp, max_hp, attack, defense)
        self.archetype = "warrior"
        self.bash_cooldown = 0
    
    def attack_set(self):
        print(" 1. Sword Strike (Base Attack)")
        if self.bash_cooldown == 0:
            print(" 2. Shield Bash (1.5x Base Attack)")
        else:
            print(" 2. Shield Bash (On Cooldown)")

    def special_attack(self):
        if self.bash_cooldown == 0:
            a = random.randint(1, 10)
            damage = int((1.5*self.attack)//1)
            enemy_stunned = (a < 4)
            self.bash_cooldown += 2
            ignores_armor = False
            return damage, enemy_stunned, ignores_armor
        else:
            return (0, False, False)

class Mage(Character):

    def __init__(self, name, hp = 80, max_hp = 80, attack = 50, defense = 15):
        super().__init__(name, hp, max_hp, attack, defense)
        self.archetype = "mage"
        self.mana = 100

    def __str__(self):
        return f"Mage {self.name} | HP : {self.hp}/{self.max_hp} | ATT : {self.attack} | DEF : {self.defense} | MANA : {self.mana} | LVL : {self.level} | XP : {self.xp}/100"

    def attack_set(self):
        print(" 1. Wand Strike (Base Attack)")
        if self.mana >= 20:
            print(" 2. Fireball (2x Base Attack)")
        else:
            print(" 2. Fireball (Insufficient Mana)")

    def special_attack(self):
        if self.mana >= 20:
            damage = 2*self.attack
            enemy_stunned = False
            self.mana -= 20
            ignores_armor = False
            return damage, enemy_stunned, ignores_armor
        else:
            print("You try to conjure a fireball but do not have sufficient mana.")
            return (0, False, False)

class Ranger(Character):

    def __init__(self, name, hp = 100, max_hp = 100, attack = 40, defense = 20):
        super().__init__(name, hp, max_hp, attack, defense)
        self.archetype = "ranger"
        self.precise_shot_cooldown = 0

    def attack_set(self):
        print(" 1. Shoot (Base Attack)")
        if self.precise_shot_cooldown == 0:
            print(" 2. Precise Shot (Ignores armor)")
        else:
            print(" 2. Precise Shot (On Cooldown)")

    def special_attack(self):
        damage = self.attack
        if self.precise_shot_cooldown == 0:
            ignores_armor = True
            enemy_stunned = False
            self.precise_shot_cooldown += 1
            return damage, enemy_stunned, ignores_armor
        else:
            return (damage, False, False)

class Enemy(Character):

    def __init__(self, name, hp, max_hp, attack, defense, xp_reward):
        super().__init__(name, hp, max_hp, attack, defense)
        self.xp_reward = xp_reward


    def __str__(self):
        return f"{self.name} | HP : {self.hp}/{self.max_hp} | ATT : {self.attack} | DEF : {self.defense}"

    @staticmethod

    def enemy(enemy_string):
        if enemy_string == "goblin":
            return Enemy("Goblin", 30, 30, 12, 0, 10)
        elif enemy_string == "orc":
            return Enemy("Orc", 60, 60, 24, 10, 30)
        elif enemy_string == "dragon":
            return Enemy("Dragon", 90, 90, 48, 20, 60)
        else:
            print("No such enemy found.")

def goblin_intro():
    input("You push open the castle gates. The air smells of dust, old wood, and forgotten gold.          ")
    input("The entrance hall stretches before you — grand columns, cobwebs the size of fishing nets...    ")
    input("And paintings. Magnificent ones. Kings and queens of a bygone era staring down at you.        ")
    input("You lean in to admire one particularly stern-looking fellow above the fireplace...             ")
    input("Extraordinary brushwork. Really. The shadow on his left cheek alone must have taken weeks—    ")
    input("                        *a tiny crash from behind the curtain*                                 ")
    input("...You turn slowly.                                                                            ")
    input("A small, green, deeply unimpressive creature tumbles out from behind the drapes.              ")
    input("It bares its teeth. Three of them.                                                             ")
    input("It raises what appears to be a sharpened stick.                                               ")
    input("It lets out what it clearly intended to be a fearsome war cry.                                ")
    input("                        *it sounds like a sneeze*                                              ")
    input("...A Goblin. You were almost ambushed by a Goblin.                                            ")
    input("It looks as surprised to see you as you are disappointed to see it.                           ")
    input("Well. No sense being rude about it. The thing did try.                                        ")

def orc_intro():
    input("You step over the goblin — gently, it's already had a rough day — and press deeper into the castle. ")
    input("The second floor is darker. The ceilings higher. The cobwebs... significantly more ambitious.       ")
    input("You pass an overturned table. Then a wall with a fist-sized hole in it.                            ")
    input("Then another hole. Then what appears to be a hole shaped vaguely like a person.                    ")
    input("You begin to sense a theme.                                                                        ")
    input("The growl reaches you before the smell does. Which is saying something.                            ")
    input("It lumbers out of the shadows — seven feet of bad posture, worse hygiene, and apparent purpose.   ")
    input("An Orc. A proper one. It looks at you the way most people look at a problem they intend to solve  ")
    input("with their fists.                                                                                  ")
    input("It cracks its knuckles. All of them. Twice.                                                       ")
    input("Somewhere in that tiny skull, a thought is forming. It hasn't arrived yet, but it's trying.       ")
    input("You ready yourself. The Goblin was an embarrassment. This... this is an actual fight.              ")

def dragon_intro():
    input("The throne room doors are taller than any doors have a right to be.                               ")
    input("You push them open anyway. Heroism is largely just doing unreasonable things with confidence.      ")
    input("The room is vast. Gold everywhere — coins, chalices, candlesticks, things you can't name.         ")
    input("Beautiful, really. You take a moment to appreciate it.                                            ")
    input("Then the pile of gold moves.                                                                      ")
    input("Not all of it. Just... a significant portion. A horded, breathing, sighing portion.               ")
    input("One enormous eye opens. Then the other. Both find you immediately.                               ")
    input("The Dragon does not scramble. It does not snarl. It simply... regards you.                        ")
    input("Like a chess player who's already seen twelve moves ahead and finds the whole thing mildly sad.  ")
    input("It exhales once through its nose. A small flame escapes, almost apologetically.                  ")
    input("Then it speaks. Low, slow, and terribly calm:                                                    ")
    input("'Another one.'                                                                                    ")
    input("Just that. Two words. Like it's done this before. Many times. And found it tiresome.             ")
    input("You grip your weapon.                                                                             ")
    input("The Dragon tilts its enormous head, as if genuinely curious whether you'll be interesting.       ")
    input("No pressure.                                                                                      ")

def congratulations_message():
    input("\nPress Enter to hear from our special guest...")
    print("\nWell I'll be damned... FOUR Goblins? FOUR Orcs? And FOUR Dragons?!")
    
    input("\nPress Enter to continue...")
    print("In my 84 years I have never seen such slaughter. My grandson fought ONE Goblin in '97. We don't talk about '97.")
    
    input("\nPress Enter to continue...")
    print("You know, when I was your age, we didn't HAVE heroes like you. We had Gerald. Gerald tripped over a Goblin and that was the end of that.")
    
    input("\nPress Enter to continue...")
    print("FOUR Dragons. Do you understand what you've done? The SMELL alone should have killed you. I once stood near a Dragon and lost three toes. THREE.")
    
    input("\nPress Enter to continue...")
    print("I want you to know, young one, that this victory means everything. To me. To this village. To Gerald's memory. To my three remaining toes.")
    
    input("\nPress Enter to continue...")
    print("You have restored honour to these lands and I — I just — my heart is so full right now I could just—")
    
    input("\nPress Enter to continue...")
    print("...hm.")
    print("...hm.")
    print("...anyway you should probably loot the Dragons. All four of them.")
    print("\n*dies*")
    print("*the cause of death is later reported as 'too much honour witnessed in one sitting'*")

def fight(enemy_string):
    monster = Enemy.enemy(enemy_string)
    monster_stunned = False
    while player.is_alive() and monster.is_alive():
        print("                                                                                                                             ")
        print(player.__str__())
        print("                                                                                                                         ")
        print(monster.__str__())
        print("                                                                                                                         ")

        player.attack_set()
        player_attack_choice = input("Enter your move(1/2): ")

        while True:
            if player_attack_choice == "1":
                damage, stunned, penetrated = player.basic_attack()
                damage_dealt, monster_stunned = monster.take_damage(damage, stunned, penetrated)
                print(f"You strike {monster.name} for {damage_dealt} damage.")
                if player.archetype == "warrior":
                    player.bash_cooldown = max(0, player.bash_cooldown - 1)
                elif player.archetype == "ranger":
                    player.precise_shot_cooldown = max(0, player.precise_shot_cooldown - 1)
                if monster_stunned:
                    print(f"{monster.name} is stunned!")
                break
            elif player_attack_choice == "2":
                damage, stunned, penetrated = player.special_attack()
                damage_dealt, monster_stunned = monster.take_damage(damage, stunned, penetrated)
                if player.archetype == "warrior":
                    print(f"You slam your shield into {monster.name} for {damage_dealt} damage!")
                elif player.archetype ==  "mage":
                    print(f"You hurl a fireball at {monster.name} for {damage_dealt} damage!")
                elif player.archetype == "ranger":
                    if player.precise_shot_cooldown > 0:
                        print(f"You try lining up a precise shot, but fail and deal {damage_dealt} damage to {monster.name}.")
                    else:
                        print(f"You line up a precise shot on {monster.name} for {damage_dealt} damage!")
                if monster_stunned:
                    print(f"{monster.name} is stunned!")
                break
            else:
                print("Invalid input. Try again.")
                player_attack_choice = input("Enter your move(1/2): ")
        
        print("                                                                                                     ")
        if monster.is_alive():
            input("Press Enter to Continue")
            if monster_stunned:
                print(f"{monster.name} is stunned and skips their turn!")
                print("                                                                                                             ")
                monster_stunned = False
            else:
                damage, stunned, penetrated = monster.basic_attack()
                damage_dealt, _ = player.take_damage(damage, stunned, penetrated)  
                print(f"{monster.name} strikes you for {damage_dealt} damage.")
                print("                                                                                             ")

        else:
            print(f"{monster.name} has been defeated!")
            player.gain_xp(monster.xp_reward)
            
    if not player.is_alive():
        print(f"You have been slain by {monster.name}. Game over.")
       
print("You venture into the abandoned castle to get hold of the enormous treasures within only to be stormed by hordes of monsters...")
input("                                                                                                                              ")
player_name = input("Enter name: ")
print("1. Warrior       2. Mage        3. Ranger")

while True:
    player_class_choice = input("Pick a class(1/2/3): ")
    player_class_choice.replace(" ", "")
    if player_class_choice == "1":
        player = Warrior(player_name)
        print("A bold Warrior eh?")
        input("Hah! The classic choice of those who prefer their thinking done BEFORE the battle... ")
        input("Big shield, bigger gut, and a heart to match. Can't say it's elegant, but it gets the job done. ")
        input("Your Shield Bash can stun enemies — land it right and the poor fool won't know what hit him. Literally. ")
        input("Press on, you magnificent oaf.                                                                          ")
        break
    elif player_class_choice == "2":
        player = Mage(player_name)
        print("The way of the Mage...")
        input("Ah... yes. Of course. The Mage. *clears throat nervously*                                    ")
        input("Fragile as parchment, but do NOT let that fool you. I've seen a Mage reduce an Orc to cinders with a look. ")
        input("Your Fireball costs 20 mana — spend it wisely. Once the well runs dry, you're just an angry person in a robe. ")
        input("I'll... just stand over here. Out of range. No offence, your worship.                                         ")
        break
    elif player_class_choice == "3":
        player = Ranger(player_name)
        print("The humble bow and arrow...")
        input("Ah, a Ranger! Good. Reliable. The kind of person you actually want watching your back.       ")
        input("Not the flashiest path, but there's a quiet wisdom in it. Balanced stats, steady hands.     ")
        input("Your Precise Shot ignores enemy armor entirely — doesn't matter how thick their hide is.    ")
        input("I always liked Rangers. Salt of the earth. Now go show them what patience looks like.       ")
        break
    else:
        print("Eh? What was that? I couldn't hear ya.")

input("Right then. The castle awaits. Try not to die on the first floor, it'd be terribly embarrassing. ")

while player.is_alive():
    if difficulty == 0:
        goblin_intro()
    elif difficulty == 3:
        orc_intro()
        player.heal()
    elif difficulty == 7:
        dragon_intro()
        player.heal()
    elif difficulty == 12:
        congratulations_message()
        print(player)
        print("You win!")
        break
    else:
        player.heal()
    fight(difficulty_list[difficulty])
    difficulty += 1
