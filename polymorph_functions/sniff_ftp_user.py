def sniff_ftp_user(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "USER":
            print("USER DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("HACIENDO CAMBIOS")
            packet["FTP"]["request.arg"] = "nouser"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            return packet
    except:
        return None
