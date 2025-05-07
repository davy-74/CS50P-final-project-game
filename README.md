# Platform hoarder
#### **Video Demo:**  <https://youtu.be/G-olHUXpJFo>
#### **Description:**
A simple jumping game using pygame library.

### **Project structure:**

* **Image_files** (Folder containing game image files)
* **Sound_files** (Folder containing game sound files)
* **Project.py** (Main project file)
* **README.md**
* **Requirements.txt** (File listing neccesary libraries)
* **Test_project.py** (File for testing main project)

### **Technical overview:**
The game is seperated into a main function and seven custom functions.

**Main function:**

The game loop resides within the main function. Before entering the loop, necessary variables are declared.
At the start of the game loop, framerate (FPS) is set to 60, and delta time is calculated to decouple movement from framerate.
The event handler checks left and right movement using the arrow keys and flips the player image accordingly.
After event handler player variables are updated along with player rect object. Also boundaries are added for player movement, ensuring the player can't move off the screen. Function calls are made to draw player and platforms, increment score, show score and handle game over screen. Near the end of the game loop a collision check is performed between player rectangle and platform rectangles. In case of collision movements are updated and a sound played.

**Drawing functions:**

**Show_score**, **player**, and **platform** functions simply use screen.blit method to draw the image and text onto the screen surface.


**change_col function:**

Creates a list of RGB color tuples and returns the appropriate value depending on the score. That value is passed into screen.fill method in the main function to paint the screen a certain color.

**create_platform_rects:**

Takes one argument specifying how many rectangles to create. Creates an empty list and then uses the get_rect and inflate methods to get a rectangle from the platform image and resize it. Then uses random.randint method to generate random numbers in certain range for where the platforms are going to be located on the screen. Adds the rectangles attached to platform image in the rectangles list for returning. Rectangles list is looped through and drawn on the screen in the game loop.

**game_over_screen:**

This function takes as an argument the rectangles list within the game loop. It then handles the logic of displaying the game over screen, which involves changing the screen color, displaying text and clearing the platform rectangles list. It then returns the cleared list for the purposes of testing

**increment_score:**

This function loops through the platforms rectangles list to check for their position to see if score should rise. After score rises a sound is played and the platform is reset using the random.randint method. Conditionals are added to make sure reset platform stays within the game window.

### **Design choices:**

This game initially started as an idea to try to remake some version of Doodle Jump. Where the player would move upward jumping on platforms. That idea was discarded because initially i struggled to figure out how to generate platforms. After some trial and error i came upon the current version of how the game works, where the player jumps on platforms and the platform moves down. The goal is to nudge the platform down the screen.  Playing the current version the strategy is to always go for the highest platform, otherwise you might not reach it later. I also debated adding different functionality to the game, like adding a beginning and end menu, additional gameplay mechanics and more music. Those ideas were discarded because of unnecessary complexity regarding the scope of the project.

### **Main problems:**

This game was developed over the course of about six months. The core problem was always platform generation and how should i implement it. I considered giving player the opportunity to pick the amount of platforms, but eventually settled on seven platforms, because it felt appropriate considering difficulty. Too many platforms would clutter the screen and make it too easy. Only a few platforms would make the game impossible with the current implementation of platform generation. The other issues where fine-tuning rectangle sizes used for collision and fine-tuning movement speed, which also had to be reworked when decoupling movement from framerate.

### **Testing:**
Functions being tested with pytest:
* **create_platfrom_rects**
* **game_over_screen**
* **change_col**

Most of the game was written without testing in mind, so functions needed to be modified to make testing easier. For instance game_over_screen function returns a rectangles list just for the purposes of making testing easier.