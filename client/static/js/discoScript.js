const url = "https://gmad.up.railway.app/api/"
// const url = "http://127.0.0.1:8000/api/"

const d = document,
  $title = d.querySelector('.crud-title'),
  $discosTable = d.querySelector("#discos-table tbody"),
  $discoTemplate = d.getElementById("disco-template").content,
  $discoFragment = d.createDocumentFragment();
  $discoForm = d.querySelector(".crud-form");

const getAll = async () => {
  try {
    let res = await axios.get(url + "productos/"),
      json = await res.data;

    // console.log(json);

    json.forEach((p) => {
      if (p.disco) {
        $discoTemplate.querySelector(".id").textContent = p.disco.id_disco;
        $discoTemplate.querySelector(".precio").textContent = p.precio;
        $discoTemplate.querySelector(".stock").textContent = p.stock;
        $discoTemplate.querySelector(".titulo").textContent = p.disco.titulo;
        $discoTemplate.querySelector(".sello").textContent = p.disco.detalle_disco?.sello_discografico?.nombre;
        $discoTemplate.querySelector(".genero").textContent = p.disco.detalle_disco?.genero_musical?.nombre;
        $discoTemplate.querySelector(".artista").textContent = p.disco.detalle_disco?.artista?.nombre;
    
        // Ajustar la configuración del dataset
        $discoTemplate.querySelector(".edit").dataset.id = p.disco.id_disco;
        $discoTemplate.querySelector(".edit").dataset.id_producto = p.id_producto;
        $discoTemplate.querySelector(".edit").dataset.id_detalle_disco = p.disco.detalle_disco?.id_detalle_disco;
        $discoTemplate.querySelector(".edit").dataset.titulo = p.disco.titulo;
        $discoTemplate.querySelector(".edit").dataset.sello = p.disco.detalle_disco?.sello_discografico?.id_sello_discografico || '';
        $discoTemplate.querySelector(".edit").dataset.genero = p.disco.detalle_disco?.genero_musical?.id_genero_musical || '';
        $discoTemplate.querySelector(".edit").dataset.artista = p.disco.detalle_disco?.artista?.id_artista || '';
        $discoTemplate.querySelector(".edit").dataset.precio = p.precio;
        $discoTemplate.querySelector(".edit").dataset.stock = p.stock;
        $discoTemplate.querySelector(".delete").dataset.id = p.disco.id_disco;
        $discoTemplate.querySelector(".delete").dataset.id_producto = p.id_producto;
        $discoTemplate.querySelector(".delete").dataset.id_detalle_disco = p.disco.detalle_disco?.id_detalle_disco;
        $discoTemplate.querySelector(".delete").dataset.titulo = p.disco.titulo;
        
        let $clone = d.importNode($discoTemplate, true);
        $discoFragment.appendChild($clone);
      }
    });
    
    $discosTable.appendChild($discoFragment);
    
  } catch (error) {
    console.error(error);
  }
};

d.addEventListener("DOMContentLoaded", getAll);

d.addEventListener("submit", async e => {
  if(e.target === $discoForm){
    e.preventDefault();

    if(!e.target.id.value){
      try {
        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
          data: JSON.stringify({
                sello_discografico_id: e.target.sello.value,
                genero_musical_id: e.target.genero.value,
                artista_id: e.target.artista.value,
              })
            }
            let res = await axios(url + 'detalles_discos/', options);
            let json = await res.data;

      } catch (error) {
        console.error(error);
      }

      try {
        let res = await axios(url + "detalles_discos/");
        let json = await res.data;
        lastId = json[json.length-1].id_detalle_disco;

        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
          data: JSON.stringify({
                titulo: e.target.titulo.value,
                detalle_disco_id: lastId
              })
            }
        res = await axios(url + "discos/", options);
        json = await res.data;
      } catch (error) {
        console.error(error);
      }
      try {
        let res = await axios(url + "discos/");
        let json = await res.data;
        lastId = json[json.length-1].id_disco;

        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
          data: JSON.stringify({
                disco_id: lastId,
                instrumento_id: null,
                precio: e.target.precio.value,
                stock: e.target.stock.value
              })
            }
        res = await axios(url + "productos/", options);
        json = await res.data;
  
        location.reload(true);
      } catch (error) {
        console.error(error);
      }
    }else{

    try {
      let options = {
        method: "PUT",
        headers: {
          "content-type": "application/json;charset=utf-8"
        },
        data: JSON.stringify({
              sello_discografico_id: e.target.sello.value,
              genero_musical_id: e.target.genero.value,
              artista_id: e.target.artista.value,
            })
          }
      let res = await axios(url + `detalles_discos/${e.target.id_detalle_disco.value}/` ,options);
      let json = await res.data;

    } catch (error) {
      console.error(error);
    }

    try {
      let res = await axios(url + "discos/");
      let json = await res.data;

      let options = {
        method: "PUT",
        headers: {
          "content-type": "application/json;charset=utf-8"
        },
        data: JSON.stringify({
              titulo: e.target.titulo.value,
              detalle_disco_id: e.target.id_detalle_disco.value
            })
          }
      res = await axios(url + `discos/${e.target.id.value}/`, options);
      json = await res.data;
    } catch (error) {
      console.error(error);
    }
    try {
      let res = await axios(url + "discos/");
      let json = await res.data;
      lastId = json[json.length-1].id_disco;

      let options = {
        method: "PUT",
        headers: {
          "content-type": "application/json;charset=utf-8"
        },
        data: JSON.stringify({
              disco_id: e.target.id.value,
              instrumento_id: null,
              precio: e.target.precio.value,
              stock: e.target.stock.value
            })
          }
      res = await axios(url + `productos/${e.target.id_producto.value}/`, options);
      json = await res.data;

      location.reload(true);
    } catch (error) {
      console.error(error);
    }
    }
  }else{
    }
  });


d.addEventListener("click", async e => {
  if(e.target.matches(".edit")){
    $title.textContent = "Editar Disco";
    $discoForm.titulo.value = e.target.dataset.titulo;
    $discoForm.sello.value = e.target.dataset.sello;
    $discoForm.genero.value = e.target.dataset.genero;
    $discoForm.artista.value = e.target.dataset.artista;
    $discoForm.precio.value = e.target.dataset.precio;
    $discoForm.stock.value = e.target.dataset.stock;
    $discoForm.id_detalle_disco.value = e.target.dataset.id_detalle_disco;
    $discoForm.id.value = e.target.dataset.id;
    $discoForm.id_producto.value = e.target.dataset.id_producto;
  }

  if(e.target.matches(".delete")){
    let isDelete = confirm(`¿Estas seguro que deseas eliminar el disco: ${e.target.dataset.titulo} con id: ${e.target.dataset.id}?`);
    if(isDelete){
      // console.log("Hola")
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
        }
        es = await axios(url + `productos/${e.target.dataset.id_producto}/`, options);
        json = await res.data;
      } catch (error) {
        
      }
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
        }
        res = await axios(url + `discos/${e.target.dataset.id}/`);
        json = await res.data;
      } catch (error) {
        
      }
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
        }
        res = await axios(url + `detalles_discos/${e.target.dataset.id_detalle_disco}/`, options);
        json = await res.data;

        location.reload(true);

      } catch (error) {
        
      }
      
    }
  }

})

d.addEventListener("DOMContentLoaded", function () {
  // Referencia al elemento select
  const selectElement = document.getElementById("sello-select");

  // Función para poblar el select con opciones
  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.id_sello_discografico; // Ajusta esto según la estructura de tu objeto de la API
      option.textContent = item.nombre; // Ajusta esto según la estructura de tu objeto de la API
      selectElement.appendChild(option);
    });
  }

  // Llamada a la API REST usando Axios
  axios
    .get(url + "sellos_discograficos/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  // Referencia al elemento select
  const selectElement = document.getElementById("genero-select");

  // Función para poblar el select con opciones
  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.id_genero_musical; // Ajusta esto según la estructura de tu objeto de la API
      option.textContent = item.nombre; // Ajusta esto según la estructura de tu objeto de la API
      selectElement.appendChild(option);
    });
  }

  // Llamada a la API REST usando Axios
  axios
    .get(url + "generos_musicales/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  // Referencia al elemento select
  const selectElement = document.getElementById("artista-select");

  // Función para poblar el select con opciones
  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.id_artista; // Ajusta esto según la estructura de tu objeto de la API
      option.textContent = item.nombre; // Ajusta esto según la estructura de tu objeto de la API
      selectElement.appendChild(option);
    });
  }

  // Llamada a la API REST usando Axios
  axios
    .get(url + "artistas/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

