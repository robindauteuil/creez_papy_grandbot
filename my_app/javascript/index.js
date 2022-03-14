

let question = document.getElementById('chat-user')
console.log(question)

const Http = new XMLHttpRequest();
const url='http://127.0.0.1:5000/result';
Http.open("GET", url);
Http.send();

Http.onreadystatechange = (e) => {
  console.log(Http.responseText)
  }