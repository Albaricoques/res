import socket                                                                   
import threading                                                                
                                                                                
def server(conn, addr):                                                         
        while True:                                                             
                data = conn.recv(1024)                                          
                if not data or data == 'close' : break                          
                conn.send(data)                                                 
        conn.close()                                                            
                                                                                
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           
s.bind(('0.0.0.0',2222))                                                        
s.listen(10)                                                                    
while True:                                                                     
        conn, addr = s.accept()                                                 
        t = threading.Thread(target=server, args=(conn,addr))                   
        t.start()                                                               
                        