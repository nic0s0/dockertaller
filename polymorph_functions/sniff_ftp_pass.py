def sniff_ftp_pass(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "PASS":
            print("PASS DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("HACIENDO CAMBIOS")
            packet["FTP"]["request.arg"] = "nopass"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            return packet
    except:
        return None
