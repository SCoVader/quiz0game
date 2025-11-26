import socketserver
import logging


class Quiz0Server(socketserver.TCPServer):
    
    def __init__(self, server_address, handler_class):
        self.logger = logging.getLogger('Quiz0Server')
        self.logger.debug('__init__')
        super().__init__(self, server_address, handler_class)
        return

    def server_bind(self):
        self.logger.debug('server_bind')
        super().server_bind()
        return

    def server_activate(self):
        self.logger.debug('server_activate')
        super().server_activate(self)
        return

    def serve_forever(self):
        self.logger.debug('waiting for request')
        self.logger.info('Handling requests, press <Ctrl-C> to quit')
        while True:
            self.handle_request()
        return

    def handle_request(self):
        self.logger.debug('handle_request')
        return super().handle_request(self)

    def verify_request(self, request, client_address):
        self.logger.debug('verify_request(%s, %s)', request, client_address)
        return super().verify_request(self, request, client_address)

    def process_request(self, request, client_address):
        self.logger.debug('process_request(%s, %s)', request, client_address)
        return super().process_request(self, request, client_address)

    def server_close(self):
        self.logger.debug('server_close')
        return super().server_close(self)

    def finish_request(self, request, client_address):
        self.logger.debug('finish_request(%s, %s)', request, client_address)
        return super().finish_request(self, request, client_address)

    def close_request(self, request_address):
        self.logger.debug('close_request(%s)', request_address)
        return super().close_request(self, request_address)
