import socket

# Declare Host IP and Port
port = 53
ip = '127.0.0.1'

# Change "socket.SOCK_DGRAM" for "socket.SOCK_STREAM" for use TCP instead of UDP  
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Accept only one paramether, thats why the double parenthesis
sock.bind((ip, port))


def getflags(flags):
    byte1 = bytes(flags[:1])
    byte2 = bytes(flags [1:2])
    rflags = ''
    QR = '1'
    OPCODE = ''
    for bit in range (1,5):
        OPCODE += str(ord(byte1)&(1<<bit))

    AA = '1'
    TC = '0'
    RD = '0'
    RA = '0'
    Z = '000'
    RCODE = '0000'

    return int(QR+OPCODE+AA+TC+RD, 2).to_bytes(1, byteorder='big')+int(RA+Z+RCODE, 2).to_bytes(1, byteorder='big')


def buildresponse(data):
    # Transaction ID Section
    TransactionID = data[0:2]
    TransID = ''
    for byte in TransactionID:
        TransID += hex(byte)[2:]

    # Get flags
    Flags = getflags(data[2:4])

    # Question Count
    QDCOUNT = b'\x00\x01'

    # Answer Count


print("Listening...")
# Persistent execution
while 1:
    data, addr = sock.recvfrom(512)
    response = buildresponse(data)
    sock.sendto(response, addr)