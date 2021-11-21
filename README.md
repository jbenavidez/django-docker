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


 
## 1 - T est everything before deploying to Ec2
#### Before deploy to ec2, make sure that you can run your docker-compose-pro.yml in your localmachine
```bash
$ docker-compose -f docker-compose-prod.yml build
$ docker-compose -f docker-compose-prod.yml  Up
```
![Alt text](/images/p1.png "test locally" )

## 2 -  generate Publick key from mac | you will need to add this public key to our ec2 machine on the creationion process
```bash
$ ssh-keygen -t rsa
$ pbcopy < ~/.ssh/id_rsa.pub
```

## 3 Connect to EC2 using ssh
```bash
$ ssh ec2-user@<your-ec2-machine-add>.amazonaws.com
 
```