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
<li>run " sudo amazon-linux-extras install  docker -y " to  install docker on the vm </li>

 
</ol>