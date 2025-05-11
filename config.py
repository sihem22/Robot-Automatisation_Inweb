# Variables globales
import os

BROWSER = "chrome"

URL_inweb = "https://page-tests.botman.orangeportails.net/botmanTestPages/testPageBotman.html"

#JS_FILE= "script_preprod.js"
PROJET_PATH = os.path.dirname(os.path.abspath(__file__))
JS_FILE = os.path.join(PROJET_PATH, "Resources", "InWeb", "script_preprod.js")

# Langue : "FR" ou "EN"
Langue = "FR"



#${URL_Inweb-test}  http://dvfwcrun0b00004.nor.fr.gin.intraorange/testPageBotman/testPageBotman.html
#${headless}       	true
#${grid}           	false
#${PlatformType}   	web