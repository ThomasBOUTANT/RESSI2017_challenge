Pour le script Selenium, il existe 3 fichiers :
- script_canape.html
- script_lampe.html
- script_table.html
A chaque script l'achat de son objet.

Pour le lancer : 
	- Ouvrir et lancer la VM Ubuntu Server
	- Lancer dans la machine h�te Firefox.
	- Installer le plugin Selenium IDE
	- Red�marrer Firefox

	- Dans Firefox : Outils --> Selenium IDE
	- Dans Selenium : Fichiers --> Ajouter un cas de test...
		ouvrir ainsi les 3 fichiers cit�s au d�but du readme.

Pour la suite, installer les plugins Firefox :
	- FileLogging (pour cr�er un fichier log.txt)
	- SelBlocks (pour mettre des conditions dans les scripts)

Pour chacun des 3 fichiers :
	- le s�lectionner en double-cliquant dessus
	- ensuite : Options --> Options --> FileLogging
		- Choisir un fichier .txt dans Log Fichier
		- Mettre "Info" pour File Logging Level

La configuration est termin�e. Vous pouvez ex�cuter les scripts S�l�nium !