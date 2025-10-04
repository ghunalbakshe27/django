document.getElementById("username").addEventListener("keydown",function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("password").focus();
    }
});
document.getElementById("password").addEventListener("keydown",function(event) {
    if (event.key === "Enter") {
        event.preventDefault();
        document.getElementById("loginbtn").focus();
    }
});
