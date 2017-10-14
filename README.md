
		
Miner In The Middle
Author - Anthony Russell
@DotNetRussell

Not for illegal use!
(unless you own the network or have permission from everyone on it, it's illegal)
	 
	 
You will first need to make sure that you have `MitMf` and also `Twisted version 15.5.0`
To install dependencies run:
    ./miner_itm.sh --install
	
    ----To launch a standard miner attack----
	
    The standard network attack arp spoofs the network, then injects a miner into http responses.
    To launch a standard miner injection attack run:
    ./miner_itm.sh <coinhive api key> <gateway ip> <interface name>
	
	
    ----To launch a popup miner attack----
	
    A popup miner attack will attempt to inject a script into http responses. The script will wait for the user to click a button.
    When they do it will spawn a popup with their site in it and the origonal window will launch a miner. This is nice for persistence. 
	
    First run:
        ./miner_itm.sh --generate <coinhive api key>
	
    and place payload.html into your web server root directory
	
    Second run:
        ./miner_itm.sh -p <gateway ip> <interface name> <web server ip>
	
	

