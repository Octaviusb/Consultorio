function openTab(event, tabName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.className += " active";
  }
  
  function establecerPassword() {
    const newPassword = document.getElementById("password").value;
    // Aquí puedes realizar las acciones que desees con la nueva contraseña
    console.log("Contraseña establecida:", newPassword);
    alert("Contraseña establecida correctamente");
  }
  
  // Mostrar la pestaña de administración por defecto al cargar la página
window.addEventListener("DOMContentLoaded", function() {
  openTab(event, 'adminTab');
});