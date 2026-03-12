# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  I received incorrect sugestions. It told me to go higher when the target was actually lower. It told me to go lower when the target was actually higher.
- List at least two concrete bugs you noticed at the start (for example: "the secret number kept changing" or "the hints were backwards").
  The hints were incorrect and backwards.
  The number of guesses not updating.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Gemini to explain displayed errors.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  The AI suggested I switch the logic for the hints as they were backward. It alsso caught edge case where user enters float or decimal number.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  The AI was correct on most of the code, but I noticed that error handling and printing to console were undescriptive and unhelpful.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  To determine if a bug was really fixed, I reran the streamlit app.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  I manually entered numbers higher or lower than the guess to verify hints logic has been reslved. I also consulted and updated the pytests code to ensure a successful compilation.
- Did AI help you design or understand any tests? How?
  Yes, AI suggested tests I should run to verify the code.


---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  There was an error where some session states were being converted to a string. Therefore, it could not be stored and read efficiently.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  I would explain that session state is like a notepad that remembers recently completed actions and information.
- What change did you make that finally gave the game a stable secret number?
  I removed the str and it allowed for better handling of session state variables

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Moving forward I plan to use the dot markdown file format to query files for errors
- What is one thing you would do differently next time you work with AI on a coding task?
  Next time, I would ask it to explain the code to  a child before debugging.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that AI is great for recognizing syntax, but the engineer has to be proactive about understanding logic and system design. 
