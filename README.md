# Week 7 - Greed Design
## Team Members: Ashley, Hailey, John, Matt, Ethan

## Greed Game
There are things falling from the sky! Move the character (#) and make sure to catch the gems (*) and avoid the rocks (0). Gems will give the player a point while rocks remove points. The score is displayed in the top of the screen. There is no win/lose, closing the window ends the game.

# TODO: Design
## Team members in attendance 6/2 (Designing): Ashley, Hailey, John, Matt
Requirements:
- Eight classes
- Gems and rocks randomly appear at the top of the screen
- Player can move left and right along the bottom
- Gems +1 to score
- Rocks -1 to score
- Gems and rocks dissapear when they hit the player (or ground?)
- Game continues forever, exits only when window is closed

| Class | Job |
| ----- | --- |
Director/Game | Directs the inner workings of the game
Player | Moves around the screen, interacts with the rocks and gems
Player Input | Gets input from the user, only acting on valid input ('a' or left arrow - left, 'd' or right arrow - right, 'q' - quit)
GUI/Screen | Displays everything on the screen
Rock | Falls from the sky at a certain speed, has a character/sprite to represent itself, and has a -1 point
Gem | Inherits from Rock, overwrites character/sprite and +1 point
Score | Calculates and displays the score
\* Message | Displays a game over message/extra messages/etc
\* Big Rock | A bigger version of rock with a larger hitbot and sprite

\* Indicates that the feature is optional, depending on if the 8 class requirement has been met.

# Week 8 - Greed Program
## Team members in attendance 6/9 (Programming)

## TODO: Implementation
- [ ] Code each class (using inheritance!)
     - [ ] Director/Game
     - [ ] Player
     - [ ] Player Input
     - [ ] GUI/Screen
     - [ ] Rock
     - [ ] Gem
     - [ ] Score
     - [ ] * Big Rock
     - [ ] * Message
- [ ] Add comments
- [ ] Ensure the entire program works

## Extra
- Enhanced gems and rocks (multiple kinds, different points).
- Enhanced player movement (up and down in a limited range) - Jumping
- Enhanced game play and game over messages. - actually end the game
- Enhanced gem, rock and player representation (colors or better symbols) - images possibly?
