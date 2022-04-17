"""Pratical no. 3
Aim: Study and implementation of Infrastructure as a Service
Objective: From this experiment, the student will be able to,
.Understand the concepts of virtualization and to use cloud as       IAAS
       .Learn the technique
       .Understand the importance of this technique.
Outcome:
	The learner will able to 
	.to match the industry requirements of Database management,
	Programming and networking with limited infrastructure
	.to analyze the local and global impact of computing on    individuals.
	  .to use current techniques,skills and tools necessary for computing practice.
Procedure:
	Add user useradd –s/bin/bash –d/opt/stack –m
	Stack apt-get install sudo –y
	Echo ‘stack ALL=(ALL) NOPASSWD:ALL’>>/etc/sudo
	Login as stack user
Download DevStack
	Sudoapt-getinstallgit –y sudoyuminstall –ygit
	Gitclonehttps://git.openstack.org/openstack-dev/devstack cddevstack
Run DevStack
Create local.conf
Set FLOATING_RANGE
Set FIXED RANGE
Set FIXED NETWORK SIZE
Set FLAT INTERFACE

Local.conf should look like this:
	[[local|localrc]]
	FLOATING_RANGE=192.168.1.224/27
	FIXED_RANGE=10.11.12.0/24
	FIXED_NETWORK_SIZE=256
	FLAT INTERFACE= eth0
	ADMIN PASSWORD =SUPERSECRET
	DATABASE PASSWORD =IHEARTDATABASE
	RABBIT_PASSWORD=FLOPYSYMOPSY
	SERVICE_PASSWORD=IHEARTKSL
Run Devstack
Conclusion:
We have installed Ubuntu as bare and implemented it.it provides acess to computing resources in a virtual environment. With the help of iaas we can build our own it platform. 
"""