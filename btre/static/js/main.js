const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Fade out error message prompt after 3seconds
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);