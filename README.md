# Gesture Controller

Gesture Controller makes human computer interaction simple by making use of Hand Gestures and Voice Commands. The computer requires almost no direct contact. All i/o operations can be virtually controlled by using static and dynamic hand gestures along with a voice assistant. This project makes use of the state-of-art Machine Learning and Computer Vision algorithms to recognize hand gestures and voice commands, which works smoothly without any additional hardware requirments. It leverages models such as CNN implemented by MediaPipe running on top of pybind11. It consists of two modules: One which works direct on hands by making use of MediaPipe Hand detection, and other which makes use of Gloves of any uniform color. Currently it works on Windows platform.


# Features
 _click on dropdown to know more_
### Gesture Recognition:
<details>
<summary>Move Cursor</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/e20edfb1f368ffa600d96bd91031942ec97cb2ab/demo_media/move%20mouse.gif" alt="Move Cursor" width="711" height="400">
</details>
*  Left Click
*  Right Click
*  Double Click
*  Scrolling
*  Drag and Drop
*  Multiple Item Selection
*  Volume Control
*  Brightness Control

### Voice Assistant ( ***Proton*** ):
<details>
<summary>Launch / Stop  Gesture Recognition</summary>
<ul>
  <li>
    <code> Proton Launch Gesture Recognition </code><br>
    Turns on webcam for hand gesture recognition.
  </li>
  <li>
    <code> Proton Stop Gesture Recognition </code><br>
    Turns off webcam and stops gesture recognition.
    (Termination of Gesture controller can also be done via pressing <code>Enter</code> key in webcam window)
   </li>
</ul>
</details>

<details>
<summary>Google Search</summary>
<ul>
  <li>
    <code>Proton search {text_you_wish_to_search}</code><br>
    Opens a new tab on Chrome Browser if it is running, else opens a new window. Searches the given text on Google.
  </li>
</ul>
</details>

<details>
<summary>Find a Location on Google Maps</summary>
  <ol>
    <li> 
      <code>Proton Find a Location</code><br>
      Will ask the user for the location to be searched.
    </li>
    <li> 
      <code>{Location_you_wish_to_find}</code><br>
      Will find the required location on Google Maps in a new Chrome tab.
    </li>
  </ol>
</details>

<details>
<summary>File Navigation</summary>
  <ul>
    <li>
      <code>Proton list files</code> / <code> Proton list </code><br>
      Will list the files and respective file_numbers in your Current Directory (by default C:)
    </li>
    <li>  
      <code> Proton open {file_number} </code><br>
      Opens the file / directory corresponding to specified file_number.
    </li>
    <li>
      <code>Proton go back </code> / <code> Proton back </code><br>
      Changes the Current Directory to Parent Directory and lists the files.
    </li>
  </ul>
</details>

<details>
<summary>Current Date and Time</summary>
  <ul>
    <li>
      <code> Proton what is today's date </code> / <code> Proton date </code><br>
      <code> Proton what is the time </code> / <code> Proton time </code><br>
      Returns the current date and time.
    </li>
  </ul>
</details>

<details>
<summary>Copy and Paste</summary>
  <ul>
    <li>
      <code> Proton Copy </code><br>
      Copies the selected text to clipboard.<br>
    </li>
    <li>
      <code> Proton Paste </code><br>
      Pastes the copied text.
    </li>
  </ul>
</details>

<details>
<summary>Sleep / Wake up Proton</summary>
  <ul>
    <li>
      Sleep<br>
      <code> Proton bye </code><br>
      Pauses voice command execution till the assistant is woken up.
    </li>
    <li>
      Wake up<br>
      <code> Proton wake up </code><br>
      Resumes voice command execution.
    </li>
  </ul>
</details>

<details>
<summary>Exit</summary>
  <ul>
    <li>
      <code> Proton Exit </code> <br>
      Terminates the voice assisstant thread. GUI window needs to be closed manually.
    </li>
  </ul>
</details>

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
  
