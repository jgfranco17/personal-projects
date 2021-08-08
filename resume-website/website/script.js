// modal
const signupButton = document.querySelector('#button1');
const modalBg = document.querySelector('.modal-background');
const modal = document.querySelector('.modal');

signupButton.addEventListener('click', () => {
    modal.classList.add('is-active');
    console.log('modal is active');
})

modalBg.addEventListener('click', () => {
    modal.classList.remove('is-active');
})