# WOLFSSH

Recherche de faille dans le code sftp Wolfssh .

How it works ?

start with setting up the environment :

python3 -m venv sftp_env
source sftp_env/bin/activate

If you do not yet have python install it using the following command:

sudo apt install python3-pip
sudo apt install python3.12-venv

Then, navigate to the wolfSSH build directory and execute the following command to start the SFTP server :

cd wolfssh-1.4.6-stable
examples/echoserver/echoserver -f

Then, navigate to the exploits directory and run a file using:

python <exploit_file_you_want_to_test>.py