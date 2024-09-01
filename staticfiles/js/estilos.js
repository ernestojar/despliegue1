function submitForm() {
    // Obtener el formulario por su ID
    var form = document.getElementById('my-form-id'); // Reemplaza 'my-form-id' con el ID real de tu formulario
    
    // Crear un nuevo objeto FormData para recopilar los datos del formulario
    var formData = new FormData(form);
    
    // Realizar la solicitud AJAX para enviar los datos del formulario
    fetch('/ruta-de-tu-script', { // Reemplaza '/ruta-de-tu-script' con la ruta donde deseas enviar los datos
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Aquí puedes manejar la respuesta exitosa, como redireccionar a otra página
    })
    .catch((error) => {
        console.error('Error:', error);
        // Manejo de errores
    });
    
    // Evitar el comportamiento predeterminado del enlace
    event.preventDefault();
}



document.addEventListener('DOMContentLoaded', function() {
    var btBusc = document.getElementById('bt-busc');
    var form = document.querySelector('form'); // Asume que tu botón está dentro de un formulario
  
    btBusc.addEventListener('click', function(e) {
      e.preventDefault(); // Evita el comportamiento predeterminado del botón
      form.submit(); // Envía el formulario manualmente
    });
  });
  