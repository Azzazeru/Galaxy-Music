const url = "https://gmad.up.railway.app/api/"
// const url = "http://127.0.0.1:8000/api/"

const d = document,
    $table = d.querySelector('#table tbody'),
    $template = d.getElementById('template').content,
    $form = d.querySelector('.crud-form')
    $fragment = d.createDocumentFragment();
    $presupuesto = d.getElementById('presupuesto')

const getAll = async () => {
    try {
        let res = await axios.get(url + 'productos/');
        let json = await res.data;

        json.forEach(p => {
            if(!p.estado){
            $template.querySelector(".estado").textContent = p.estado ? "Aprobado" : "No Aprobado";
            $template.querySelector(".instrumento-disco").textContent = p.disco ? "Disco" : p.instrumento ? "Instrumento" : "";
            $template.querySelector(".modelo-titulo").textContent = p.disco?.titulo || p.instrumento?.modelo || "";
            $template.querySelector(".precio").textContent = p.precio;
            $template.querySelector(".check").dataset.id = p.id_producto;

            let $clone = d.importNode($template, true);
            $fragment.appendChild($clone)
            }
            ;
        });

        $table.appendChild($fragment);

    } catch (error) {
        console.error(error);
    }
}

const getPresupuesto = async () => {
    try {
        let res = await axios.get(url + 'presupuesto/1');
        let presupuesto = await res.data;
        $presupuesto.textContent = presupuesto.presupuesto;
    } catch (error) {
        console.error(error);
    }
};


d.addEventListener("DOMContentLoaded", async () => {
    await getAll();
    await getPresupuesto();
});

d.addEventListener("click", async e => {
    if (e.target.matches(".check")) {
        const confirmacion = confirm("¿Estás seguro que quieres aprobar este producto?");
        if (confirmacion) {
            e.preventDefault();
            const id = e.target.dataset.id;
            if (id) {
                try {
                    // Obtener el producto
                    let res = await axios.get(url + `productos/${id}/`);
                    let producto = await res.data;

                    // Aprobar el producto
                    producto.estado = true;

                    let options = {
                        method: "PUT",
                        headers: {
                            "content-type": "application/json;charset=utf-8"
                        },
                        data: JSON.stringify(producto)
                    };
                    res = await axios(url + `productos/${id}/`, options);
                    let json = await res.data;

                    // Obtener el presupuesto actual
                    res = await axios.get(url + 'presupuesto/1/');
                    let presupuesto = await res.data;

                    // Restar el precio del producto del presupuesto
                    presupuesto.presupuesto -= producto.precio;

                    // Actualizar el presupuesto
                    options = {
                        method: "PUT",
                        headers: {
                            "content-type": "application/json;charset=utf-8"
                        },
                        data: JSON.stringify(presupuesto)
                    };
                    res = await axios(url + 'presupuesto/1/', options);
                    json = await res.data;

                    // Actualizar el contenido de la página
                    location.reload(true);
                } catch (error) {
                    console.error(error);
                }
            }
        }
    }
});