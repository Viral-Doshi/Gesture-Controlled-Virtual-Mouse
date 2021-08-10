
document.getElementById("userInputButton").addEventListener("click", getUserInput, false);

eel.expose(addUserMsg);
eel.expose(addAppMsg);

function addUserMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message from ready rtol"><div>' + msg + '</div></div>';
    element.scrollTop = element.scrollHeight - element.clientHeight;
    //add delay for animation to complete and then modify class to => "message from"
    setTimeout(() => { element.lastChild.className = "message from"; }, 500);
    //addAppMsg(msg);
}

function addAppMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message to ready ltor"><div>' + msg + '</div></div>';
    element.scrollTop = element.scrollHeight - element.clientHeight;
    //add delay for animation to complete and then modify class to => "message to"
    setTimeout(() => { element.lastChild.className = "message to"; }, 500);
}

function getUserInput() {
    element = document.getElementById("userInput");
    msg = element.value;
    if (msg.length != 0) {
        element.value = "";
        addUserMsg(msg);
        eel.getUserInput(msg);
    }
}