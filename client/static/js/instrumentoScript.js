const url = "https://gmad.up.railway.app/api/hidden/"
const urls = "https://gmad.up.railway.app/api/public/"
// const url = "http://127.0.0.1:8000/api/hidden/"
// const urls = "http://127.0.0.1:8000/api/public/"

const d = document,
  $title = d.querySelector('.crud-title'),
  $instrumentosTable = d.querySelector("#instrumentos-table tbody"),
  $instrumentoTemplate = d.getElementById("instrumento-template").content,
  $instrumentoFragment = d.createDocumentFragment(),
  $instrumentoForm = d.querySelector(".crud-form");

  csrftoken = d.querySelector('[name=csrfmiddlewaretoken]').value;

  $filtroTipo = d.getElementById("filtroTipo"),
  $filtroEspecie = d.getElementById("filtroEspecie")


const getAllInstrumentos = async () => {
  try {
    let res = await axios.get(url + "productos/");
    instrumentosData = await res.data;

    renderizarInstrumentos(instrumentosData);
  } catch (error) {
    console.error(error)
  }
}

const renderizarInstrumentos = (instrumentos) => {
  $instrumentosTable.innerHTML = '';

  instrumentos.forEach((p) => {
    if (p.instrumento) {
      $instrumentoTemplate.querySelector(".precio").textContent = p.precio;
      $instrumentoTemplate.querySelector(".stock").textContent = p.stock;
      $instrumentoTemplate.querySelector(".modelo").textContent = p.instrumento.modelo;
      $instrumentoTemplate.querySelector(".tipo_instrumento").textContent = p.instrumento.tipo_instrumento;
      $instrumentoTemplate.querySelector(".especie").textContent = p.instrumento.especie;
      $instrumentoTemplate.querySelector(".marca").textContent = p.instrumento.marca;
      $instrumentoTemplate.querySelector(".descripcion").textContent = p.instrumento.descripcion;

      $instrumentoTemplate.querySelector(".edit").dataset.id = p.instrumento.id_instrumento;
      $instrumentoTemplate.querySelector(".edit").dataset.id_producto = p.id_producto;
      $instrumentoTemplate.querySelector(".edit").dataset.modelo = p.instrumento.modelo;
      $instrumentoTemplate.querySelector(".edit").dataset.tipo_instrumento = p.instrumento.tipo_instrumento;
      $instrumentoTemplate.querySelector(".edit").dataset.especie = p.instrumento.especie;
      $instrumentoTemplate.querySelector(".edit").dataset.marca = p.instrumento.marca;
      $instrumentoTemplate.querySelector(".edit").dataset.descripcion = p.instrumento.descripcion;
      $instrumentoTemplate.querySelector(".edit").dataset.precio = p.precio;
      $instrumentoTemplate.querySelector(".edit").dataset.stock = p.stock;

      $instrumentoTemplate.querySelector(".delete").dataset.modelo = p.instrumento.modelo;
      $instrumentoTemplate.querySelector(".delete").dataset.id = p.instrumento.id_instrumento;
      $instrumentoTemplate.querySelector(".delete").dataset.id_producto = p.id_producto;

      let $clone = d.importNode($instrumentoTemplate, true);
      $instrumentoFragment.appendChild($clone);
    }
  });

  $instrumentosTable.appendChild($instrumentoFragment);
}

const aplicarFiltros = () => {
  const tipoSeleccionado = $filtroTipo.value.toLowerCase();
  const especieSeleccionada = $filtroEspecie.value.toLowerCase();

  const instrumentosFiltrados = instrumentosData.filter(p => {
    if(p.instrumento) {
      const cumpleTipo = tipoSeleccionado === '' || p.instrumento.tipo_instrumento.toLowerCase() === tipoSeleccionado;
      const cumpleEspecie = especieSeleccionada === '' || p.instrumento.especie.toLowerCase() === especieSeleccionada;
      return cumpleTipo && cumpleEspecie;
    }
    return false;
  });

  renderizarInstrumentos(instrumentosFiltrados);
};

$filtroTipo.addEventListener("change", aplicarFiltros);
$filtroEspecie.addEventListener("change", aplicarFiltros);

d.addEventListener("DOMContentLoaded", getAllInstrumentos);

d.addEventListener("submit", async e => {
  if (e.target === $instrumentoForm) {
    e.preventDefault();

    if (!e.target.id.value) {
      try {
        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
          },
          data: JSON.stringify({
            modelo: e.target.modelo.value,
            tipo_instrumento: e.target.tipo_instrumento.value,
            especie: e.target.especie.value,
            marca: e.target.marca.value,
            descripcion: e.target.descripcion.value,
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
        lastId = json[json.length - 1].id_instrumento;

        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
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
    } else {
      try {
        let options = {
          method: "PUT",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
          },
          data: JSON.stringify({
            modelo: e.target.modelo.value,
            tipo_instrumento: e.target.tipo_instrumento.value,
            especie: e.target.especie.value,
            marca: e.target.marca.value,
            descripcion: e.target.descripcion.value,
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
        lastId = json[json.length - 1].id_instrumento;

        let options = {
          method: "PUT",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
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
  } else {
  }
});

d.addEventListener("click", async e => {
  if (e.target.matches(".edit")) {
    $title.textContent = "Editar Instrumento";
    $instrumentoForm.modelo.value = e.target.dataset.modelo || '';
    $instrumentoForm.tipo_instrumento.value = e.target.dataset.tipo_instrumento;
    $instrumentoForm.especie.value = e.target.dataset.especie;
    $instrumentoForm.marca.value = e.target.dataset.marca;
    $instrumentoForm.descripcion.value = e.target.dataset.descripcion || '';
    $instrumentoForm.precio.value = e.target.dataset.precio || '';
    $instrumentoForm.stock.value = e.target.dataset.stock || '';

    $instrumentoForm.id.value = e.target.dataset.id || '';
    $instrumentoForm.id_producto.value = e.target.dataset.id_producto || '';
  }

  if (e.target.matches(".delete")) {
    let isDelete = confirm(`¿Estas seguro que deseas eliminar el instrumento: ${e.target.dataset.modelo}?`);
    if (isDelete) {
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
          },
        }
        res = await axios(url + `instrumentos/${e.target.dataset.id}/`, options);
        json = await res.data;
        location.reload(true);
      } catch (error) {
        console.error(error);
      }
    }
  }
})

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("tipo-instrumento-select");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.tipo;
      option.textContent = item.tipo;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "tipoinstrumento/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("especie-select");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.especie;
      option.textContent = item.especie;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "especieinstrumento/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("marca-select");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.marca;
      option.textContent = item.marca;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "marcainstrumento/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

// Filtros

d.addEventListener("DOMContentLoaded", function () {
  const selectElementEspecie = document.getElementById("filtroEspecie");
  const selectElementTipo = document.getElementById("filtroTipo");

  function populateSelect(selectElement, data, key, value) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item[key];
      option.textContent = item[value];
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "especieinstrumento/")
    .then((response) => {
      populateSelect(selectElementEspecie, response.data, 'especie', 'especie');
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });

  axios
    .get(urls + "tipoinstrumento/")
    .then((response) => {
      populateSelect(selectElementTipo, response.data, 'tipo', 'tipo');
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});