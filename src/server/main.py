import logging
import socket
import socketserver
import threading
from echo_handler import EchoRequestHandler
from echo_server import EchoServer


logging.basicConfig(level=logging.DEBUG, format='%(name)s: %(message)s')

if __name__ == '__main__':

    address = ('localhost', 0) # let the kernel give us a port
    server = socketserver.TCPServer(address, EchoRequestHandler)
    ip, port = server.server_address # find out what port we were given

    t = threading.Thread(target=server.serve_forever)
    # t.setDaemon(True) # don't hang on exit
    t.daemon = True # don't hang on exit
    t.start()

    logger = logging.getLogger('client')
    logger.info('Server on %s:%s', ip, port)

    # Connect to the server
    logger.debug('creating socket')
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug('connecting to server')
    s.connect((ip, port))

    # Send the data
    message = 'Hello, world'
    logger.debug('sending data: "%s"', message)
    # len_sent = s.send(message)
    len_sent = s.send(bytes(message, 'utf-8'))

    # Receive a response
    logger.debug('waiting for response')
    response = s.recv(len_sent)
    logger.debug('response from server: "%s"', response)

    # Clean up
    logger.debug('closing socket')
    s.close()
    logger.debug('done')
    server.socket.close()