import keyboard
import pyautogui as pg



POKE_DEAD_POSITION = (958, 516) 

LIST_ATTACK = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10']
BP_LOOT_POSITION = (1747, 1002)
cure = ['f8','f5']
taca_pokebola = ['tab']



def poke_attack():
    pg.press(LIST_ATTACK)
def get_loot():
    pg.sleep(0.2)
    pg.click(POKE_DEAD_POSITION, button='right')
    pg.sleep(0.8)
    pg.press(LIST_ATTACK)
    pg.click(BP_LOOT_POSITION, clicks=5)
    pg.press(LIST_ATTACK)
    pg.sleep(1.0)
    pg.click(POKE_DEAD_POSITION, button='right')
    pg.sleep(0.8)
    pg.press(LIST_ATTACK)
    pg.click(BP_LOOT_POSITION, clicks=5)
    pg.press(LIST_ATTACK)
    pg.sleep(1.0)
    pg.click(POKE_DEAD_POSITION, button='right')
    pg.sleep(0.8)
    pg.press(LIST_ATTACK)
    pg.click(BP_LOOT_POSITION, clicks=5)
    pg.press(LIST_ATTACK)
    pg.sleep(1.0)
    
    pg.press(taca_pokebola)
    pg.sleep(0.5)
    pg.click(POKE_DEAD_POSITION)
    pg.sleep(1.0)

   

def get_poke():
     pg.sleep(0.2)
     pg.press(taca_pokebola)
     pg.sleep(0.3)
     pg.click(POKE_DEAD_POSITION)
     pg.sleep(0.3)
     


while True:  
      poke_attack()
      get_loot()
      
         
       
      
       
    
    
        
                                 