import pyautogui as pd
import time

time.sleep(3)

pd.PAUSE = 1.5

pd.write('git init')
pd.press('enter')
pd.write('git add .')
pd.press('enter')
pd.write("git commit -m 'commit automático'")
pd.press('enter')
pd.write('git branch -M main')
pd.press('enter')
pd.write('git remote add origin https://github.com/Luisfrva13/envio.git')
pd.press('enter')
pd.write('git push -u origin main')




