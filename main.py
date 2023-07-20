import json

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
    """
    Determines the winner of the fight based on the remaining energy of each player.

    Args:
        energy_p1 (int): The remaining energy points of player 1.
        energy_p2 (int): The remaining energy points of player 2.

    Returns:
        str: A string indicating the result of the fight. It will be one of the following:
            - "{character_name} wins." (if a character has less than or equal to 0 energy)
            - "The fight ends in a draw." (if both characters have more than 0 energy)
    """

    winner = ARNALDOR if energy_p1 <= 0 else TONYN if energy_p2 <= 0 else None

    if winner:
        return f"{winner} gana la pelea."
    else:
        return "La pelea ha terminado en un empate."


def execute_strike(character, movement, strike):
    """
    Executes a strike for the given character based on the provided movement and strike inputs.

    Args:
        character (str): The name of the character performing the strike.
        movement (str): The movement input for the character (e.g., "DSD", "SA").
        strike (str): The strike input for the character (e.g., "P", "K").

    Returns:
        tuple: A tuple containing the narration of the action and the energy cost of the strike.
            The narration describes the action taken by the character, and the energy cost
            represents the amount of energy consumed by the strike action.
    """
    
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


def narrate_fight(fight_json):
    """
    Narrates the fight between two characters, TONYN and ARNALDOR, based on their actions.

    Args:
        fight_json (dict): A dictionary containing the actions of player 1 and player 2.

    Returns:
        str: A string containing the narrative of the fight and the final result.
    """

    try:
        fight_json = json.loads(fight_json)
    except Exception as e:
        raise ValueError('Ingrese un valor con la siguiente estructura: {"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}')


    narration = ""
    p1_energy, p2_energy = 6, 6

    p1 = TONYN
    p2 = ARNALDOR

    max_turns = max([fight_json["player1"]["movimientos"], fight_json["player2"]["movimientos"]], key=len)
    
    for i in range(len(max_turns)):
        movement_p1 = (
            fight_json["player1"]["movimientos"][i] if i < len(fight_json["player1"]["movimientos"]) else ""
        )
        strike_p1 = fight_json["player1"]["golpes"][i] if i < len(fight_json["player1"]["golpes"]) else ""

        movement_p2 = (
            fight_json["player2"]["movimientos"][i] if i < len(fight_json["player2"]["movimientos"]) else ""
        )
        strike_p2 = fight_json["player2"]["golpes"][i] if i < len(fight_json["player2"]["golpes"]) else ""

        narration_p1, energy_strike_p1 = execute_strike(p1, movement_p1, strike_p1)
        narration_p2, energy_strike_p2 = execute_strike(p2, movement_p2, strike_p2)

        if narration_p1:
            narration += f"{narration_p1}\n"
        if narration_p2:
            narration += f"{narration_p2}\n"

        p2_energy -= energy_strike_p1

        if p2_energy <= 0:
            break

        p1_energy -= energy_strike_p2

        if p1_energy <= 0:
            break

    narration += determine_winner(p1_energy, p2_energy)
    return narration


if __name__ == "__main__":
    print()

    print("*************** Pelea 1 ***************")

    example_1 = """{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2":{"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}"""

    print()
    result = narrate_fight(example_1)
    print(result)
    print()


    print("*************** Pelea 2 ***************")

    example_2 = """{"player1":{"movimientos":["SDD","DSD","SA","DSD"],"golpes":["K","P","K","P"]},"player2":{"movimientos":["DSD","WSAW","ASA","","ASA","SA"],"golpes":["P","K","K","K","P","k"]}}"""

    
    print()
    result = narrate_fight(example_2)
    print(result)
    print()


    print("*************** Pelea 3 ***************")

    example_3 = """{"player1":{"movimientos":["DSD","S"],"golpes":["P",""]},"player2":{"movimientos":["","ASA","DA","AAA","","SA"],"golpes":["P","","P","K","K","K"]}}"""

    
    print()
    result = narrate_fight(example_3)
    print(result)
    print()


    print("*************** Tu pelea ***************")



    
    print()
    secuence = input("Ingrese la secuencia de combate: ")
    result = narrate_fight(secuence)
    print(result)
    print()