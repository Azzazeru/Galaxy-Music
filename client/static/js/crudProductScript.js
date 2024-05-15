url = "https://galaxy-music-ad.up.railway.app/api/products/"
const d = document,
    $table = d.querySelector('.crud-table'),
    $form = d.querySelector('.crud-form'),
    $title = d.querySelector('.crud-title'),
    $template = d.getElementById('crud-template').content,
    $fragment = d.createDocumentFragment();

const getAll = async () => {
    try {
        let res = await axios.get(url),
            json = await res.data;

        console.log(json);

        json.forEach(el => {
            $template.querySelector(".id").textContent = el.productId;
            $template.querySelector(".name").textContent = el.name;
            $template.querySelector(".price").textContent = el.price;
            $template.querySelector(".edit").dataset.id = el.productId;
            $template.querySelector(".edit").dataset.name = el.name;
            $template.querySelector(".edit").dataset.price = el.price;
            $template.querySelector(".delete").dataset.id = el.productId;

            let $clone = d.importNode($template, true);
            $fragment.appendChild($clone);
        });

        $table.querySelector('tbody').appendChild($fragment);

    } catch (err) {
        let message = err.statusText || "Ocurrio un error";
        $table.insertAdjacentHTML("afterend", `<p><b>Error ${err.status}: ${message}</b></p>`);
    }
}

d.addEventListener("DOMContentLoaded", getAll);

d.addEventListener("submit", async e => {
    if (e.target === $form) {
        e.preventDefault();

        if (!e.target.id.value) {
            try {
                let options = {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json; charset=utf-8"
                    },
                    data: JSON.stringify({
                        name: e.target.name.value,
                        price: e.target.price.value
                    })
                },
                    res = await axios(url, options),
                    json = await res.data;

                    location.reload();

            } catch (err) {
                let message = err.statusText || "Ocurrio un error";
                $form.insertAdjacentHTML("afterend", `<p><b>Error ${err.status}: ${message}</b></p>`);
            }
        } else {
            try {
                let options = {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json; charset=utf-8"
                    },
                    data: JSON.stringify({
                        name: e.target.name.value,
                        price: e.target.price.value
                    })
                },
                    res = await axios(url + e.target.id.value + '/', options),
                    json = await res.data;

                    location.reload();

            } catch (err) {
                let message = err.statusText || "Ocurrio un error";
                $form.insertAdjacentHTML("afterend", `<p><b>Error ${err.status}: ${message}</b></p>`);
            }
        }
    }
});

d.addEventListener("click", async e => {
    if(e.target.matches(".edit")){
        $title.textContent = "Editar Producto";
        $form.name.value = e.target.dataset.name;
        $form.price.value = e.target.dataset.price;
        $form.id.value = e.target.dataset.id;
    }
    if(e.target.matches(".delete")){
        let isDelete = confirm(`Estas seguro de eliminar el id ${e.target.dataset.id}`)

    if(isDelete){
        //Delete
        try {
                let options = {
                    method: "DELETE",
                    headers: {
                        "Content-Type": "application/json; charset=utf-8"
                    }
                },
                    res = await axios(url + e.target.dataset.id + '/', options),
                    json = await res.data;

                    location.reload();

            } catch (err) {
                let message = err.statusText || "Ocurrio un error";
                alert(`Error ${err.status}: ${message}`);
            }
    }
    }
})