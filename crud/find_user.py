from models import User


def find_user(chat):
    return User.find_one(chat_id=chat.id)
