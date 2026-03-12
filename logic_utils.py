def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    difficulty_map = {
        "Easy": (1, 20),
        "Normal": (1, 50),
        "Hard": (1, 100) 
    }
    return difficulty_map.get(difficulty, (1, 20))

def parse_guess(raw: str):
    """
    Parse user input into an int guess.
    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if not raw or raw.strip() == "":
        return False, None, "Please enter a number."

    try:
        value = int(float(raw.strip()))
        return True, value, None
    except ValueError:
        return False, None, f"'{raw}' is not a valid integer."



def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).
    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct! You nailed it."
    
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    
    return "Too Low", "📈 Go HIGHER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = max(10, 100 - (attempt_number * 10))
        return current_score + points

    if outcome in ["Too High", "Too Low"]:
        return max(0, current_score - 2)

    return current_score