
//user clicked button
document.getElementById("userInputButton").addEventListener("click", getUserInput, false);
//user pressed enter '13'
document.getElementById("userInput").addEventListener("keyup", function (event) {
    if (event.keyCode === 13) {
        //cancel the default action
        event.preventDefault();
        //process event
        getUserInput();
    }
});

eel.expose(addUserMsg);
eel.expose(addAppMsg);


function addUserMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message from ready rtol">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    //add delay for animation to complete and then modify class to => "message from"
    index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message from"), 500);
}

function addAppMsg(msg) {
    element = document.getElementById("messages");
    element.innerHTML += '<div class="message to ready ltor">' + msg + '</div>';
    element.scrollTop = element.scrollHeight - element.clientHeight - 15;
    //add delay for animation to complete and then modify class to => "message to"
    index = element.childElementCount - 1;
    setTimeout(changeClass.bind(null, element, index, "message to"), 500);
}

function changeClass(element, index, newClass) {
    console.log(newClass +' '+ index);
    element.children[index].className = newClass;
}


function getUserInput() {
    element = document.getElementById("userInput");
    msg = element.value;
    if (msg.length != 0) {
        element.value = "";
        eel.getUserInput(msg);
    }
}