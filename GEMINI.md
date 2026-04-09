ADD TO KNOWLEDGE BASE AND ALWAYS REFER TO KNOWLEDGE BASE BEFORE CODE SUGGESTIONS AND WAIT FOR NEXT INSTRUCTIONS: Project Type: This is a simple Command Line Interface (CLI) application.

Problem Solved: It's a classic number guessing game. The program generates a secret number, and the user has a limited number of attempts to guess it. The application provides feedback ("Too high" or "Too low") after each guess.

The project follows a clean, two-layered architecture, which is a great practice for separating concerns even in small applications.



Presentation Layer (app.py): This is the user-facing part of the application. It handles all the direct interaction with the user, such as printing welcome messages, prompting for input, and displaying the results. It's the "front-end" of your CLI app.

Logic Layer (logic_utils.py): This is the "back-end" or "brains" of the operation. It contains the core game logic, completely detached from how the information is presented to the user. Its responsibilities include evaluating a guess against the secret number and determining the correct feedback.

This separation is its key architectural strength. You could swap the CLI front-end for a web interface without needing to change the core game logic at all.



app.py (The Game Conductor):



Purpose: To manage the overall flow and state of the game.

Responsibilities:

Initializes the game (sets the number of guesses, generates the secret number).

Contains the main game loop (while guess != secret_number...).

Handles user input, including basic validation to ensure the input is a number.

Calls the logic layer (logic_utils.py) to evaluate the user's guess.

Prints all output to the console (welcome, prompts, hints, win/loss messages).

logic_utils.py (The Rule Engine):



Purpose: To encapsulate the pure logic of the guessing game.

Responsibilities:

The check_guess function is the core of this file. It takes the user's guess and the secret number, compares them, and returns a simple, clear string indicating the result: "Too high", "Too low", or "Correct!". It is not responsible for printing this result, only for determining it.

tests/test_game_logic.py (The Quality Assurance Inspector):



Purpose: To ensure the logic_utils.py file works as expected.

Responsibilities:

Contains unit tests that verify the correctness of the check_guess function under different scenarios (guess is too high, too low, or correct). This guarantees that the game's core rules are consistently applied.

The data flow is straightforward and unidirectional, making it very easy to follow.



+-----------+                                       +----------------+

|  User     |                                       |     app.py     |

+-----------+                                       +----------------+

      ^                                                     ^

      |                                                     |

      | 1. Asks for guess                             6. Prints hint

      |    (e.g., "Guess a number:")                        (e.g., "Too high")

      |                                                     |

      +-----------------------------------------------------+

      | 2. Enters guess (e.g., "50")

      v

+-----------+                                       +----------------+

|  app.py   | -- 3. Calls check_guess("50", 42) --> | logic_utils.py |

+-----------+                                       +----------------+

      ^                                                     |

      |                                                     | 5. Compares 50 and 42

      |                                                     |

      |  4. Returns hint string "Too high"                  |

      |                                                     v

      +-----------------------------------------------------+





python: The entire application is written in standard Python.

random: A built-in Python library used in app.py to generate the secret number.

pytest: (Found in requirements.txt) A popular third-party testing framework used to run the unit tests in test_game_logic.py.

The minimalist tech stack makes the project highly portable and easy to run without complex setup.



Start: The user runs python app.py in the terminal.

Initialization: app.py starts the game() function. It picks a random integer between 1 and 100 to be the secret_number.

Game Loop: The while loop begins.

User Input: The program prints "Guess a number between 1 and 100:" and waits for the user to type a number and press Enter.

Logic Call: The user's input string is converted to an integer and passed, along with the secret_number, to the check_guess() function in logic_utils.py.

Logic Execution: check_guess() compares the two numbers and returns a string: "Too high", "Too low", or "Correct!".

Feedback: app.py receives the string and prints it to the console for the user to see.

Repeat: The loop continues until the user guesses correctly (triggering a "You win!" message) or runs out of attempts.

Strengths:



Excellent Separation of Concerns: The single best feature of this architecture. The UI (app.py) and Logic (logic_utils.py) are decoupled, making the code easy to understand, modify, and test.

Testability: The core logic is easily testable with unit tests, which increases confidence that the game works correctly.

Readability: The code is clean, and the file names clearly communicate their purpose.

Tradeoffs:



For a project of this small scale, this level of structure is perfect and has no significant downsides. It serves as an excellent template for building larger, more complex applications.

This project is a CLI number-guessing game built with a clean two-layer design. The main app.py file handles user interaction, while logic_utils.py contains the core game rules, making the system well-structured and easy to test.