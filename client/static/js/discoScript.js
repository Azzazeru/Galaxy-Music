const url = "https://gmad.up.railway.app/api/";

const d = document,
  $discosTable = d.querySelector("#discos-table tbody"),
  $discoTemplate = d.getElementById("disco-template").content,
  $discoFragment = d.createDocumentFragment();

const getAll = async () => {
  try {
    let res = await axios.get(url + "productos/"),
      json = await res.data;

    console.log(json);

    json.forEach((p) => {
      if (p.disco) {
        $discoTemplate.querySelector(".id").textContent = p.disco.id_disco;
        $discoTemplate.querySelector(".precio").textContent = p.precio;
        $discoTemplate.querySelector(".stock").textContent = p.stock;
        $discoTemplate.querySelector(".titulo").textContent = p.disco.titulo;
        $discoTemplate.querySelector(".sello").textContent =
          p.disco.detalle_disco?.sello_discografico?.nombre;
        $discoTemplate.querySelector(".genero").textContent =
          p.disco.detalle_disco?.genero_musical?.nombre;
        $discoTemplate.querySelector(".artista").textContent =
          p.disco.detalle_disco?.artista?.nombre;

        $discoTemplate.querySelector(".edit").dataset.id = p.disco.id_disco;
        $discoTemplate.querySelector(".edit").dataset.titulo = p.disco.titulo;
        $discoTemplate.querySelector(".edit").dataset.sello =
          p.disco.detalle_disco?.sello_discografico?.nombre;
        $discoTemplate.querySelector(".edit").dataset.genero =
          p.disco.detalle_disco?.genero_musical?.nombre;
        $discoTemplate.querySelector(".edit").dataset.artista =
          p.disco.detalle_disco?.artista?.nombre;
        $discoTemplate.querySelector(".edit").dataset.precio = p.precio;
        $discoTemplate.querySelector(".edit").dataset.stock = p.stock;

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

// Evento para enviar el formulario
d.addEventListener("submit", async (e) => {
  if (e.target === $form) {
    e.preventDefault();

    if (e.target.id.value) {
      try {
        let options = {
          method: "POST",
          headers: {
            "Content-Type": "application/json;charset=utf-8",
          },
          data: JSON.stringify({
            titulo: e.target.titulo.value,
            disco: {
              id_disco: e.target.id_disco.value, // Aquí deberías tener algún mecanismo para obtener el ID del disco
              detalle_disco: {
                id_artista: e.target.id_artista.value, // Aquí accedes al ID del artista
                sello_discografico: {
                  id_sello_discografico: e.target.sello.value,
                },
                genero_musical: {
                  id_genero_musical: e.target.genero.value,
                },
              },
            },
            precio: e.target.precio.value,
            stock: e.target.stock.value,
          }),
        };

        res = await axios(url + "productos/", options);
        json = await res.data();

        console.log(json);

        // location.reload();
      } catch (err) {
        let message = err.statusText || "Ocurrio un error";
        $form.insertAdjacentHTML(
          "afterend",
          `<p><b>Error ${err.status}: ${message}</b></p>`
        );
      }
    } else {
    }
  }
});
