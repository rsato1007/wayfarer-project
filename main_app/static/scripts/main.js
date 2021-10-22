let editForm = document.querySelector(".three-dot-editing");
let postOptionsMenuEl = document.querySelector(".individual-post-options");

editForm.addEventListener('click', (e) => {
    postOptionsMenuEl.style.display = "block";
})

postOptionsMenuEl.addEventListener('click', (e) => {
    const cancelEl = document.getElementById("cancel");
    if (e.target === cancelEl) {
        postOptionsMenuEl.style.display = "none";
    }
})