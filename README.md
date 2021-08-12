# Gesture_Controller

Gesture_Controller provides ease of interacting with computer by using hand gesture and voice commands, almost no direct contact is required with computer.
This project makes use of the state-of-art machine learning and computer vision algorithm to recognize hand gestures and voice commands, which works smoothly without any additional hardware requirments. It leverages models such as CNN implemented by MediaPipe running on top of pybind11.
It consists of two modules one which requires hand glove and another without hand glove.
Currently it works on Windows platform.

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
*  Launch / Stop  Gesture Recognition
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
*  Launch / Stop  Gesture Recognition
``` Proton Launch Gesture Recognition ```
   Turns on webcam for hand gesture recognition.
``` Proton Stop Gesture Recognition ```
   Turns off webcam and stops gesture recognition. (Termination of Gesture controller can also be done via pressing ```Enter``` key in webcam window)
   
*  Google Search
  ``` Proton search {text_you_wish_to_search} ```
  Opens a new tab on Chrome Browser if it is running, else opens a new window. Searches the given text on Google.
  
*  Find a Location on Google Maps
   Step 1: ``` Proton Find a Location ```
   Will ask the user for the location to be searched
   Step 2: ```{Location_you_wish_to_find}```
   Will find the required location on Google Maps in a new Chrome tab.
   
*  File Navigation
  ``` Proton list files ``` / ``` Proton list ```
  Will list the files and respective file_numbers in your Current Directory (by default C:)
  ``` Proton open {file_number} ```
  Opens the file / directory corresponding to specified file_number.
  ``` Proton go back ``` / ``` Proton back ```
  Changes the Current Directory to Parent Directory and lists the files. 
    
*  Current Date and Time
  ``` Proton what is today's date ``` / ``` Proton date ```
  ``` Proton what is the time ``` / ``` Proton time ```
  Returns the current date and time
  
*  Copy and Paste
  ``` Proton Copy ```
  Copies the selected text to clipboard.
  ``` Proton Paste ```
  Pastes the copied text.
  
*  Sleep / Wake up Proton
   Sleep:
  ``` Proton bye ```
  Pauses voice command execution till the assistant is woken up.
  Wake up:
  ``` Proton wake up ```
  Resumes voice command execution.
    
*  Exit
  ``` Proton Exit ```
  Terminates the voice assisstant thread. GUI window needs to be closed manually.
  
# Collaborators
  Viral Doshi   Github  Email  LinkedIn  Instagram
  Nishiket Bidawat   Github  Email  LinkedIn  Instagram
  Ankit Sharma   Github  Email  LinkedIn  Instagram
  Parth Sakariya   Github  Email  LinkedIn  Instagram
