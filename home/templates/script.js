document.addEventListener("DOMContentLoaded", function () {
    const products = document.querySelectorAll(".product");

    // Resaltar productos al pasar el mouse por encima
    products.forEach(product => {
        product.addEventListener("mouseenter", () => {
            product.style.backgroundColor = "#444";
        });

        product.addEventListener("mouseleave", () => {
            product.style.backgroundColor = "#222";
        });
    });

    // Mostrar mensaje de confirmación al hacer clic en "Ver Detalles"
    const detailButtons = document.querySelectorAll(".btn");
    
    detailButtons.forEach(button => {
        button.addEventListener("click", (event) => {
            event.preventDefault();
            const productName = button.parentNode.querySelector("h3").textContent;
            const confirmed = confirm(`Do you want to see details? ${productName}?`);
            if (confirmed) {
                // Aquí puedes redirigir a la página de detalles del producto
            }
        });
    });
});
