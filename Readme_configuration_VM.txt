1/ Importer la machine virtuelle Web Server.ova sous VirtualBox
2/ Cocher la case pour r�initialiser les MACs
3/ Cliquez sur la VM, puis sur Configuration > R�seau et changez le mode d'acc�s r�seau depuis NAT vers Acc�s par pont. Dans nom, s�lectionnez votre carte WiFi.
4/ Lancer la VM et se connecter � l'aide de l'identifiant "cassioressi" et du mot de passe "wordpresse"
5/ Dans /var/www/html/wp-config.php ajouter "
define('WP_HOME','http://<team>.ressi/');
define('WP_SITEURL','http://<team>.ressi/');" avec <team> = nom d'�quipe





