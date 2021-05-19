import socket # importing library

ip = socket.gethostbyname (socket.gethostname()) # getting IP-Address of host(requester)

for port in range(65535): #Check for all available ports

    try:

        serv = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Create a new Socket

        serv.bind((ip,port)) #Bind socket with Address

    except:

        print('[OPEN] Port open:',port)
        # print('[OPEN] Port open :', port) #Print open port Number

serv.close() #Close Connection