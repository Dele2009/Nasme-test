const tooltipTriggerList = document.querySelectorAll(
  '[data-bs-toggle="tooltip"]'
);
const tooltipList = [...tooltipTriggerList].map(
  (tooltipTriggerEl) => new bootstrap.Tooltip(tooltipTriggerEl)
);

const collapseToggler = document.querySelectorAll('[data-bs-toggle="collapse"]');
const sidebar = document.getElementById("sidebar");
const mainContent = document.getElementById("main-content");

// const toggleSideBar = () => {
//     if (isSideBarActive) return;
//     sidebar.classList.toggle('active');
// }

const onMouseLeave = () => {
  sidebar.classList.remove("active");

  console.log(collapseToggler);
  if (collapseToggler.length) {
    collapseToggler.forEach((toggler) => closeModal(toggler));
  }
};

sidebar.addEventListener("mouseenter", () => sidebar.classList.add("active"));
sidebar.addEventListener("mouseleave", onMouseLeave);

document.getElementById("togglerLg").addEventListener("click", () => {
  sidebar.classList.toggle("active");
});

function closeModal(toggler) {
  const targetCollapse = toggler.getAttribute('href');
  document.querySelector(targetCollapse).classList.remove('show');
}

