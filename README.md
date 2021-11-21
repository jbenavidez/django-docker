# Django-docker-EC2
This project is used to show how we can connect our django app to a progres db on a docker enviroment, in addition, it show how we can run our dockerize app in a ec2 instance 



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
#### Before deploy to ec2, on your local machine, test  docker-compose-prod.yml to make sure everything work correctly 
```bash
$ docker-compose -f docker-compose-prod.yml build
$ docker-compose -f docker-compose-prod.yml  Up
```
![Alt text](/images/p1.png "test locally" )

## 2) Generate public key from mac | Register your key in aws, so you can add it   to your  ec2 instance on the creation process
```bash
$ ssh-keygen -t rsa
$ pbcopy < ~/.ssh/id_rsa.pub
```

## 3) Connect to EC2 using ssh
```bash
$ ssh ec2-user@<your-ec2-instance-add>.amazonaws.com
 
``` 

## 4) Install Depedencies in your EC2 instance 
<ol>
<li>run  "<b>sudo yum install git -y </b>" to install git in the VM, so we can clone the source code from github  </li>
<li>run " <b>sudo amazon-linux-extras install  docker -y </b>" to  install docker on the vm </li>
<li>run " <b>sudo systemctl enable docker.service </b>"  to enable docker services to start when we reboot the instance </li>
<li>run " <b>sudo systemctl start  docker.service</b>"to start docker </li>
<li>run " <b>sudo usermod -aG docker ec2-user</b>" to add 'ec2-user' to the docker-group, so the 'ec2-user can run the our project      </li>
<li>install docker-compose in ec2  
<ul>
<li> run <b>" sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose"</b> to install docker-compose in ec2</li>
<li> Get the above command from  <b>"https://docs.docker.com/compose/install/" </b> |linux tab </li>
 
</ul>
</li>
<li>run " <b>exit</b>"to applied the  update (you need to logout and login again in order to make it  ) </li>
<li>run " <b>ssh ec2-user@<your-ec2-machine-add>.amazonaws.com</b>"to login to your ec2 instance docker </li>
</ol>

## 5) Connect your ec2 instance to your repo
### Generate key for your ec2 instance | you will need a public key to conenct to your private repo
<ol>
<li>run  "<b>ssh-keygen -t ed25519 -b 4096</b>", this will generate a key, so we can add this key to our repo since our repo is private    </li>
<li>run " <b> cat ~/.ssh/id_ed25519.pub"</b>" to get the public key;   </li>
<li>On your repo under the settings ->deploy key, register paste the public key; after we add the deploy key, our ec2 instance should be able to connect to our github project </li>
</ol>

## 6) Add the project to our ec2 instance 
### On github  porject . click code  -> clone -->ssh and copy the link | is your repo is private your must 'ssh' otherwise it wont work 
<ul>
<li>run  "<b>git clone git@github.com:jbenavidez/django-docker-aws.git </b>"to clon the project   </li>
<li>run  "<b>cp .env.sample .env </b>" to create your env(this file store your environment varibles) </li>
<li>run  "<b>docker-compose -f docker-compose-prod.yml up -d</b>"  to run the app in your ee2 instane | the '-d' means to run in the background</li>
 
</ul>
### Result | open your ec2 add in your browser to see your app 

![Alt text](/images/p2.png "test locally" )
#### Make sure that you enabled "http port 80" request in your ec2 instance otherwise you will not be able to acces to your ec2 via browser

## 7) Push new udpate to your EC2 instance
<ul>
<li> push your local updates to your repo, we never code in our ec2 instance </li>
<li>run  "<b>git pull origin</b>"to  pull the lastest update   </li>
<li>run  "<b>docker-compose -f docker-compose-prod.yml build app </b>" to  rebuild the app  </li>
<li>run  "<b>docker-compose -f docker-compose-prod.yml up --no-deps -d app</b>"  to start the the containers </li>
</ul>

## 8) Extra 

<ul>
<li>run  "<b>docker-compose -f docker-compose-prod.yml run --rm app sh -c "python manage.py  "     </b>"to  run python command in your docker enviroment   </li>
 
</ul>
