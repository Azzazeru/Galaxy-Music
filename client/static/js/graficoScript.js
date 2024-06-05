const url = "https://gmad.up.railway.app/api/productos"
// const url = "http://127.0.0.1:8000/api/productos/"

Chart.defaults.color = "#FFFFFF";
Chart.defaults.borderColor = "#444";

const fetchProductsData = (...urls) => {
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

const printCharts = () => {
  fetchProductsData(url).then(
    ([allProducts]) => {
      renderModelsChart(allProducts);
      renderFeaturesChart(allProducts);    
      enableEventHandlers(allProducts);
    }

  );

  renderModelsChart();
};

const updateChartData = (chartId, data, label) => {
  const chart = Chart.getChart(chartId);
  chart.data.datasets[0].data = data;
  chart.data.datasets[0].label = label;
  chart.update();
};

const enableEventHandlers = products => {
  document.querySelector('#featuresOptions').onchange = e => {
    const { value: property, text: label } = e.target.selectedOptions[0];
    console.log(property, label);

    let newData;
    if (label === 'Mas caro') {
      newData = products.map(product => product[property]);
    } else if (label === 'Mas barato') {
      newData = products.map(product => -product[property]);
    }

    updateChartData('featuresChart', newData, label);
  };
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

const renderFeaturesChart = products => {

  const data = {
    labels: products.map(product => {
      const tituloDisco = product.disco ? product.disco.titulo : '';
      const modeloInstrumento = product.instrumento ? product.instrumento.modelo : '';
      return tituloDisco && modeloInstrumento ? `${tituloDisco} - ${modeloInstrumento}` : (tituloDisco || modeloInstrumento);
    }),
    datasets: [{
      label: "Precio",
      data: products.map(product => product.precio),
      borderColor: getDataColors()[0],
      backgroundColor: getDataColors(20)[0],
      
    }]
  }
  const options = {
    plugins: {
      legend: { display: false}
    },
    scales: {
      r: {
        ticks: { display: false}
      }
    }
  }

  new Chart('featuresChart', { type: 'radar', data, options})
}

printCharts();
