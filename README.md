# chrimson.net

### Launch
Ubuntu Server 22.04 LTS (HVM), SSD Volume Type - ami-070650c005cce4203 (64-bit Arm) \
t4g.nano 2 vCPUs 0.5 GiB \
IAM chrimson.net AmazonEC2FullAccess AmazonS3FullAccess \
www.chrimson.net Tag Name \
default Security Group \
chrimson.net > chrimsonnet.pem Key Pair \
Allocate Elastc IP, Associate

Route 53, Create A Record

PuTTY 0.77 \
PuTTYgen, .pem > Private Key .ppk \
ubuntu@[Public IPv4] \
/etc/ssh/sshd_confg PubkeyAcceptedKeyTypes +ssh-rsa

### Install
sudo su - \
apt update \
apt install python3-pip \
pip install Flask \
apt install awscli \
apt install git

snap install core \
snap refresh core \
apt remove certbot \
snap install --classic certbot \
ln -s /snap/bin/certbot /usr/bin/certbot \
certbot certonly --standalone



### To Do:
ansible \
redirects \
wsgi \
boto3 \
gunicorn \
ec2, s3, iam, route53
