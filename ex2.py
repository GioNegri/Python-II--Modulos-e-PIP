import os

# 1 - Desligar o computador

#os.system("shutdown  /s") # desliga em 60s
#os.system("shutdown /s /t 0") #imediatamente

# 2 - cancelar desligamento

#os.system("shutdown /a")

def turn_off_one_hour():
    os.system("shutdown /s /t 3600")
    
def turn_off_half_an_hour():
    os.system("shutdown /s /t 1800")
    
def cancel_shutdown():
    os.system("shutdown /a ")
    
turn_off_half_an_hour()
cancel_shutdown()
