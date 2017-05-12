from cofee import CApplication
from cofee import Menubar
from cofee import SubMenu
from cofee.lib import stc

app = CApplication(800, 600, "Cofee Test")
stcWid = stc.StyledTextControl(app, 800, 600, "Consolas", 12) # Text Box
stcWid.pack()
app.exe()
