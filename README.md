


# Lode Runner Online (Web based)

#### Lode Runner is a legendary 1983 puzzle-platform video game developed by Douglas E. Smith and originally published by Brøderbund Software. Renowned for its highly strategic gameplay, it was one of the earliest games to blend fast-paced action with intense puzzle-solving. It is also famous for being one of the first video games to include a built-in level editor, allowing players to design and share their own custom stages.

https://en.wikipedia.org/wiki/Lode_Runner


#### We have added more levels and will soon have the ability to add new levels.  This version works on tablets as well.

#### Have a comment or want to add a new level?  Just use https://github.com/robthelinuxguy/LodeRunner/issues

### * PLAY it online here:
<a target="_blank" href="https://robthelinuxguy.github.io/LodeRunner/">https://robthelinuxguy.github.io/LodeRunner/</a>

### * What's new? (Oct 2026)
- Added over 400 levels
- Added Speed settings for enemy guards
- Added scroll bars to level selection (for tablets, phones)
- Added URL parameters to jump straight into a game & level (see below)


### * Play a specific game and level number with a link
Add URL parameters to start the game right on a chosen level, no menu needed:
- `?game=`  game id number, 1 to 9 (see the table below).  Without it, the game you played last is used.
- `?level=` level number, starting at 1.  

| Game id | Game | Levels |
|---------|-----------------------------|--------|
| 1 | Classic Lode Runner | 150 |
| 2 | Championship Lode Runner | 50 |
| 3 | Professional Lode Runner | 150 |
| 4 | Revenge of Lode Runner | 78 |
| 5 | Lode Runner Fan Book | 90 |
| 6 | Sneaky & Hyper Levels | 110 |
| 7 | Big Red Apple Levels | 100 |
| 8 | Fred Pence Levels | 150 |
| 9 | Super LR Levels | 150 |

The game id is not the same as the position of the game in the "Select Game Version" menu.

Examples:
- `https://robthelinuxguy.github.io/LodeRunner/?game=1&level=5`  ...  Classic Lode Runner, level 5
- `https://robthelinuxguy.github.io/LodeRunner/?game=3&level=22`  ...  Professional Lode Runner, level 22


### Play on a Local Machine
A simple web server is required to play Lode Runner on a local machine.
Open a web browser and go to "http://127.0.0.1:8080/lodeRunner.html". (use the correct Port #)
<br>
#### Forked from the amazing work by https://github.com/SimonHung : https://github.com/SimonHung/LodeRunner_TotalRecall

"Lode Runner" is a trademark of Tozai Games. This project is unaffiliated with and unendorsed by Tozai Games or any other rights holder.
