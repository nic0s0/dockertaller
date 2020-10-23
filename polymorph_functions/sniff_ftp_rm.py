def sniff_ftp_rm(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "DELE":
            print("DELE DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("HACIENDO CAMBIOS")
            packet["FTP"]["request.arg"] = "hola.txt"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            return packet
    except:
        return None
