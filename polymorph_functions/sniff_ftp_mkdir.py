def sniff_ftp_mkdir(packet):

    # your code here
    try:
        if packet["FTP"]["request.command"] == "MKD":
            print("MKD DETECTADO")
            print("request.arg =" + packet["FTP"]["request.arg"])
            ####################################################
            print("HACIENDO CAMBIOS")
            packet["FTP"]["request.arg"] = "probando0"
            print("request.arg =" + packet["FTP"]["request.arg"])
    # If the condition is meet
            return packet
    except:
        return None
    
