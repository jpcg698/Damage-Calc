from pickle import FALSE
import tkinter as tk
from tkinter import HORIZONTAL, ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")
        self.title('Damage Calc')

        # initialize data
        self.class_options = ('Fighter', 'Barbarian', 'Rogue')
        self.ac_category_options = ('Low', 'Moderate', 'High','Extreme')
        self.dice_options = ('1d4','1d6','1d8','1d10','1d12')
        self.damage_progression = {
            "Fighter":{
                1:{
                "attack_bonus":9,
                "damage_bonus":4},
                2:{
                "attack_bonus":11,
                "damage_bonus":4},
                3:{
                "attack_bonus":12,
                "damage_bonus":4},
                4:{
                "attack_bonus":13,
                "damage_bonus":4},
                5:{
                "attack_bonus":16,
                "damage_bonus":4},
                6:{
                "attack_bonus":17,
                "damage_bonus":4},
                7:{
                "attack_bonus":18,
                "damage_bonus":7},
                8:{
                "attack_bonus":19,
                "damage_bonus":7},
                9:{
                "attack_bonus":20,
                "damage_bonus":7},
                10:{
                "attack_bonus":23,
                "damage_bonus":8},
                11:{
                "attack_bonus":24,
                "damage_bonus":8},
                12:{
                "attack_bonus":25,
                "damage_bonus":8},
                13:{
                "attack_bonus":28,
                "damage_bonus":9},
                14:{
                "attack_bonus":29,
                "damage_bonus":9},
                15:{
                "attack_bonus":30,
                "damage_bonus":13},
                16:{
                "attack_bonus":32,
                "damage_bonus":13},
                17:{
                "attack_bonus":33,
                "damage_bonus":13},
                18:{
                "attack_bonus":34,
                "damage_bonus":13},
                19:{
                "attack_bonus":35,
                "damage_bonus":13},
                20:{
                "attack_bonus":37,
                "damage_bonus":14}
            },
            "Barbarian":{
                1:{
                "attack_bonus":7,
                "damage_bonus":10},
                2:{
                "attack_bonus":9,
                "damage_bonus":10},
                3:{
                "attack_bonus":10,
                "damage_bonus":10},
                4:{
                "attack_bonus":11,
                "damage_bonus":10},
                5:{
                "attack_bonus":14,
                "damage_bonus":10},
                6:{
                "attack_bonus":15,
                "damage_bonus":10},
                7:{
                "attack_bonus":16,
                "damage_bonus":16},
                8:{
                "attack_bonus":17,
                "damage_bonus":16},
                9:{
                "attack_bonus":18,
                "damage_bonus":16},
                10:{
                "attack_bonus":21,
                "damage_bonus":17},
                11:{
                "attack_bonus":22,
                "damage_bonus":17},
                12:{
                "attack_bonus":23,
                "damage_bonus":17},
                13:{
                "attack_bonus":26,
                "damage_bonus":18},
                14:{
                "attack_bonus":27,
                "damage_bonus":18},
                15:{
                "attack_bonus":28,
                "damage_bonus":29},
                16:{
                "attack_bonus":30,
                "damage_bonus":29},
                17:{
                "attack_bonus":31,
                "damage_bonus":29},
                18:{
                "attack_bonus":32,
                "damage_bonus":29},
                19:{
                "attack_bonus":33,
                "damage_bonus":29},
                20:{
                "attack_bonus":35,
                "damage_bonus":30}
                
                },
            "Rogue":{
                1:{
                "attack_bonus":9,
                "damage_bonus":4},
                2:{
                "attack_bonus":11,
                "damage_bonus":4},
                3:{
                "attack_bonus":12,
                "damage_bonus":4},
                4:{
                "attack_bonus":13,
                "damage_bonus":4},
                5:{
                "attack_bonus":16,
                "damage_bonus":4},
                6:{
                "attack_bonus":17,
                "damage_bonus":4},
                7:{
                "attack_bonus":18,
                "damage_bonus":7},
                8:{
                "attack_bonus":19,
                "damage_bonus":7},
                9:{
                "attack_bonus":20,
                "damage_bonus":7},
                10:{
                "attack_bonus":23,
                "damage_bonus":8},
                11:{
                "attack_bonus":24,
                "damage_bonus":8},
                12:{
                "attack_bonus":25,
                "damage_bonus":8},
                13:{
                "attack_bonus":28,
                "damage_bonus":9},
                14:{
                "attack_bonus":29,
                "damage_bonus":9},
                15:{
                "attack_bonus":30,
                "damage_bonus":13},
                16:{
                "attack_bonus":32,
                "damage_bonus":13},
                17:{
                "attack_bonus":33,
                "damage_bonus":13},
                18:{
                "attack_bonus":34,
                "damage_bonus":13},
                19:{
                "attack_bonus":35,
                "damage_bonus":13},
                20:{
                "attack_bonus":37,
                "damage_bonus":14},
                }
        }
        self.ac_progression = {
            "Low":{
             0:15,
             1:15,
             2:17,
             3:18,
             4:20,
             5:21,
             6:23,
             7:24,
             8:26,
             9:27,
             10:29,
             11:30,
             12:32,
             13:33,
             14:35,
             15:36,
             16:38,
             17:39,
             18:41,
             19:42,
             20:44,
             21:45,
             22:47,
             23:48,
             24:50
            },
            "Moderate":{
             0:15,
             1:15,
             2:17,
             3:18,
             4:20,
             5:21,
             6:23,
             7:24,
             8:26,
             9:27,
             10:29,
             11:30,
             12:32,
             13:33,
             14:35,
             15:36,
             16:38,
             17:39,
             18:41,
             19:42,
             20:44,
             21:45,
             22:47,
             23:48,
             24:50
            },
            "High":{
             0:15,
             1:15,
             2:17,
             3:18,
             4:20,
             5:21,
             6:23,
             7:24,
             8:26,
             9:27,
             10:29,
             11:30,
             12:32,
             13:33,
             14:35,
             15:36,
             16:38,
             17:39,
             18:41,
             19:42,
             20:44,
             21:45,
             22:47,
             23:48,
             24:50
            },
            "Extreme":{
             0:15,
             1:15,
             2:17,
             3:18,
             4:20,
             5:21,
             6:23,
             7:24,
             8:26,
             9:27,
             10:29,
             11:30,
             12:32,
             13:33,
             14:35,
             15:36,
             16:38,
             17:39,
             18:41,
             19:42,
             20:44,
             21:45,
             22:47,
             23:48,
             24:50
            }
        }
        # set up variable
        self.selected_class = tk.StringVar(self)
        self.selected_level = tk.IntVar(self)
        self.selected_level.set(1)
        self.selected_enemy_ac_category = tk.StringVar(self)
        self.selected_enemy_level = tk.IntVar(self)
        self.selected_enemy_level.set(1)
        self.selected_weapon_dice = tk.StringVar(self)

        # create widget
        self.create_wigets()

    def create_wigets(self):
        # padding for widgets using the grid layout
        paddings = {'padx': 5, 'pady': 5}

        # class label
        class_label = ttk.Label(self,  text='Select a class to calculate damage:')
        class_label.grid(column=0, row=0, sticky=tk.W, **paddings)

        # class option menu
        class_menu = ttk.OptionMenu(
            self,
            self.selected_class,
            self.class_options[0],
            *self.class_options)

        class_menu.grid(column=1, row=0, sticky=tk.W, **paddings)

        # label level
        level_label = ttk.Label(self,  text='Select a level for your class:')
        level_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        # level option menu
        level_menu = ttk.Spinbox(
            self, from_=1, to= 20, textvariable=self.selected_level)

        level_menu.grid(column=1, row=1, sticky=tk.W, **paddings)

        # enemy ac label
        class_label = ttk.Label(self,  text='Select enemy AC category:')
        class_label.grid(column=0, row=2, sticky=tk.W, **paddings)

        # enemy ac class option menu
        class_menu = ttk.OptionMenu(
            self,
            self.selected_enemy_ac_category,
            self.ac_category_options[0],
            *self.ac_category_options)

        class_menu.grid(column=1, row=2, sticky=tk.W, **paddings)

        # label enemy level
        enemy_level_label = ttk.Label(self,  text='Select a level for your enemy:')
        enemy_level_label.grid(column=0, row=3, sticky=tk.W, **paddings)

        # level enemy option menu
        enemy_level_menu = ttk.Spinbox(
            self, from_=1, to= 20, textvariable=self.selected_enemy_level)

        enemy_level_menu.grid(column=1, row=3, sticky=tk.W, **paddings)

        # label
        dice_label = ttk.Label(self,  text='Select a weapon dice:')
        dice_label.grid(column=0, row=4, sticky=tk.W, **paddings)

        # option menu
        dice_menu = ttk.OptionMenu(
            self,
            self.selected_weapon_dice,
            self.dice_options[0],
            *self.dice_options)

        dice_menu.grid(column=1, row=4, sticky=tk.W, **paddings)

        # output Button
        results_button = ttk.Button(self,text="Get Results", command=self.getResults)
        results_button.grid(column=0,row=5,sticky=tk.W, **paddings)

        #hit output label
        self.hit_bonus_label = ttk.Label(self, foreground='red')
        self.hit_bonus_label.grid(column=1, row=5, sticky=tk.W, **paddings)

        # output label
        self.damage_bonus_label = ttk.Label(self, foreground='red')
        self.damage_bonus_label.grid(column=1, row=6, sticky=tk.W, **paddings)

        # output label
        self.ac_label = ttk.Label(self, foreground='red')
        self.ac_label.grid(column=1, row=7, sticky=tk.W, **paddings)

        # output label
        self.hit_label = ttk.Label(self, foreground='red')
        self.hit_label.grid(column=1, row=8, sticky=tk.W, **paddings)
        
        # output label
        self.crithit_label = ttk.Label(self, foreground='red')
        self.crithit_label.grid(column=1, row=9, sticky=tk.W, **paddings)

        # output label
        self.damage_label = ttk.Label(self, foreground='red')
        self.damage_label.grid(column=1, row=10, sticky=tk.W, **paddings)
        
        # output label
        self.crit_label = ttk.Label(self, foreground='red')
        self.crit_label.grid(column=1, row=11, sticky=tk.W, **paddings)
        
        # output label
        self.results_button = ttk.Label(self, foreground='red')
        self.results_button.grid(column=1, row=12, sticky=tk.W, **paddings)
        

    def getResults(self, *args):
        selectedClass = self.selected_class.get()
        selectedLevel = self.selected_level.get()
        selectedDice = self.selected_weapon_dice.get()
        selectedEnemyLevel = self.selected_enemy_level.get()
        selectedAcCategory= self.selected_enemy_ac_category.get()
        toHitBonus = self.damage_progression[selectedClass][selectedLevel]["attack_bonus"]
        damageBonus = self.damage_progression[selectedClass][selectedLevel]["damage_bonus"]
        enemyAc = self.ac_progression[selectedAcCategory][selectedEnemyLevel]
        diferenceToHit = enemyAc - toHitBonus
        if (diferenceToHit >=30):
            chanceToCrit = 0
            chanceToHit = 0
            chanceToMiss = 20
        elif (diferenceToHit >20):
            chanceToCrit = 0
            chanceToHit = 1
            chanceToMiss = 19
        elif (diferenceToHit == 20):
            chanceToCrit = 1
            chanceToHit = 0
            chanceToMiss = 19
        elif (diferenceToHit >= 10):
            chanceToCrit = 1
            hitFloor = 20-diferenceToHit
            chanceToHit = hitFloor
            chanceToMiss = (diferenceToHit-1)
        elif (diferenceToHit > 1):
            chanceToCrit = (20-(10+diferenceToHit-1))
            chanceToHit = 10
            chanceToMiss = 20-chanceToCrit-chanceToHit
        elif (diferenceToHit > -9):
            chanceToCrit = (20-(10+diferenceToHit-1))
            chanceToMiss = 1
            chanceToHit = 20-chanceToCrit-chanceToMiss
        else:
            chanceToCrit = 19
            chanceToHit = 1
            chanceToMiss = 0

        if(selectedLevel >= 19):
            multiplier = 4
        elif(selectedLevel >= 12):
            multiplier = 3
        elif(selectedLevel >= 4):
            multiplier = 2
        else:
            multiplier = 1

        match selectedDice:
            case "1d4":
                averageDamage = 2.5
            case "1d6":
                averageDamage = 3.5
            case "1d8":
                averageDamage = 4.5
            case "1d10":
                averageDamage = 5.5
            case "1d12":
                averageDamage = 6.5
            case _:
                averageDamage = 0

        normalDamage = multiplier * (averageDamage + damageBonus)
        critDamage = 2* normalDamage
        totalDamage = ((normalDamage * chanceToHit) + (critDamage * chanceToCrit))/20
        #hitDifference = self.damage_progression.get()[self.selected_class.get()[self.selected_level.get()]["attack_bonus"]]
        self.hit_bonus_label['text'] = f'Hit bonus: {toHitBonus}'
        self.damage_bonus_label['text'] = f'damage bonus: {damageBonus}'
        self.ac_label['text'] = f'Enemy Ac: {enemyAc}'
        self.hit_label['text'] = f'Chance to hit: {chanceToHit}'
        self.crithit_label['text'] = f'Chance to crit: {chanceToCrit}'
        self.damage_label['text'] = f'Damage: {normalDamage}'
        self.crit_label['text'] = f'Crit Damage: {critDamage}'
        self.results_button['text'] = f'Average Damage: {totalDamage}'


if __name__ == "__main__":
    app = App()
    app.mainloop()