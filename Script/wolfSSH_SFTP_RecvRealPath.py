import paramiko
import logging
# Activer les logs de débogage
#logging.basicConfig(level=logging.DEBUG)
# Détails de connexion
hostname = "127.0.0.1"
port = 22222
username = "jill"
password = "upthehill"

# Créer un client SFTP
transport = paramiko.Transport((hostname, port))
transport.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(transport)

sftp.normalize("../"+"a"*253)

# Lister les fichiers dans le répertoire racine
files = sftp.listdir('.')