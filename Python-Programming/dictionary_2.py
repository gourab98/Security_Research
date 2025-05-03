def network(servers):
    result = ""

    for hostname, IP_address in servers.items():
        
        result = result + "The IP address of the {} server is: {}".format(hostname,IP_address) + "\n"

    return result

print(network({"Domain Name Server":"8.8.8.8","Gateway Server":"192.168.1.1", "Print Server":"192.168.1.33","Mail Server":"192.168.1.190"}))