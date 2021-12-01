
const submitButton = document.getElementById("next");
const totalPages = document.getElementById("totalPages").childElementCount;

window.addEventListener('load', function() {
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

function forward(){
    var page = getRequestVariable("page");
    var pageNumber = parseInt(page);
    console.log("Page: " + page + " Total: " + totalPages);
    if(page != undefined && page != NaN) 
    {
        if(totalPages > pageNumber){
            document.location.href="/question?page=" + (pageNumber + 1);
        }
        else if(totalPages == pageNumber) {
            console.log(getCookie("answers"));
            document.location.href="/send-form";
        }
    }
    else
    {
        document.location.href="/question?page=2";
        let answers = [];
        answers[0] = $('form').serialize();
        setCookie("answers", JSON.stringify(answers), 1);
    }

}

function saveQuestion(button) {
    let answers = getCookie("answers");
    if (answers == ""){
        answers = {}
    } else {
        answers = JSON.parse(answers);
    }

    answers[button.name] = button.value;
    setCookie("answers", JSON.stringify(answers), 1);
}

function nextQuest(button, nextQuestion){
    saveQuestion(button);
    goToQuestion(nextQuestion)
}

function goToQuestion(questionID) {
    let jsonData = JSON.stringify(questionID)
    $.ajax({
        url: "/question",
        type: 'POST',
        contentType: "application/json",
        data : jsonData,
        success: function(result) {
            document.location.reload(false)
        }
    });
}

function sendCookie(){
    let answers = getCookie("answers");
    console.log(answers)
    $.ajax({
        url: "/send-form",
        type: 'POST',
        contentType: "application/json",
        data : answers,
    });
    //Dålig lösning men orkar inte, borde kolla om vi faktiskt lyckas göra vårt post request
    document.location.href="/last";
}

function back(){
    var page = getRequestVariable("page");
    var pageNumber = parseInt(page);
    if(page != undefined && page != NaN) 
    {
        if(pageNumber > 1){
            document.location.href="/question?page=" + (pageNumber - 1);
        }
        
    }
    else
    {
        document.location.href="/question?page=2"
    }

}

    function getSelectedValue(){
        var selectedValue = document.getElementById("answer").value;
        console.log(selectedValue);
    }

    