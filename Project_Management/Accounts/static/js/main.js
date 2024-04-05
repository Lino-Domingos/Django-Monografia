let arrows = document.querySelectorAll(".arrow");
for (let i = 0; i < arrows.length; i++) {
    arrows[i].addEventListener("click", function(e) {
        let arrowParent = e.target.parentElement.parentElement; // Selecionando o elemento pai do arrow
        arrowParent.classList.toggle("showMenu");
    });
}

let sidebar = document.querySelector(".sidebar");
let sidebarBtn = document.querySelector(".bx-menu");
sidebarBtn.addEventListener("click", function() {
    sidebar.classList.toggle("close");
});
