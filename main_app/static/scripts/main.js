let editForm = document.getElementsByClassName("three-dot-editing");
let postOptionsMenuEl = document.getElementsByClassName("individual-post-options");
const cancelEl = document.getElementsByClassName("cancel");

for (let i = 0; i < editForm.length; i++) {
    editForm[i].addEventListener('click', (e) => {
        postOptionsMenuEl[i].style.display = "block";
    })
    
    postOptionsMenuEl[i].addEventListener('click', (e) => {
        if (e.target === cancelEl[i]) {
            postOptionsMenuEl[i].style.display = "none";
        }
    })
}

// We'll use this code to eventually design a nav bar for mobile devices.
if (screen.width <= 550) {
    console.log("The screen is small now");
} else {
    console.log("The screen is not so small now.");
}