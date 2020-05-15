let message = document.getElementById('dayMessage');

let date = new Date();
let currentHour = date.getHours();

if (currentHour < 12) {
    message.textContent = '⛅ Good morning, ';
} else if (currentHour < 18) {
    message.textContent = '☀ Good afternoon, ';
} else {
    message.textContent = '🌃 Good evening, ';
}