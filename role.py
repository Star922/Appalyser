class Role:
    def __init__(self, name, permissions, home, context, chatplaceholder, chat, usage):
        self.name = name
        self.permissions = permissions
        self.home = home
        self.context=context
        self.chatplaceholder=chatplaceholder
        self.chat = chat
        self.usage = usage

    def add_to_history(self, new_entry):
        self.chat.history.append(new_entry)
