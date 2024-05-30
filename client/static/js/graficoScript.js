const fetchCoastersData = (...urls) => {
  const promises = urls.map((url) =>
    fetch(url).then((response) => response.json())
  );
  return Promise.all(promises);
};

const getDataColors = (opacity) => {
  const colors = [
    "#7448c2",
    "#21c0d7",
    "#d99e2b",
    "#cd3a81",
    "#9c99cc",
    "#e14eca",
    "#ffffff",
    "#ff0000",
    "#d6ff00",
    "#0038ff",
  ];
  return colors.map((color) => (opacity ? `${color + opacity}` : color));
};

Chart.defaults.color = "#FFFFFF";

const printCharts = () => {
  fetchCoastersData("https://gmad.up.railway.app/api/productos/").then(
    ([allProducts]) => {
      renderModelsChart(allProducts);

      // console.log(allProducts)
    }
  );

  renderModelsChart();
};

const renderModelsChart = (products) => {
  // Mapea los productos a sus descripciones y agrupa por descripciones únicas
  const productMap = products.reduce((acc, product) => {
    let productName;
    if (product.instrumento) {
      productName =
        product.instrumento.detalle_instrumento.tipo_instrumento.tipo +
        " " +
        product.instrumento.modelo;
    } else if (product.disco) {
      productName = "Disco " + product.disco.titulo;
    }

    if (productName) {
      if (!acc[productName]) {
        acc[productName] = { stock: 0 };
      }
      acc[productName].stock += product.stock;
    }

    return acc;
  }, {});

  const uniqueProducts = Object.keys(productMap);
  const stocks = uniqueProducts.map((product) => productMap[product].stock);

  const data = {
    labels: uniqueProducts,
    datasets: [
      {
        data: stocks,
        borderColor: getDataColors(),
        backgroundColor: getDataColors(20),
      },
    ],
  };

  const options = {
    plugins: {
      legend: { position: "left" },
    },
  };

  new Chart("modelsChart", { type: "doughnut", data, options });
};

printCharts();

const enableEventHandlers = (coasters) => {
  document.querySelector("#featuresOptions").onchange = (e) => {
    const { value: property, text: label } = e.target.selectedOptions[0];

    const newData = coasters.map((coaster) => coaster[property]);

    updateChartData("featuresChart", newData, label);
  };
};

const getCoastersByYear = (coasters, years) => {
  const coastersByYear = years.map((yearsRange) => {
    const [from, to] = yearsRange.split("-");
    return coasters.filter(
      (eachCoaster) => eachCoaster.year >= from && eachCoaster.year <= to
    ).length;
  });
  return coastersByYear;
};

const updateChartData = (chartId, data, label) => {
  const chart = Chart.getChart(chartId);
  chart.data.datasets[0].data = data;
  chart.data.datasets[0].label = label;
  chart.update();
};
