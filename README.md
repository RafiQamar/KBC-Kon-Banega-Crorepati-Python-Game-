# KBC (Kon Banega Crorepati) Python Game 🎮

Welcome to **KBC Kon Banega Crorepati**, a Python-based game inspired by the popular Indian quiz show! This project is a fun and engaging general knowledge quiz with a twist of risk and reward. Test your knowledge while managing the thrill of penalties and milestones. 

## Features ✨

1. **Random Question Selection**:
   - The game randomly selects 12 questions from a larger pool of general knowledge questions. 
   - Questions cover a variety of topics, such as geography, history, science, and pop culture.

2. **Progressive Rewards**:
   - Earn progressively higher rewards as you answer questions correctly.
   - Milestones at every 3rd question ensure guaranteed winnings when crossed.

3. **Penalty for Quitting Early**:
   - Adds a strategic layer: the earlier you quit, the higher the penalty.
   - Encourages players to weigh their risks and play strategically.

4. **Custom Error Handling**:
   - Handles incorrect user inputs with a custom error message, ensuring a smooth gaming experience.

5. **Interactive Gameplay**:
   - Each question includes four multiple-choice options.
   - Players can choose to answer or quit the game at any point.

## How It Works 🔧

1. **Question Module**:
   - The `kbc_questions` module provides a list of general knowledge questions.
   - The `get_questions()` function randomly selects 12 questions for each game session.

2. **Main Game Logic**:
   - The game iterates through the 12 questions and checks the player's answers.
   - Rewards are updated after every 3rd correct answer:
     - Questions 1-3: $1000, $2000, $5000
     - Questions 4-6: $10,000, $25,000, $50,000
     - Questions 7-9: $100,000, $150,000, $200,000
     - Questions 10-12: $250,000, $500,000, $1,000,000
   - Milestones ensure guaranteed winnings if reached.
   - Players who quit early face penalties based on their progress.

3. **Custom Exceptions**:
   - Handles invalid inputs (e.g., selecting options outside 'a', 'b', 'c', 'd', or quitting with '0') with user-friendly error messages.

4. **Endgame**:
   - Displays the total winnings based on the player's progress, penalties, and milestones.

## How to Play 🕹️

1. Clone this repository:
   ```bash
   git clone https://github.com/RafiQamar/kbc-python-game.git
   cd kbc-python-game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to answer questions or quit the game.

4. Enjoy the thrill of progressing through milestones and strategizing your way to the top prize of $1,000,000!

## File Structure 📂

- `kbc_questions.py`: Contains the pool of questions and the logic to fetch a random subset for the game.
- `main.py`: The main game logic, including handling user input, calculating rewards, and managing penalties.

## Example Gameplay 🎉

- Question: What is the capital of Japan?
  - a. Beijing
  - b. Seoul
  - c. Tokyo
  - d. Kyoto
- Input: `c`
  - Output: *Correct! You’ve won $1000 so far.*

## Future Improvements 🚀

- Add lifelines (e.g., 50-50, audience poll).
- Introduce difficulty levels.
- Create a GUI version for a more interactive experience.
- Add a leaderboard for competitive play.

## Contributions 🤝

Contributions, suggestions, and bug reports are welcome! Feel free to fork this repository and submit a pull request.

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Have fun playing and may you win the jackpot! 💰
