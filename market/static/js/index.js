const form = document.querySelector('#market-form');
const submitBtn = document.querySelector('#submit-btn');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const selectedProducts = document.querySelectorAll('input[type="checkbox"]:checked');
    const data = {
        user_name: document.querySelector('#user_name').value,
        products: [],
        quantities: []
    };

    selectedProducts.forEach((product) => {
        const productId = product.value;
        const quantityInput = document.querySelector(`#quantity_${productId}`);
        const quantity = quantityInput.value;
        data.products.push(productId);
        data.quantities.push(quantity);
    });

    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/');
    xhr.setRequestHeader('Content-Type', 'application/json');  // Добавляем заголовок Content-Type
    xhr.onload = () => {
        window.location.href = xhr.responseURL;
    };
    xhr.send(JSON.stringify(data));
});