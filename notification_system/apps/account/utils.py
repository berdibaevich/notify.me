import random

def get_upload_avatar_for_user():
    guess = random.randrange(1, 5)
    return f"avatars/avatar_{guess}.png"