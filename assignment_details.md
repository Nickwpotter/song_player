# Playlist Manager 🎞️ 
## Objective
To build a console-based music playlist manager using a linked list that can manage multiple playlists, play songs, move to the next or previous song, add songs from a song pool, remove songs, display song details, and save/load playlists from/to a file. It has additional functionality of undo or redo any user action.
- Understand and implement linked lists.
- Learn the intricacies of list-based objects and how they interact in a linked-list environment.
- Get a foundational understanding of concepts that will be later covered in the course, like stacks and queues, which will be useful for features like `undo` and `redo`.


## Class files:
`song.py`: A `Song` class has been provided. If any additional functionality or properties needed, you need to modify this class.

`playlist.py`: Use a doubly linked list. All the functionalities of a plalist like, next, prev, play will be implemented here.Most of your logic will be implemented here.

`manager.py`: Manages multiple playlists. It also has functionality for undoing and redoing actions. Focus on this later part. At first you need to handle only one playlist having no undo-redo functionality. So At the begining your objective is to making sure this is communicating with main and playlist properly. 

`main_dev.py`: It has basic functionality. User will run this file during the development phase. 

`main.py` : Instead of using `main_dev.py` use this file for final release. 

## Basic Functionalities
- **Add Song to Playlist**: From the provided song pool, a song can be added to a playlist.
- **Remove Song**: Songs can be removed either by their name or their index in the playlist.
- **Display Playlist Songs**: Display all songs in the current playlist.
- **Play Song**: Display the details of the song currently being played.
- **Next Song**: Move to the next song in the playlist.
- **Previous Song**: Move to the previous song in the playlist.
- **Playlist Management**: Ability to switch between playlists, view all playlists, and create a new playlist.
- **Undo/Redo**: Implement the ability to undo or redo an action.
- **Save and Load**: Save the manager's state to a file and load it later.


## Extra credit (Premium features)
- Introduce any idea. Show your creativity here. Define the task, why it is portant, how it is going to change the user experience? (You are asking for additional payment for this premium feature, convince them!)

## Game Plan
---
### Week 1

#### Familiarization with codebase and implement foundational operations

- [ ] 1.1.  Describe the code organizations, how different classess are connected, how various datastructures are being accessed by various algoorithm

- [ ] 1.2. Implement `add` method of `Playlist` class

- [ ] 1.3. Make progress on `remove_by_name`, `remove_by_index` and `clear` method


#### Report
- Report 1.1
- Share implemented methods code
- Share your plan , (if you want to modify any plan below)
- Challange, experience, feedback

---
### Week 2

#### Enhance the playlist and introducing advanced features

- [ ] 2.1.  Finish the `reverse`, `total_count`, `total_view`, and `total_runtime` methods

- [ ] 2.2. Begin brainstorming and possibly implementing the `undo` and`redo` functionality

- [ ] 2.3. Implement the `save` and `load` functionalities


#### Report
- Hilight or discuss the completed methods and any changes made to the original structure
- State the plan, how you are planning to implement `undo` and `redo` function
- `save` and `load` function code sharing [if you find it hard I will share the code, how to implement, but make sure your playlist object is working fine.]
- Challange, experience, feedback
---
### Week 3

#### Advanced features & robustness 

- [ ] 3.1.  Complete `undo` and `redo` function

- [ ] 3.2. Begin brainstorming and possibly implementing the `undo` and`redo` functionality

- [ ] 3.3. Implement the `save` and `load` functionalities


#### Report
- Hilight or discuss the completed methods and any changes made to the original structure
- State the plan, how you are planning to implement `undo` and `redo` function
- `save` and `load` function code sharing [if you find it hard I will share the code, how to implement, but make sure your playlist object is working fine.]
- Challange, experience, feedback
---
### Week 4

#### Testing, bug fixing and extension 

- [ ] 4.1.  Conduct testing

- [ ] 3.2. Work on extra feature or creative aspect of the project

- [ ] 3.3. Refine code for efficiency (if any)


#### Report
- Test cases and their results, your approach to solve bugs (if any)
- What is the extra feature you have implemented? How and why it is different.
- What is the improvement you were planing for and you have implemented (if any)
- Challange, experience, feedback

## Submission
- Every week you have to submit the progress
- Submit zip file containing all the python files and additional files
- File name should be `<last_name_1>_<last_name_2>_v_<0.week or final>.zip `(developers last name(s) in alphabetical order in snake case)

## Point Distribution
- Correctness of the linked list implementation: [40 pts].
- Functionality and UI of the playlist manager: [30 pts].
- Implementation of additional features like save/load : [20 pts].
- Creativity: Introducing a new idea or concept, user experience, additional features, or any other innovative aspect: [10 pts]

## _Additional Note_
**List Objects in a List**: In Python, when you place objects in a list, you are essentially placing references (or pointers) to those objects in the list, not the objects themselves. When you make changes to an object that's referenced in a list, those changes are reflected across all references to that object.

**Linked List Access:** Unlike traditional lists, linked lists do not provide constant-time access to the $i^{th}$ item. Instead, you must traverse the list to find the $i^{th}$ item, which can take up to $O(n)$ time in the worst case.

## Fair Play
- You are allowed to discuss about the logic with any other group over MS Team, but do not share your code. Thank them in your readme file for their time and effort.
- Cite any article or post if you follow the coding from them (even stackoverflow or any forum)
- Communicate Properly. If you need extra time or got stuck, feel free to reach out. 
- Use of any AI coding assistant is strictly prohabited.