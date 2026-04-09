🎮 Glitchy Guesser: AI Edition
Title and Summary: Glitchy Guesser: AI Edition is a strategic number-guessing system that uses an AI agent to turn a simple game into a logic challenge. This project matters because it demonstrates how to integrate LLMs into traditional applications while maintaining reliability through custom guardrails.

Base Project Identification and Original Scope
The foundation of this system is the "Glitchy Guesser" CLI game, a project originally developed during Modules 1-3. In its initial scope, the application functioned as a standard number-guessing utility where the primary goal was to provide a hands-on environment for debugging state management and logic errors in a Streamlit environment. The original system's capabilities included basic random number generation, a two-layered architecture separating presentation logic from game rules, and a simple feedback loop that returned "Too High" or "Too Low" responses. By identifying this base project, a clear context is established for the current extensions: shifting the system from a static, rule-based script into an Applied AI System that leverages a strategic agent and reliability guardrails to enhance the user experience.

Substantial New AI Feature: The Strategic Agent Workflow
This project introduces a Strategic AI Hint Master, a substantial evolution from the original static logic. Rather than providing simple "higher/lower" feedback, the system implements a multi-step agentic workflow using structured prompting and contextual analysis. The AI Agent retrieves the user’s entire guess history, the secret number, and the difficulty setting to generate a sophisticated mathematical hint—such as identifying if the target is a prime number, a Fibonacci sequence member, or evaluating the user's current narrowing strategy. This feature is fully integrated into the core game loop in app.py, meaning it is not a standalone demo but a functional part of the system that meaningfully alters user behavior by encouraging strategic deduction over random guessing. To ensure high-quality output, the workflow includes an automated self-checking reliability harness that validates the hint before it reaches the UI, preventing the AI from prematurely ending the game by leaking the secret number.

✨ Features
Strategic AI Hint Master: Get contextual hints from an AI that analyzes your guess history and the current difficulty.

Self-Critique Guardrail: A safety check ensures the AI never accidentally reveals the secret number.

Clean Architecture: The application is built with a modular three-tiered architecture.

Streamlit UI: A user-friendly web interface for a seamless gaming experience.

🚀 System Architecture
Architecture Overview: The system uses a modular design where app.py acts as the controller, logic_utils.py handles the deterministic math, and ai_agent.py processes natural language. Data flows from user input to the logic layer for verification, then to the AI Agent for hint generation, passing through a guardrail before returning to the UI.

app.py (Presentation Layer): Manages the Streamlit UI, user input, and game state.

logic_utils.py (Logic Layer): Contains pure Python functions for game logic, such as range calculation and score tracking.

ai_agent.py (AI Service Layer): Manages LLM prompting, context history, and the reliability guardrail.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-link]
    cd guessing_game_ai
    ```
2.  **Set up a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    # .venv\Scripts\activate   # Windows
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure environment variables:**
    Create a `.env` file in the root directory with your OpenAI API key:
    ```text
    GROQ_API_KEY=your_key_here
    ```
5.  **Run the application:**
    ```bash
    streamlit run app.py --server.enableCORS=false --server.enableXsrfProtection=false --server.address=0.0.0.0
    ```

--- 
🎮 Sample Interactions
User Input: Guess 10 (Target 42). AI Output: "That is quite low. The secret is much closer to the upper limit of your current range."

User Input: Guess 50 (Target 42). AI Output: "You're getting closer. The secret number is an even number and is a multiple of 6."

User Input: Guess 40 (Target 42). AI Output: "You are very warm; the number is greater than 40 but is not a prime number."

🛠️ Design Decisions
I chose a modular three-tier architecture to keep the AI logic separate from the game engine. A major trade-off was using Structured Prompting instead of a complex RAG system; while RAG allows for more data, simple prompting was the "path of least resistance" for a localized game and significantly reduced latency.

🔬 Reliability and Evaluation
Testing Summary: The core math logic passed 100% of the unit tests. The AI struggled initially with leaking the secret number in hints, but the String-Matching Guardrail effectively resolved this. I learned that AI requires strict output constraints to remain helpful without spoiling the game.

💭 Reflection
This project taught me that AI is an excellent tool for recognizing patterns and syntax, but the engineer must remain proactive in designing the logic and safety loops. Problem-solving in an AI context is less about writing every line of code and more about architecting how the AI interacts with deterministic systems.

🔮 Future Improvements
[ ] Add a Confidence Score for each AI hint.

[ ] Implement a Leaderboard using a SQLite database.

[ ] Add a "Voice Hint" feature using Text-to-Speech.

![Game Demo](/assets/demo.gif)
![Diagrams](/assets/diagram3.png)
![Diagrams](/assets/diagram1.png)
![Diagrams](/assets/diagram2.png)
![Output](/assets/output1.png)
![Output](/assets/output2.png)
![Output](/assets/output3.png)