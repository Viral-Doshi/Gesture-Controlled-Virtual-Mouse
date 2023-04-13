

# Gesture Controlled Virtual Mouse &nbsp;[![](https://img.shields.io/badge/python-3.8.5-blue.svg)](https://www.python.org/downloads/) [![platform](https://img.shields.io/badge/platform-windows-green.svg)](https://github.com/xenon-19/Gesture_Controller) 

Gesture Controlled Virtual Mouse makes human computer interaction simple by making use of Hand Gestures and Voice Commands. The computer requires almost no direct contact. All i/o operations can be virtually controlled by using static and dynamic hand gestures along with a voice assistant. This project makes use of the state-of-art Machine Learning and Computer Vision algorithms to recognize hand gestures and voice commands, which works smoothly without any additional hardware requirements. It leverages models such as CNN implemented by [MediaPipe](https://github.com/google/mediapipe) running on top of pybind11. It consists of two modules: One which works direct on hands by making use of MediaPipe Hand detection, and other which makes use of Gloves of any uniform color. Currently it works on Windows platform.

 _Video Demonstration: [link](https://www.youtube.com/watch?v=ufm6tfgo-OA&ab_channel=Proton)_<br>
Note: Use Python version: 3.8.5

# Features
 _click on dropdown to know more_ <br>

### Gesture Recognition:
<details>
<summary>Neutral Gesture</summary>
 <figure>
  <img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/palm.gif" alt="Palm" width="711" height="400"><br>
  <figcaption>Neutral Gesture. Used to halt/stop execution of current gesture.</figcaption>
</figure>
</details>
 

<details>
<summary>Move Cursor</summary>
  <img src="https://github.com/xenon-19/Gesture_Controller/blob/e20edfb1f368ffa600d96bd91031942ec97cb2ab/demo_media/move%20mouse.gif" alt="Move Cursor" width="711" height="400"><br>
  <figcaption>Cursor is assigned to the midpoint of index and middle fingertips. This gesture moves the cursor to the desired location. Speed of the cursor movement is proportional to the speed of hand.</figcaption>
</details>

<details>
<summary>Left Click</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/left%20click.gif" alt="Left Click" width="711" height="400"><br>
 <figcaption>Gesture for single left click</figcaption>
</details>

<details>
<summary>Right Click</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/right%20click.gif" alt="Right Click" width="711" height="400"><br>
 <figcaption>Gesture for single right click</figcaption>
</details>

<details>
<summary>Double Click</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/double%20click.gif" alt="Double Click" width="711" height="400"><br>
 <figcaption>Gesture for double click</figcaption>
</details>

<details>
<summary>Scrolling</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/Scrolling.gif" alt="Scrolling" width="711" height="400"><br>
 <figcaption>Dynamic Gestures for horizontal and vertical scroll. The speed of scroll is proportional to the distance moved by pinch gesture from start point. Vertical and Horizontal scrolls are controlled by vertical and horizontal pinch movements respectively.</figcaption>
</details>

<details>
<summary>Drag and Drop</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/drag%20and%20drop.gif" alt="Drag and Drop" width="711" height="400"><br>
 <figcaption>Gesture for drag and drop functionality. Can be used to move/tranfer files from one directory to other.</figcaption>
</details>

<details>
<summary>Multiple Item Selection</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/multiple%20item%20selection.gif" alt="Multiple Item Selection" width="711" height="400"><br>
 <figcaption>Gesture to select multiple items</figcaption>
</details>

<details>
<summary>Volume Control</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/Volume%20control.gif" alt="Volume Control" width="711" height="400"><br>
 <figcaption>Dynamic Gestures for Volume control. The rate of increase/decrease of volume is proportional to the distance moved by pinch gesture from start point. </figcaption>
</details>

<details>
<summary>Brightness Control</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/9be82cfc75aa4c04fff0e12dd4de853f9d83a101/demo_media/Brigntness%20Control.gif" alt="Brightness Control" width="711" height="400"><br>
 <figcaption>Dynamic Gestures for Brightness control. The rate of increase/decrease of brightness is proportional to the distance moved by pinch gesture from start point. </figcaption>
</details>

### Voice Assistant ( ***Proton*** ):
<details>
<summary>Launch / Stop  Gesture Recognition</summary>
<img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20launch%20stop%20gest.png" alt="launch stop gesture recognition" width="250" height="auto">
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
<img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20search.png" alt="proton search github" width="800" height="auto">
<ul>
  <li>
    <code>Proton search {text_you_wish_to_search}</code><br>
    Opens a new tab on Chrome Browser if it is running, else opens a new window. Searches the given text on Google.
  </li>
</ul>
</details>

<details>
<summary>Find a Location on Google Maps</summary>
 <img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20find%20location.png" alt="proton find location" width="800" height="auto">
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
<img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20list%20files.png" alt="proton list files" width="250" height="auto">&emsp;
 <img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20open.png" alt="proton open" width="250" height="auto">&emsp;
 <img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20go%20back.png" alt="proton go back" width="250" height="auto">
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
<img src="https://github.com/xenon-19/Gesture_Controller/blob/d49c868acc41ac6c89489bfd80e5e5015a8cb571/demo_media/voice%20commands/proton%20date%20time.png" alt="proton date / time" width="250" height="auto">
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
 <img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20copy.png" alt="proton copy" width="500" height="auto">
 <img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20paste.png" alt="proton paste" width="500" height="auto">
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
  <img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20bye%20wake%20up.png" alt="proton sleep / wake up" width="250" height="auto">
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
   <img src="https://github.com/xenon-19/Gesture_Controller/blob/4041eedc2f75fa2923902000b606a05a677629e8/demo_media/voice%20commands/proton%20exit.png" alt="proton exit" width="250" height="auto">
  <ul>
    <li>
      <code> Proton Exit </code> <br>
      Terminates the voice assisstant thread. GUI window needs to be closed manually.
    </li>
  </ul>
</details>

# Getting Started

  ### Pre-requisites
  
  Python: (3.6 - 3.8.5)<br>
  Anaconda Distribution: To download click [here](https://www.anaconda.com/products/individual).
  
  ### Procedure
  ```bash
  git clone https://github.com/xenon-19/Gesture-Controlled-Virtual-Mouse.git
  ```
  For detailed information about cloning visit [here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository).
  
  Step 1: 
  ```bash
  conda create --name gest python=3.8.5
  ```
  
  Step 2:
  ```bash
  conda activate gest
  ```
  
  Step 3:
  ```bash
  pip install -r requirements.txt
  ```
  
  Step 4:
  ```bash 
  conda install PyAudio
  ```
  ```bash 
  conda install pywin32
  ```
  
  Step 5:
  ``` 
  cd to the GitHub Repo till src folder
  ```
  Command may look like: `cd C:\Users\.....\Gesture-Controlled-Virtual-Mouse\src`
  
  Step 6:
  
  For running Voice Assistant:
  ```bash 
  python Proton.py
  ```
  ( You can enable Gesture Recognition by using the command "Proton Launch Gesture Recognition" )
  
  Or to run only Gesture Recognition without the voice assisstant:
  
  Uncomment last 2 lines of Code in the file `Gesture_Controller.py`
  ```bash 
  python Gesture_Controller.py
  ```
  

  
# Collaborators
  | |  |  |  |  |
  | ------------- | ------------- | ------------- | ------------- | ------------- |
  | Viral Doshi | [GitHub](https://github.com/Viral-Doshi) | Email | [LinkedIn](https://www.linkedin.com/in/viral-doshi-5a7737190/) | Instagram |
  | Nishiket Bidawat | [Github](https://github.com/xenon-19) | [Email](mailto:bidawatnishiket@gmail.com) | [LinkedIn](https://www.linkedin.com/in/nishiket-bidawat-74b419193/) | [Instagram](https://myanimelist.net/profile/Xenon1901) |
  | Ankit Sharma | [GitHub](https://github.com/ankit-4129) | [Email](mailto:ankitsharma.rbt@gmail.com) | LinkedIn | Instagram |
  | Parth Sakariya | [Github](https://github.com/parth-12) | [Email](mailto:parthsakariya12@icloud.com) | [LinkedIn](https://www.linkedin.com/in/parth-sakariya-1886b2193/) | [Instagram](https://www.instagram.com/parth_sak12/) |
  
