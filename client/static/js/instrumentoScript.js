const url = "https://gmad.up.railway.app/api/"
// const url = "http://127.0.0.1:8000/api/"

const d = document,
  $title = d.querySelector('.crud-title'),
  $instrumentosTable = d.querySelector("#instrumentos-table tbody"),
  $instrumentoTemplate = d.getElementById("instrumento-template").content,
  $instrumentoFragment = d.createDocumentFragment(),
  $instrumentoForm = d.querySelector(".crud-form");

const getAll = async () => {
  try {
    let res = await axios.get(url + "productos/"),
      json = await res.data;

    // console.log(json);

    json.forEach((p) => {
      if (p.instrumento) {
        $instrumentoTemplate.querySelector(".id").textContent = p.instrumento.id_instrumento;
        $instrumentoTemplate.querySelector(".precio").textContent = p.precio;
        $instrumentoTemplate.querySelector(".stock").textContent = p.stock;
        $instrumentoTemplate.querySelector(".modelo").textContent = p.instrumento.modelo;
        $instrumentoTemplate.querySelector(".tipo_instrumento").textContent = p.instrumento.detalle_instrumento?.tipo_instrumento?.tipo;
        $instrumentoTemplate.querySelector(".marca").textContent = p.instrumento.detalle_instrumento?.marca?.nombre;
        $instrumentoTemplate.querySelector(".descripcion").textContent = p.instrumento.detalle_instrumento?.descripcion;
    
        // Ajustar la configuración del dataset
        $instrumentoTemplate.querySelector(".edit").dataset.id = p.instrumento.id_instrumento;
        $instrumentoTemplate.querySelector(".edit").dataset.id_producto = p.id_producto;
        $instrumentoTemplate.querySelector(".edit").dataset.id_detalle_instrumento = p.instrumento.detalle_instrumento?.id_detalle_instrumento;
        $instrumentoTemplate.querySelector(".edit").dataset.modelo = p.instrumento.modelo;
        $instrumentoTemplate.querySelector(".edit").dataset.tipo_instrumento = p.instrumento.detalle_instrumento?.tipo_instrumento?.id_tipo_instrumento || '';
        $instrumentoTemplate.querySelector(".edit").dataset.marca = p.instrumento.detalle_instrumento?.marca?.id_marca || '';
        $instrumentoTemplate.querySelector(".edit").dataset.descripcion = p.instrumento.detalle_instrumento?.descripcion;
        $instrumentoTemplate.querySelector(".edit").dataset.precio = p.precio;
        $instrumentoTemplate.querySelector(".edit").dataset.stock = p.stock;
        $instrumentoTemplate.querySelector(".delete").dataset.id = p.instrumento.id_instrumento;
        $instrumentoTemplate.querySelector(".delete").dataset.id_producto = p.id_producto;
        $instrumentoTemplate.querySelector(".delete").dataset.id_detalle_instrumento = p.instrumento.detalle_instrumento?.id_detalle_instrumento;
        $instrumentoTemplate.querySelector(".delete").dataset.modelo = p.instrumento.modelo;
        
        let $clone = d.importNode($instrumentoTemplate, true);
        $instrumentoFragment.appendChild($clone);
      }
    });
    
    $instrumentosTable.appendChild($instrumentoFragment);
    
  } catch (error) {
    console.error(error);
  }
};

d.addEventListener("DOMContentLoaded", getAll);

d.addEventListener("submit", async e => {
  if(e.target === $instrumentoForm){
    e.preventDefault();

    if(!e.target.id.value){
      try {
        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
          data: JSON.stringify({
                tipo_instrumento_id: e.target.tipo_instrumento.value,
                marca_id: e.target.marca.value,
                descripcion: e.target.descripcion.value,
              })
            }
            let res = await axios(url + 'detalles_instrumentos/', options);
            let json = await res.data;

      } catch (error) {
        console.error(error);
      }

      try {
        let res = await axios(url + "detalles_instrumentos/");
        let json = await res.data;
        lastId = json[json.length-1].id_detalle_instrumento;

        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
          data: JSON.stringify({
                modelo: e.target.modelo.value,
                detalle_instrumento_id: lastId
              })
            }
        res = await axios(url + "instrumentos/", options);
        json = await res.data;
      } catch (error) {
        console.error(error);
      }
      try {
        let res = await axios(url + "instrumentos/");
        let json = await res.data;
        lastId = json[json.length-1].id_instrumento;

        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
          data: JSON.stringify({
                instrumento_id: lastId,
                disco_id: null,
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
              tipo_instrumento_id: e.target.tipo_instrumento.value,
              marca_id: e.target.marca.value,
              descripcion: e.target.descripcion.value,
            })
          }
      let res = await axios(url + `detalles_instrumentos/${e.target.id_detalle_instrumento.value}/` ,options);
      let json = await res.data;

    } catch (error) {
      console.error(error);
    }

    try {
      let res = await axios(url + "instrumentos/");
      let json = await res.data;

      let options = {
        method: "PUT",
        headers: {
          "content-type": "application/json;charset=utf-8"
        },
        data: JSON.stringify({
              modelo: e.target.modelo.value,
              detalle_instrumento_id: e.target.id_detalle_instrumento.value
            })
          }
      res = await axios(url + `instrumentos/${e.target.id.value}/`, options);
      json = await res.data;
    } catch (error) {
      console.error(error);
    }
    try {
      let res = await axios(url + "instrumentos/");
      let json = await res.data;
      lastId = json[json.length-1].id_instrumento;

      let options = {
        method: "PUT",
        headers: {
          "content-type": "application/json;charset=utf-8"
        },
        data: JSON.stringify({
              instrumento_id: e.target.id.value,
              disco_id: null,
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
    $title.textContent = "Editar Instrumento";
    $instrumentoForm.modelo.value = e.target.dataset.modelo;
    $instrumentoForm.tipo_instrumento.value = e.target.dataset.tipo_instrumento;
    $instrumentoForm.marca.value = e.target.dataset.marca;
    $instrumentoForm.descripcion.value = e.target.dataset.descripcion;
    $instrumentoForm.precio.value = e.target.dataset.precio;
    $instrumentoForm.stock.value = e.target.dataset.stock;
    $instrumentoForm.id_detalle_instrumento.value = e.target.dataset.id_detalle_instrumento;
    $instrumentoForm.id.value = e.target.dataset.id;
    $instrumentoForm.id_producto.value = e.target.dataset.id_producto;
  }

  if(e.target.matches(".delete")){
    let isDelete = confirm(`¿Estas seguro que deseas eliminar el instrumento: ${e.target.dataset.modelo} con id: ${e.target.dataset.id}?`);
    if(isDelete){
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
        }
        res = await axios(url + `productos/${e.target.dataset.id_producto}/`, options);
        json = await res.data;
      } catch (error) {
        console.error(error);
      }
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
        }
        res = await axios(url + `instrumentos/${e.target.dataset.id}/`);
        json = await res.data;
      } catch (error) {
        console.error(error);
      }
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8"
          },
        }
        res = await axios(url + `detalles_instrumentos/${e.target.dataset.id_detalle_instrumento}/`, options);
        json = await res.data;

        location.reload(true);

      } catch (error) {
        console.error(error);
      }
      
    }
  }

})

d.addEventListener("DOMContentLoaded", function () {
    // Referencia al elemento select
    const selectElement = document.getElementById("tipo-instrumento-select");
  
    // Función para poblar el select con opciones
    function populateSelect(data) {
      data.forEach((item) => {
        const option = document.createElement("option");
        option.value = item.id_tipo_instrumento; // Ajusta esto según la estructura de tu objeto de la API
        option.textContent = item.tipo; // Ajusta esto según la estructura de tu objeto de la API
        selectElement.appendChild(option);
      });
    }
  
    // Llamada a la API REST usando Axios
    axios
      .get(url + "tipos_instrumentos/")
      .then((response) => {
        populateSelect(response.data);
      })
      .catch((error) => {
        console.error("Error al obtener los datos de la API:", error);
      });
  });
  
  d.addEventListener("DOMContentLoaded", function () {
    // Referencia al elemento select
    const selectElement = document.getElementById("marca-select");
  
    // Función para poblar el select con opciones
    function populateSelect(data) {
      data.forEach((item) => {
        const option = document.createElement("option");
        option.value = item.id_marca; // Ajusta esto según la estructura de tu objeto de la API
        option.textContent = item.nombre; // Ajusta esto según la estructura de tu objeto de la API
        selectElement.appendChild(option);
      });
    }
  
    // Llamada a la API REST usando Axios
    axios
      .get(url + "marcas/")
      .then((response) => {
        populateSelect(response.data);
      })
      .catch((error) => {
        console.error("Error al obtener los datos de la API:", error);
      });
  });
  