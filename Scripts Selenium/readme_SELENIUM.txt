Pour le script Selenium, il existe 3 fichiers :
- script_canape.html
- script_lampe.html
- script_table.html
A chaque script l'achat de son objet.

Pour le lancer : 
	- Ouvrir et lancer la VM Ubuntu Server
	- Lancer dans la machine hôte Firefox.
	- Installer le plugin Selenium IDE
	- Redémarrer Firefox

	- Dans Firefox : Outils --> Selenium IDE
	- Dans Selenium : Fichiers --> Ajouter un cas de test...
		ouvrir ainsi les 3 fichiers cités au début du readme.

Pour la suite, installer les plugins Firefox :
	- FileLogging (pour créer un fichier log.txt)
	- SelBlocks (pour mettre des conditions dans les scripts)

Pour chacun des 3 fichiers :
	- le sélectionner en double-cliquant dessus
	- ensuite : Options --> Options --> FileLogging
		- Choisir un fichier .txt dans Log Fichier
		- Mettre "Info" pour File Logging Level

La configuration est terminée. Vous pouvez exécuter les scripts Sélénium !