# Installing Hadoop 3.0.3 on Linux Mint

## 1 Prerequisites
Hadoop is a big data storage and analytics framework that is built on top of the Java TM platform and runs on the Java Virtual Machine. Thus installation of JDK is a must.

### Installing JDK 8
1. Open terminal and type the following command to add Oracle's PPA,

`$ sudo add-apt-repository ppa:webupd8team/java`
`$ sudo apt-get update`

2. Now go on and install JDK 8 on your Machine
`$ udo apt-get install oracle-java8-installer`

### Setting JAVA_HOME environment Variable and Adding Java to your PATH

1. Open terminal and go to home directory.

`$ cd ~`

2. Now open the .bashrc file in your preferred text editor (I am using gedit)

`$ gedit .bashrc`

3. Add the following lines to the bottom of your .bashrc

![alt text](/img/img1.png)