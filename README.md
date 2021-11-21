# Django-docker-ECE
This project is used to show how to deploy an dockerize django app on an EC2 machine 


## Stack
<ul>
<li>Django</li>
<li>Docker </li>
<li>ec2 </li>
<li>S3 </li>
<li>posgress </li>
<li>nginx </li>
</ul>


 
## 1) Test everything before deploying to Ec2
#### Before deploy to ec2, make sure that you can run your docker-compose-pro.yml in your localmachine
```bash
$ docker-compose -f docker-compose-prod.yml build
$ docker-compose -f docker-compose-prod.yml  Up
```
![Alt text](/images/p1.png "test locally" )

## 2) generate Publick key from mac | you will need to add this public key to our ec2 machine on the creationion process
```bash
$ ssh-keygen -t rsa
$ pbcopy < ~/.ssh/id_rsa.pub
```

## 3) Connect to EC2 using ssh
```bash
$ ssh ec2-user@<your-ec2-machine-add>.amazonaws.com
 
``` 

## 4) Install Depedencies in your EC2 machine 
<ol>
<li>run  "<b>sudo yum install git -y </b>" to install git in the VM, so we can clone the source code from github  </li>
<li>run " <b>sudo amazon-linux-extras install  docker -y </b>" to  install docker on the vm </li>
<li>run " <b>sudo systemctl enable docker.service </b>"  to enable docker services to start when we reboot the machine </li>
<li>run " <b>sudo systemctl start  docker.service</b>"to start docker </li>
<li>run " <b>sudo usermod -aG docker ec2-user</b>" to add 'ec2-user' to the docker-group, so the 'ec2-user can run the our project      </li>
<li>install docker-compose in ec2  
<ul>
<li> run <b>" sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose"</b> to install docker-compose in ec2</li>
<li> Get the above command from  <b>"https://docs.docker.com/compose/install/" </b> |linux tab </li>
 
</ul>
</li>
</ol>