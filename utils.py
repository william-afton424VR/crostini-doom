import random

def random_damage(min_val=5, max_val=20):
    """Returns a random damage value within a range."""
    return random.randint(min_val, max_val)

def random_enemy_message():
    """Returns a randomly selected enemy attack message."""
    messages = [
        "Enemy Incoming!",
        "Brace yourself!",
        "You can't hide!",
        "Target locked!",
        "They're closing in!",
        "Dodge or die!",
        "Incoming strike!"
    ]
    return random.choice(messages)
