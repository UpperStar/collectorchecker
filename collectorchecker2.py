import httplib2
import os
from termcolor import colored, cprint
clear = lambda: os.system('cls')
clear()
cprint('\n    ███    █▄     ▄███████▄    ▄███████▄    ▄████████    ▄████████    ▄████████     ███        ▄████████    ▄████████ \n'
'    ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ▀█████████▄   ███    ███   ███    ███ \n'
'    ███    ███   ███    ███   ███    ███   ███    █▀    ███    ███   ███    █▀     ▀███▀▀██   ███    ███   ███    ███ \n'
'    ███    ███   ███    ███   ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀   ███            ███   ▀   ███    ███  ▄███▄▄▄▄██▀ \n'
'    ███    ███ ▀█████████▀  ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ▀███████████     ███     ▀███████████ ▀▀███▀▀▀▀▀   \n'
'    ███    ███   ███          ███          ███    █▄  ▀███████████          ███     ███       ███    ███ ▀███████████ \n'
'    ███    ███   ███          ███          ███    ███   ███    ███    ▄█    ███     ███       ███    ███   ███    ███ \n'
'    ████████▀   ▄████▀       ▄████▀        ██████████   ███    ███  ▄████████▀     ▄████▀     ███    █▀    ███    ███ \n'
'                                                        ███    ███                                         ███    ███ \n', 'green')
cprint('---------> JVC Collector Checker V1.0\n', 'green', 'on_red')

def check(pseudo):
	c = httplib2.Http('.cache')
	url = 'http://www.jeuxvideo.com/profil/' + pseudo + '?mode=infos'
	resp, content = c.request(url, 'GET', )
	if resp.status == 200:
		cprint(pseudo + ' est indisponible', 'red')
	else:
		cprint(pseudo + ' est disponible', 'green')

path = input('Chemin d\'accès du fichier ?')
cprint('Checking...', 'yellow')
with open(path) as f:
	for pseudo in f:
		check(pseudo.rstrip('\n').lower())
	
