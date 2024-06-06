const url = "https://gmad.up.railway.app/api/"
// const url = "http://127.0.0.1:8000/api/"

const d = document,
    $discosTable = d.querySelector('#discos-table tbody'),
    $instrumentosTable = d.querySelector('#instrumentos-table tbody'),
    $discoTemplate = d.getElementById('disco-template').content,
    $instrumentoTemplate = d.getElementById('instrumento-template').content,
    $discoFragment = d.createDocumentFragment(),
    $instrumentoFragment = d.createDocumentFragment();

const getAll = async () => {
    try {
        let res = await axios.get(url + 'productos/') , json = await res.data;
        
        json.forEach(p => {
            if (p.disco) {
                $discoTemplate.querySelector(".id").textContent = p.id_producto;
                $discoTemplate.querySelector(".precio").textContent = p.precio;
                $discoTemplate.querySelector(".stock").textContent = p.stock;
                $discoTemplate.querySelector(".estado").textContent = p.aprobado ? "Aprobado" : "No Aprobado";
                $discoTemplate.querySelector(".titulo").textContent = p.disco.titulo;
                $discoTemplate.querySelector(".sello").textContent = p.disco.detalle_disco?.sello_discografico?.nombre;
                $discoTemplate.querySelector(".artista").textContent = p.disco.detalle_disco?.artista?.nombre;

                let $clone = d.importNode($discoTemplate, true);
                $discoFragment.appendChild($clone);
            } else if (p.instrumento) {
                $instrumentoTemplate.querySelector(".id").textContent = p.id_producto;
                $instrumentoTemplate.querySelector(".precio").textContent = p.precio;
                $instrumentoTemplate.querySelector(".stock").textContent = p.stock;
                $instrumentoTemplate.querySelector(".estado").textContent = p.aprobado? "Aprobado" : "No Aprobado";
                $instrumentoTemplate.querySelector(".modelo").textContent = p.instrumento.modelo;
                $instrumentoTemplate.querySelector(".tipo").textContent = p.instrumento.detalle_instrumento?.tipo_instrumento?.tipo;
                $instrumentoTemplate.querySelector(".marca").textContent = p.instrumento.detalle_instrumento?.marca?.nombre;

                let $clone = d.importNode($instrumentoTemplate, true);
                $instrumentoFragment.appendChild($clone);
            }
        });

        $discosTable.appendChild($discoFragment);
        $instrumentosTable.appendChild($instrumentoFragment);
    } catch (error) {
        console.error(error);
    }
}


d.addEventListener("DOMContentLoaded", getAll);