# Gesture Controller

Gesture Controller makes human computer interaction simple by making use of Hand Gestures and Voice Commands. The computer requires almost no direct contact. All i/o operations can be virtually controlled by using static and dynamic hand gestures along with a voice assistant. This project makes use of the state-of-art Machine Learning and Computer Vision algorithms to recognize hand gestures and voice commands, which works smoothly without any additional hardware requirments. It leverages models such as CNN implemented by MediaPipe running on top of pybind11. It consists of two modules: One which works direct on hands by making use of MediaPipe Hand detection, and other which makes use of Gloves of any uniform color. Currently it works on Windows platform.


# Features

Gesture Recognition:
*  Move Cursor
*  Left Click
*  Right Click
*  Double Click
*  Scrolling
*  Drag and Drop
*  Multiple Item Selection
*  Volume Control
*  Brightness Control

Voice Assistant ( ***Proton*** ):
*  [Launch / Stop  Gesture Recognition](github.com/xenon-19/Gesture_Controller/blob/main/README.md?plain=1#L43)
*  Google Search
*  Find a Location on Google Maps
*  File Navigation
*  Current Date and Time
*  Copy and Paste Shortcuts
*  Sleep / Wake up Proton
*  Exit

# Getting Started
  ### Requirments
  ``` pip install requirments.txt ```
  ### Procedure
  Lorem ipsum





# Usage
  ### Hand Gesture
  ...
  ### Voice Commands
*  Launch / Stop  Gesture Recognition <br>
``` Proton Launch Gesture Recognition ``` <br>
   Turns on webcam for hand gesture recognition. <br>
``` Proton Stop Gesture Recognition ``` <br>
   Turns off webcam and stops gesture recognition. (Termination of Gesture controller can also be done via pressing ```Enter``` key in webcam window) <br>
   
*  Google Search <br>
  ``` Proton search {text_you_wish_to_search} ``` <br>
  Opens a new tab on Chrome Browser if it is running, else opens a new window. Searches the given text on Google. <br>
  
*  Find a Location on Google Maps <br>
   Step 1: ``` Proton Find a Location ``` <br>
   Will ask the user for the location to be searched <br>
   Step 2: ```{Location_you_wish_to_find}``` <br>
   Will find the required location on Google Maps in a new Chrome tab. <br>
   
*  File Navigation <br>
  ``` Proton list files ``` / ``` Proton list ``` <br>
  Will list the files and respective file_numbers in your Current Directory (by default C:) <br>
  ``` Proton open {file_number} ``` <br>
  Opens the file / directory corresponding to specified file_number. <br>
  ``` Proton go back ``` / ``` Proton back ``` <br>
  Changes the Current Directory to Parent Directory and lists the files.  <br>
    
*  Current Date and Time <br>
  ``` Proton what is today's date ``` / ``` Proton date ``` <br>
  ``` Proton what is the time ``` / ``` Proton time ``` <br>
  Returns the current date and time <br>
  
*  Copy and Paste <br>
  ``` Proton Copy ``` <br>
  Copies the selected text to clipboard. <br>
  ``` Proton Paste ``` <br>
  Pastes the copied text. <br>
  
*  Sleep / Wake up Proton <br>
   Sleep: <br>
  ``` Proton bye ``` <br>
  Pauses voice command execution till the assistant is woken up. <br>
  Wake up: <br>
  ``` Proton wake up ``` <br>
  Resumes voice command execution. <br>
    
*  Exit <br>
  ``` Proton Exit ``` <br>
  Terminates the voice assisstant thread. GUI window needs to be closed manually. <br>
  
# Collaborators
  | |  |  |  |  |
  | ------------- | ------------- | ------------- | ------------- | ------------- |
  | Viral Doshi | [GitHub](https://github.com/Viral-Doshi) | [Email](mailto:viraldoshi321@gmail.com) | [LinkedIn](https://www.linkedin.com/in/viral-doshi-5a7737190/) | [Instagram](https://www.instagram.com/_viral_doshi/) |
  | Nishiket Bidawat | Github | Email | LinkedIn | Instagram |
  | Ankit Sharma | Github | Email | LinkedIn | Instagram |
  | Parth Sakariya | Github | Email | LinkedIn | Instagram |
  
