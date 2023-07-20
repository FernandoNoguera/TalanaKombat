# Constants for movements and strikes
MOVEMENTS = {"W", "S", "A", "D", "SD", "DSD", "SA", "ASA"}
STRIKES = {"P", "K"}

# Constants for character names
ARNALDOR = "Arnaldor Shuatseneguer"
TONYN = "Tonyn Stallone"

# Dictionary to map character moves and strikes to their corresponding actions and energy usage
CHARACTER_ACTIONS = {
    "Tonyn Stallone": {
        ("DSD", "P"): ("Taladoken", 3),
        ("SD", "K"): ("Remuyuken", 2),
        ("P", None): ("puñetazo", 1),
        ("K", None): ("patada", 1),
    },
    "Arnaldor Shuatseneguer": {
        ("SA", "K"): ("Remuyuken", 3),
        ("ASA", "P"): ("Taladoken", 2),
        ("P", None): ("puñetazo", 1),
        ("K", None): ("patada", 1),
    },
}

# Dictionary to map letter representations to words for movements and strikes
MOVEMENTS_WORDS = {
    "W": "arriba",
    "S": "abajo",
    "A": "izquierda",
    "D": "derecha",
    "SD": "diagonal inferior derecha",
    "DSD": "diagonal superior derecha",
    "SA": "diagonal superior izquierda",
    "ASA": "diagonal inferior izquierda",
}
STRIKES_WORDS = {
    "P": "puñetazo",
    "K": "patada",
}


def determine_winner(energy_p1, energy_p2):

    winner = ARNALDOR if energy_p1 <= 0 else TONYN if energy_p2 <= 0 else None

    if winner:
        return f"{winner} gana la pelea."
    else:
        return "La pelea ha terminado en un empate."


def execute_strike(character, movement, strike):
    energy = 0
    narration = ""

    if character in CHARACTER_ACTIONS:
        action_key = (movement, strike)
        if action_key in CHARACTER_ACTIONS[character]:
            action, energy = CHARACTER_ACTIONS[character][action_key]
            narration = f"{character} usa {action}"
        elif movement in MOVEMENTS:
            narration = f"{character} se mueve hacia  {MOVEMENTS_WORDS[movement]}"
            energy = 0
        elif strike in STRIKES:
            narration = f"{character} usa {STRIKES_WORDS[strike]}"
            energy = 1

    return narration, energy

