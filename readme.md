credentials
aws cli // easiest and safest

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version

slava
security credentials
users
add users
CS_user_fil_rouge
programmatic access // Access key - Programmatic access
below create policy
Attach existing policies directly 
create policy button
chooce service
chooce s3 / comprehend
all actions
add ARN 
bucket name youtubecredtest
name the policy "youtubecredbucket"
back to another wdw w/ 5 steps, 
go to 5th step
access key

aws configure in cli
put access key
default region name  eu-central-1
output format json
launch code.py



more details on CLI
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

run

---
another way
iam in search line
users from left column
button right - add users
user name - admin
crocher on #Access key - Programmatic access
from 3 rectangles choose "Attach existing policies directly 
AdministratorAccess
next: tags
next: review
create user
copy and past "Access key ID" and "Secret access key 