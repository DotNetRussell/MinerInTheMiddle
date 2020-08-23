Miner In The Middle  
Author: Anthony Russell  
Twitter: @DotNetRussell  
Blog: https://www.DotNetRussell.com  
  
Not for illegal use!  
(unless you own the network or have permission from everyone on it, it's illegal)  
	 
INTRO:  
  
Miner in the Middle is a script that allows you to inject javascript miners into targets on your local network. It does this using python, scapy and netfilterqueue. When you run the application, it will automatically configure your iptables and setup packet forwarding for you. The only things you need to do are run setup, start your arpspoofing and run the application.   
	   
TO USE:	  
  
Make sure to configure your config.json file before attempting to use the application.     
    
You'll find a sample_config.json in this repo. You really only need two things in this config file.  
  
1. You're going to need to go to minero.cc - register an account - and get a public key. You'll put this public key in the config.json file under "site-key"  
2. The second thing you'll want to do is put in an ip constraint. This constraint prevents unintentional injection to targets outside of your scope.   
If my target ips are in the 192.168.1.0 through 192.168.1.255 then in the config.json `ipConstraint` field, I would put `192.168.1`   
  
BONUS: if you have your own js file you'd rather inject into people instead of the minero.cc miner, then in the config file, put the path of your js file in the `customInjection` field  
  
You will first need to make sure that you have the required python dependencies    
    
To install dependencies run:  
        `./setup.sh`  
	
   ----To launch a standard miner attack----
	
   The standard network attack arp spoofs the network, then injects a miner into http responses.
   To launch a standard miner injection attack run:
      ` ./mineritm.py /path/to/your/config.json`
	

   ----To launch a custom js injection attack----

   You only need to create the js file and modify the config.json file. The config.json property for customInjection should be the path to your custom js file


   ----To launch a popunder attack----

   You'll need to configure a couple things for this. First, the config file should have the attacker ip filled in as well as the palyoad name. This just needs to be a file that you're hosting on your attacking box. For example, if I'm running an apache server at 192.168.1.10 and it's hosting the html file I want to display as my pop under and it's called test.html, then the attacker ip in the config file would be 192.168.1.10 and the payload name would be test.html  

   Also, please make sure to start your server :-)  


	
	

