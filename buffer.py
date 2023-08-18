class MessageBuffer:
    def __init__(self):
        self.buffer = []

    def add_message(self, message):
        self.buffer.append(message)

    def get_messages(self):
        messages = self.buffer[:]
        self.buffer.clear()
        return messages
