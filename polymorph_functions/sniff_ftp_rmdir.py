def sniff_ftp_rmdir(packet):

    # your code here
    try:        
        if packet["FTP"]["request.command"] == "RMD":
            print("RMD DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("HACIENDO CAMBIOS")
            packet["FTP"]["request.arg"] = "probando0"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            return packet
    except:
        return None
