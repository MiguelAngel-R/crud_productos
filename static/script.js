document.addEventListener('DOMContentLoaded', cargarProductos);

let productoEditandoId = null;

function cargarProductos() {
    fetch('/productos')
        .then(response => response.json())
        .then(data => {
            const productos = document.querySelector('#products');
            productos.innerHTML = '';
            data.forEach(producto => {
                productos.innerHTML += `
                    <div class="producto">
                        <p>${producto.nombre}</p>
                        <p>${producto.precio}</p>
                        <p>${producto.descripcion}</p>
                        <div class="botones">
                            <button onclick="editarProducto(${producto.id})">Editar</button>
                            <button onclick="eliminarProducto(${producto.id})">Eliminar</button>                        
                        </div>
                    </div>                    
                `;
            });
        });
}

function guardarProducto() {
    const producto = {
        nombre: document.getElementById('nombre').value,
        precio: parseFloat(document.getElementById('precio').value),
        descripcion: document.getElementById('descripcion').value
    };

    const url = productoEditandoId ? `/productos/${productoEditandoId}` : '/productos';
    const method = productoEditandoId ? 'PUT' : 'POST';

    fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(producto)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').textContent = data.mensaje;
        cargarProductos();
        limpiarFormulario();
        productoEditandoId = null;
    });
}

function editarProducto(id) {
    fetch(`/productos/${id}`)
        .then(response => response.json())
        .then(producto => {
            productoEditandoId = id;
            document.getElementById('nombre').value = producto.nombre;
            document.getElementById('precio').value = producto.precio;
            document.getElementById('descripcion').value = producto.descripcion;
            window.scrollTo(0, 0);
        });
}

function eliminarProducto(id) {
    if (confirm('¿Eliminar este producto?')) {
        fetch(`/productos/${id}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                document.getElementById('message').textContent = data.mensaje;
                cargarProductos();
            });
    }
}

function limpiarFormulario() {
    document.getElementById('nombre').value = '';
    document.getElementById('precio').value = '';
    document.getElementById('descripcion').value = '';
    productoEditandoId = null;
}
