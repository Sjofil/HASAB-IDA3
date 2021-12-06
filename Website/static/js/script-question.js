
const submitButton = document.getElementById("next");
const totalPages = document.getElementById("totalPages").childElementCount;

window.addEventListener('input', function() {
    var page = getRequestVariable("page");
    var pageNumber = parseInt(page);
    if(pageNumber > 1){
          document.getElementById("back").disabled=false; 
    }else {
        document.getElementById("back").disabled=true;
    }
  
  })

function submitForm(){
document.location.href="last.html";
}

function saveQuestion(name, value) {
    let answers = getCookie("answers");
    if (answers == ""){
        answers = {}
    } else {
        answers = JSON.parse(answers);
    }

    answers[name] = value;
    setCookie("answers", JSON.stringify(answers), 1);
}

function nextQuest(button, nextQuestion){
    if(button.value == "numberInput")
    {
        saveQuestion(button.name, document.getElementById("numberInput").valueAsNumber);
    }
    else {
        saveQuestion(button.name, button.value);
    }
    goToQuestion(nextQuestion);
}

function back(questionID) {
    let jsonData = { "previousQuestion": questionID }
    $.ajax({
        url: "/question",
        type: 'POST',
        contentType: "application/json",
        data : JSON.stringify(jsonData),
        success: function(result) {
            document.location.reload(false)
        }
    });
}


function goToQuestion(questionID) {
    let jsonData = { "nextQuestion": questionID };
    $.ajax({
        url: "/question",
        type: 'POST',
        contentType: "application/json",
        data : JSON.stringify(jsonData),
        success: function(result) {
            document.location.reload(false)
        }
    });
}

function sendCookie(){
    let answers = getCookie("answers");
    console.log(answers);
    $.ajax({
        url: "/send-form",
        type: 'POST',
        contentType: "application/json",
        data : answers,
    });
    //Dålig lösning men orkar inte, borde kolla om vi faktiskt lyckas göra vårt post request
    document.location.href="/last";
}

    function getSelectedValue(){
        var selectedValue = document.getElementById("answer").value;
        console.log(selectedValue);
    }

    