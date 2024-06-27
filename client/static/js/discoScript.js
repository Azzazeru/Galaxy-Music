const url = "https://gmad.up.railway.app/api/hidden/"
const urls = "https://gmad.up.railway.app/api/public/"
// const url = "http://127.0.0.1:8000/api/hidden/"
// const urls = "http://127.0.0.1:8000/api/public/"

const d = document,
  $title = d.querySelector('.crud-title'),
  $discosTable = d.querySelector("#discos-table tbody"),
  $discoTemplate = d.getElementById("disco-template").content,
  $discoFragment = d.createDocumentFragment();
  $discoForm = d.querySelector(".crud-form");

  csrftoken = d.querySelector('[name=csrfmiddlewaretoken]').value;

  $filtroGenero = d.getElementById('filtroGenero'),
  $filtroArtista = d.getElementById('filtroArtista');
  $filtroTipo = d.getElementById('filtroTipo');
  $filtroFecha = d.getElementById('filtroFecha');
  $filtroSello = d.getElementById('filtroSello');
  $filtroAnioDesde = d.getElementById('filtroAnioDesde');
  $filtroAnioHasta = d.getElementById('filtroAnioHasta');

const getAllDiscos = async () => {
  try {
    let res = await axios.get(url + "productos/");
    discosData = await res.data;

    renderizarDiscos(discosData);
  } catch (error) {
    console.error(error);
  }
};

const renderizarDiscos = (discos) => {
  $discosTable.innerHTML = '';

  discos.forEach((p) => {
    if (p.disco) {
      $discoTemplate.querySelector(".precio").textContent = p.precio;
      $discoTemplate.querySelector(".stock").textContent = p.stock;
      $discoTemplate.querySelector(".titulo").textContent = p.disco.titulo;
      $discoTemplate.querySelector(".sello").textContent = p.disco.sello_discografico;
      $discoTemplate.querySelector(".genero").textContent = p.disco.genero_musical;
      $discoTemplate.querySelector(".artista").textContent = p.disco.artista;
      $discoTemplate.querySelector(".tipodisco").textContent = p.disco.tipo_disco;
      $discoTemplate.querySelector(".fecha").textContent = p.disco.fecha_lanzamiento;

      $discoTemplate.querySelector(".edit").dataset.id = p.disco.id_disco;
      $discoTemplate.querySelector(".edit").dataset.id_producto = p.id_producto;
      $discoTemplate.querySelector(".edit").dataset.titulo = p.disco.titulo;
      $discoTemplate.querySelector(".edit").dataset.sello = p.disco.sello_discografico;
      $discoTemplate.querySelector(".edit").dataset.genero = p.disco.genero_musical;
      $discoTemplate.querySelector(".edit").dataset.artista = p.disco.artista;
      $discoTemplate.querySelector(".edit").dataset.tipodisco = p.disco.tipo_disco;
      $discoTemplate.querySelector(".edit").dataset.fecha = p.disco.fecha_lanzamiento;
      $discoTemplate.querySelector(".edit").dataset.precio = p.precio;
      $discoTemplate.querySelector(".edit").dataset.stock = p.stock;

      $discoTemplate.querySelector(".delete").dataset.titulo = p.disco.titulo;
      $discoTemplate.querySelector(".delete").dataset.id = p.disco.id_disco;
      $discoTemplate.querySelector(".delete").dataset.id_producto = p.id_producto;

      let $clone = d.importNode($discoTemplate, true);
      $discoFragment.appendChild($clone);
    }
  });

  $discosTable.appendChild($discoFragment);
};

const aplicarFiltros = () => {
  const generoSeleccionado = $filtroGenero.value.toLowerCase();
  const artistaSeleccionado = $filtroArtista.value.toLowerCase();
  const tipoSeleccionado = $filtroTipo.value.toLowerCase();
  const selloSeleccionado = $filtroSello.value.toLowerCase();

  // Filtrar los discos basado en los criterios seleccionados
  let discosFiltrados = discosData.filter(p => {
      if (p.disco
          && p.disco.genero_musical
          && p.disco.artista
          && p.disco.tipo_disco
          && p.disco.sello_discografico
          && p.disco.fecha_lanzamiento
      ) {
          const cumpleGenero = generoSeleccionado === '' || p.disco.genero_musical.toLowerCase() === generoSeleccionado;
          const cumpleArtista = artistaSeleccionado === '' || p.disco.artista.toLowerCase().includes(artistaSeleccionado);
          const cumpleTipo = tipoSeleccionado === '' || p.disco.tipo_disco.toLowerCase() === tipoSeleccionado;
          const cumpleSello = selloSeleccionado === '' || p.disco.sello_discografico.toLowerCase().includes(selloSeleccionado);

          return cumpleGenero && cumpleArtista && cumpleTipo && cumpleSello;
      } else {
          return false;
      }
  });

  // Ordenar los discos por fecha de lanzamiento de manera descendente (los más recientes primero)
  discosFiltrados.sort((a, b) => new Date(b.disco.fecha_lanzamiento) - new Date(a.disco.fecha_lanzamiento));

  // Llamar a la función para renderizar los discos filtrados y ordenados
  renderizarDiscos(discosFiltrados);
};

// Agregar event listeners para los filtros existentes
$filtroGenero.addEventListener('change', aplicarFiltros);
$filtroArtista.addEventListener('change', aplicarFiltros);
$filtroTipo.addEventListener('change', aplicarFiltros);
$filtroSello.addEventListener('change', aplicarFiltros);

d.addEventListener("DOMContentLoaded", getAllDiscos);

d.addEventListener("submit", async e => {
  if (e.target === $discoForm) {
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
            titulo: e.target.titulo.value,
            sello_discografico: e.target.sello.value,
            genero_musical: e.target.genero.value,
            artista: e.target.artista.value,
            tipo_disco: e.target.tipodisco.value,
            fecha_lanzamiento: e.target.fecha.value
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
        lastId = json[json.length - 1].id_disco;

        let options = {
          method: "POST",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
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
    } else {
      try {
        let res = await axios(url + "discos/");
        let json = await res.data;

        let options = {
          method: "PUT",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
          },
          data: JSON.stringify({
            titulo: e.target.titulo.value,
            sello_discografico: e.target.sello.value,
            genero_musical: e.target.genero.value,
            artista: e.target.artista.value,
            tipo_disco: e.target.tipodisco.value,
            fecha_lanzamiento: e.target.fecha.value
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
        lastId = json[json.length - 1].id_disco;

        let options = {
          method: "PUT",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
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
  } else {
  }
});

d.addEventListener("click", async e => {
  if (e.target.matches(".edit")) {
    $title.textContent = "Editar Disco";
    $discoForm.titulo.value = e.target.dataset.titulo;
    $discoForm.sello.value = e.target.dataset.sello;
    $discoForm.genero.value = e.target.dataset.genero;
    $discoForm.artista.value = e.target.dataset.artista;
    $discoForm.precio.value = e.target.dataset.precio;
    $discoForm.stock.value = e.target.dataset.stock;
    $discoForm.tipodisco.value = e.target.dataset.tipodisco;
    $discoForm.fecha.value = e.target.dataset.fecha;

    $discoForm.id.value = e.target.dataset.id;
    $discoForm.id_producto.value = e.target.dataset.id_producto;
  }

  if (e.target.matches(".delete")) {
    let isDelete = confirm(`¿Estas seguro que deseas eliminar el disco: ${e.target.dataset.titulo}?`);
    if (isDelete) {
      try {
        let options = {
          method: "DELETE",
          headers: {
            "content-type": "application/json;charset=utf-8",
            "X-CSRFToken": csrftoken
          },
        }
        res = await axios(url + `discos/${e.target.dataset.id}/`, options);
        json = await res.data;

        location.reload(true)
      } catch (error) {

      }
    }
  }
})

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("sello-select");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "sellos/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("genero-select");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "generos/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("artista-select");
  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "artistas/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("tipodisco-select");
  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "tipodiscos/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

// Filtros

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("filtroGenero");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "generos/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
});

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("filtroArtista");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "artistas/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
})

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("filtroTipo");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "tipodiscos/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
})

d.addEventListener("DOMContentLoaded", function () {
  const selectElement = document.getElementById("filtroSello");

  function populateSelect(data) {
    data.forEach((item) => {
      const option = document.createElement("option");
      option.value = item.nombre;
      option.textContent = item.nombre;
      selectElement.appendChild(option);
    });
  }

  axios
    .get(urls + "sellos/")
    .then((response) => {
      populateSelect(response.data);
    })
    .catch((error) => {
      console.error("Error al obtener los datos de la API:", error);
    });
})