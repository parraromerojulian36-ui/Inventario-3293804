const API_URL = 'http://127.0.0.1:8000/Inventario/api/ProductoApi/';

fetch(API_URL)
    .then(respuesta => respuesta.json())
    .then(productos => {
        let filas = '';

        productos.forEach(producto => {
            filas += `
                <tr>
                    <td>${producto.codigo_barras}</td>
                    <td>${producto.nombre_producto}</td>
                    <td>${producto.categoria}</td>
                    <td>$${producto.precio_venta}</td>
                    <td>${producto.stock_actual}</td>
                    <td>${producto.estado}</td>
                </tr>
            `;
        });

        document.getElementById('cuerpo').innerHTML = filas;
    });
