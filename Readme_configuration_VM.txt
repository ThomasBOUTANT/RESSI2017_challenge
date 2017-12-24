1/ Importer la machine virtuelle Web Server.ova sous VirtualBox
2/ Cocher la case pour réinitialiser les MACs
3/ Cliquez sur la VM, puis sur Configuration > Réseau et changez le mode d'accès réseau depuis NAT vers Accès par pont. Dans nom, sélectionnez votre carte WiFi.
4/ Lancer la VM et se connecter à l'aide de l'identifiant "cassioressi" et du mot de passe "wordpresse"
5/ Dans /var/www/html/wp-config.php ajouter "
define('WP_HOME','http://<team>.ressi/');
define('WP_SITEURL','http://<team>.ressi/');" avec <team> = nom d'équipe





