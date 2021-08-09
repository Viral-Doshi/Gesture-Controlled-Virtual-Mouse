document.getElementById("userInputButton").addEventListener("click", getUserInput , false);

eel.expose(addUserMsg);
eel.expose(addAppMsg);

function addUserMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message from read">' + msg + '</div>';
    element.scrollTo = 100;
}

function addAppMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message to read">' + msg + '</div>';
    //element.scrollTop = element.scrollHeight - element.clientHeight;
}

function getUserInput() {
    element = document.getElementById("userInput");
    msg = element.value;
    console.log(document.getElementById("messages").scrollTop);
    if (msg.length != 0) {
        element.value = "";
        addUserMsg(msg);
        eel.getUserInput(msg);
    }
}