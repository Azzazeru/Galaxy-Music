const url = "https://gmad.up.railway.app/api/"
// const url = "http://127.0.0.1:8000/api/"

const d = document, 
    $table = d.querySelector('#table tbody'),
    $template = d.getElementById('template').content,
    $form = d.querySelector('.crud-form')
    $fragment = d.createDocumentFragment();

const getAll = async () => {
    try {
        let res = await axios.get(url + 'productos/') , json = await res.data;
        console.log(json)
        json.forEach(p => {
            if(p.disco && !p.aprobado){
                $template.querySelector(".id").textContent = p.id_producto;
                $template.querySelector(".estado").textContent = p.aprobado ? "Aprobado" : "No Aprobado";
                $template.querySelector(".instrumento-disco").textContent = "Disco"
                $template.querySelector(".modelo-titulo").textContent = p.disco.titulo;

                $template.querySelector(".check").dataset.id = p.id_producto;

                let $clone = d.importNode($template, true);
                $fragment.appendChild($clone);
            } else if(p.instrumento && !p.aprobado){
                $template.querySelector(".id").textContent = p.id_producto;
                $template.querySelector(".estado").textContent = p.aprobado ? "Aprobado" : "No Aprobado";
                $template.querySelector(".instrumento-disco").textContent = "Instrumento"
                $template.querySelector(".modelo-titulo").textContent = p.instrumento.modelo;

                $template.querySelector(".check").dataset.id = p.id_producto;

                let $clone = d.importNode($template, true);
                $fragment.appendChild($clone);
            }
        })

        $table.appendChild($fragment);

    } catch (error) {
        
    }
}

d.addEventListener("click", async e => {
    if(e.target.matches(".check")){
        const confirmacion = confirm("¿Estás seguro que quieres aprobar este producto?");
        if (confirmacion) {
            e.preventDefault();
            const id = e.target.dataset.id;
            if(id){
                try {
                    let res = await axios.get(url + `productos/${id}/`);
                    let producto = await res.data;

                    producto.aprobado = true;

                    let options = {
                        method: "PUT",
                        headers: {
                            "content-type": "application/json;charset=utf-8"
                        },
                        data: JSON.stringify(producto)
                    };
                    res = await axios(url + `productos/${id}/`, options);
                    let json = await res.data;
                    location.reload(true);
                } catch (error) {
                    console.error(error);
                }
            }
        }
    }
});


d.addEventListener("DOMContentLoaded", getAll);