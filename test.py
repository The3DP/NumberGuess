def test_example():
    # A simple test to check arithmetic
    assert 1 + 1 == 2

def test_number_guess_logic():
    # Replace this logic with your game's actual logic
    correct_number = 7
    user_guess = 7
    assert user_guess == correct_number, "The guess should match the correct number"

def test_string_output():
    # Test for any string output functionality in your game
    welcome_message = "Welcome to the Number Guessing Game!"
    assert "Welcome" in welcome_message
