const submitButton = document.getElementById("next");
const input = document.getElementById("answer");


//disablar knappen tills man skrivit in något
console.log(input);

input.addEventListener('keypress', (e) => {

    console.log(e.currentTarget.value);

    const value = e.currentTarget.value;
    if(value === ""){
        submitButton.disabled = true;
    } else {
        submitButton.disabled=false;
    }
    
});

function submitForm(){
document.location.href="last.html";
}

function nextQuest(){
    document.location.href="/question2";
}

console.log(555555);