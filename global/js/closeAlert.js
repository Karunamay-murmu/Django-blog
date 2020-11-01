const button = document.querySelector('#close-alert-icon');
const alert = document.querySelector('#alert-box');

(function removeAlert() {
    button.onclick = function () {
        alert.remove();
    }
    window.setTimeout(() => {
        alert.remove()
    }, 5000)
})()