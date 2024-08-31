// static/js/tabs.js

document.addEventListener('DOMContentLoaded', function () {
    const tabHeaders = document.querySelectorAll('.tab-headers li a');
    const tabs = document.querySelectorAll('.tab');

    tabHeaders.forEach(header => {
        header.addEventListener('click', function (e) {
            e.preventDefault();

            // Remove active class from all headers and tabs
            tabHeaders.forEach(h => h.parentElement.classList.remove('active'));
            tabs.forEach(tab => tab.classList.remove('active'));

            // Add active class to the clicked header and corresponding tab
            this.parentElement.classList.add('active');
            const target = document.querySelector(this.getAttribute('href'));
            target.classList.add('active');
        });
    });
});
