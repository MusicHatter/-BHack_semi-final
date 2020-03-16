 const restoreSection = document.querySelector(".restore-section");
 const inputLogin = document.querySelector(".input-login");
 const loginPasswordRestore = document.querySelector(".login-password-restore");
 const restoreReturn = document.querySelector(".restore-return");
 const registrationReturnSection = document.querySelector(".registration-return-section");

 function hideElem(elem) {
     elem.style.display = 'none';
 }

 function showElem(elem) {
     elem.style.display = 'block';
 }

 loginPasswordRestore.addEventListener('click', function () {
     hideElem(inputLogin);
     showElem(restoreSection);
 });

 restoreReturn.addEventListener('click', function () {
    hideElem(restoreSection);
    showElem(inputLogin);
 })