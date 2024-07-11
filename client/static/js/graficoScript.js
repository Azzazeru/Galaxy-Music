const url = "https://gmad.up.railway.app/api/public/productos/"
const urlboleta = "https://gmad.up.railway.app/api/fake/boleta/"
const urldetalleboleta = "https://gmad.up.railway.app/api/fake/detalleboleta/"
// const url = "http://127.0.0.1:8000/api/public/productos/"
// const urlboleta = "http://127.0.0.1:8000/api/public/boleta/"
// const urldetalleboleta = "http://127.0.0.1:8000/api/public/detalleboleta/"

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
    "#7448c2","#21c0d7","#d99e2b","#cd3a81","#9c99cc","#e14eca","#ffffff","#ff0000","#d6ff00","#0038ff","#f57c00","#8e24aa","#616161","#ff6e40","#1de9b6","#fdd835","#8d6e63",
    "#f06292","#90a4ae","#689f38","#7b1fa2","#ef6c00", "#9e9e9e","#3f51b5","#c2185b","#009688","#ffeb3b","#757575","#673ab7","#ff5722","#607d8b","#4caf50",
    "#ff9800","#795548","#2196f3","#f44336","#00bcd4","#ffc107","#9c27b0","#8bc34a","#e91e63","#cddc39","#03a9f4","#ff4081","#4db6ac","#ffeb3b","#ff5252","#8bc34a",
  ];
  
  return colors.map((color) => (opacity ? `${color}${opacity}` : color));
};

const printCharts = () => {
  fetchProductsData(url, urlboleta, urldetalleboleta).then(
    ([allProducts, boletas, detalles]) => {
      renderModelsChart(allProducts);
      renderDiskChart(allProducts);
      renderInstrumentChart(allProducts);
      renderFeaturesChart(allProducts);
      renderMonthlySalesChart(boletas);
      renderAnnualSalesChart(boletas);
      renderSalesChart(allProducts, boletas, detalles);
      renderGenresChart(allProducts);
      enableEventHandlers(allProducts);
    }

  );

  renderModelsChart();
};

const enableEventHandlers = products => {
  document.querySelector('#featuresOptions').onchange = e => {
    const { value: property, text: label } = e.target.selectedOptions[0];

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
  if (!Array.isArray(products) || products.length === 0) {
    return;
    // No se por que da error, pero da error en la consola, PERO NO AFECTA NEGATIVAMENTE AL CODIGO XD, y esto es para evitar ese error.
  }
  const productMap = products.reduce((acc, product) => {
    let productName;
    if (product.instrumento) {
      productName =
        product.instrumento.especie +
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

const renderDiskChart = (products) => {
  const productMap = products.reduce((acc, product) => {
    let productName;
    if (product.disco) {
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

  new Chart("diskChart", { type: "doughnut", data, options });
};

const renderInstrumentChart = (products) => {
  const productMap = products.reduce((acc, product) => {
    let productName;
    if (product.instrumento) {
      productName =
        product.instrumento.especie +
        " " +
        product.instrumento.modelo;
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

  new Chart("instrumentChart", { type: "doughnut", data, options });
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

const updateChartData = (chartId, data, label) => {
  const chart = Chart.getChart(chartId);
  chart.data.datasets[0].data = data;
  chart.data.datasets[0].label = label;
  chart.update();
};

const renderMonthlySalesChart = boletas => {
  const monthlySales = Array(12).fill(0);
  const monthlyRevenue = Array(12).fill(0);

  boletas.forEach(boleta => {
    const month = new Date(boleta.fecha_venta).getMonth();
    monthlySales[month]++;
    monthlyRevenue[month] += boleta.total;
  });

  const labels = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
  ];

  const data = {
    labels,
    datasets: [
      {
        label: "Ventas",
        data: monthlySales,
        borderColor: getDataColors()[0],
        backgroundColor: getDataColors(20)[0],
        yAxisID: 'y1',
      },
      {
        label: "Ganancias",
        data: monthlyRevenue,
        borderColor: getDataColors()[1],
        backgroundColor: getDataColors(20)[1],
        yAxisID: 'y2',
      }
    ]
  };

  const options = {
    plugins: {
      legend: { position: "top" },
    },
    scales: {
      y1: {
        type: 'linear',
        position: 'left',
        title: {
          display: true,
          text: 'Número de Ventas',
        },
      },
      y2: {
        type: 'linear',
        position: 'right',
        title: {
          display: true,
          text: 'Ganancias Totales ($)',
        },
        grid: {
          drawOnChartArea: false,
        },
      }
    }
  };

  new Chart('salesChart', { type: 'line', data, options });
}

const renderAnnualSalesChart = boletas => {
  const annualSales = {};
  const annualRevenue = {};

  boletas.forEach(boleta => {
    const year = new Date(boleta.fecha_venta).getFullYear();
    if (!annualSales[year]) {
      annualSales[year] = 0;
      annualRevenue[year] = 0;
    }
    annualSales[year]++;
    annualRevenue[year] += boleta.total;
  });

  const labels = Object.keys(annualSales);
  const salesData = Object.values(annualSales);
  const revenueData = Object.values(annualRevenue);

  const data = {
    labels,
    datasets: [
      {
        label: "Ventas",
        data: salesData,
        backgroundColor: getDataColors(20)[0],
        borderColor: getDataColors()[0],
        borderWidth: 1,
        yAxisID: 'y1'
      },
      {
        label: "Ganancias",
        data: revenueData,
        backgroundColor: getDataColors(20)[1],
        borderColor: getDataColors()[1],
        borderWidth: 1,
        yAxisID: 'y2'
      }
    ]
  };

  const options = {
    plugins: {
      legend: { position: "top" }
    },
    scales: {
      y1: {
        beginAtZero: true,
        type: 'linear',
        position: 'left',
        title: {
          display: true,
          text: 'Número de Ventas'
        },
        grid: {
          drawOnChartArea: false
        }
      },
      y2: {
        beginAtZero: true,
        type: 'linear',
        position: 'right',
        title: {
          display: true,
          text: 'Ganancias Totales ($)'
        },
        grid: {
          drawOnChartArea: false
        }
      }
    }
  };

  new Chart('annualSalesChart', { type: 'bar', data, options });
}

const getSalesData = (allProducts, boletas, detalles) => {
  const salesCount = {};

  detalles.forEach(detalle => {
    const productId = detalle.producto.toString();
    if (salesCount[productId]) {
      salesCount[productId] += detalle.cantidad;
    } else {
      salesCount[productId] = detalle.cantidad;
    }
  });

  const sortedProducts = Object.keys(salesCount).sort((a, b) => salesCount[b] - salesCount[a]);

  const mostSoldProducts = sortedProducts.slice(0, 5);

  const leastSoldProducts = sortedProducts.slice(-5);

  const mostSoldProductsData = mostSoldProducts.map(productId => {
    const productInfo = allProducts.find(product => product.id_producto.toString() === productId);
    const productName = productInfo.disco ? productInfo.disco.titulo : productInfo.instrumento.modelo;
    return {
      id: productId,
      name: productName,
      quantity: salesCount[productId]
    };
  });

  const leastSoldProductsData = leastSoldProducts.map(productId => {
    const productInfo = allProducts.find(product => product.id_producto.toString() === productId);
    const productName = productInfo.disco ? productInfo.disco.titulo : productInfo.instrumento.modelo;
    return {
      id: productId,
      name: productName,
      quantity: salesCount[productId]
    };
  });

  return {
    mostSoldProductsData,
    leastSoldProductsData
  };
};

const getProductDisplayName = (product, allProducts) => {
  const productInfo = allProducts.find(p => p.id_producto.toString() === product.id);
  if (productInfo) {
    if (productInfo.disco) {
      return `Disco ${productInfo.disco.titulo}`;
    } else if (productInfo.instrumento) {
      return `${productInfo.instrumento.especie} ${productInfo.instrumento.modelo}`;
    }
  }
  return `Producto ${product.id}`;
};

const renderSalesChart = (allProducts, boletas, detalles) => {
  const { mostSoldProductsData, leastSoldProductsData } = getSalesData(allProducts, boletas, detalles);

  const mostSoldProductsNames = mostSoldProductsData.map(product => getProductDisplayName(product, allProducts));
  const mostSoldProductsQuantities = mostSoldProductsData.map(product => product.quantity);

  const leastSoldProductsNames = leastSoldProductsData.map(product => getProductDisplayName(product, allProducts));
  const leastSoldProductsQuantities = leastSoldProductsData.map(product => product.quantity);

  const data = {
    labels: [...mostSoldProductsNames, ...leastSoldProductsNames],
    datasets: [
      {
        label: 'Más Vendidos',
        data: [...mostSoldProductsQuantities, ...Array(5).fill(0)],
        backgroundColor: 'rgba(54, 162, 235, 0.2)',
        borderColor: 'rgba(54, 162, 235, 1)',
        borderWidth: 1
      },
      {
        label: 'Menos Vendidos',
        data: [...Array(5).fill(0), ...leastSoldProductsQuantities],
        backgroundColor: 'rgba(255, 99, 132, 0.2)',
        borderColor: 'rgba(255, 99, 132, 1)',
        borderWidth: 1
      }
    ]
  };

  const options = {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  };

  const ctx = document.getElementById('morelessSalesChart').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: data,
    options: options
  });
};

const getGenresData = (allProducts) => {
  const genreCount = {};

  allProducts.forEach(product => {
    if (product.disco) {
      const genre = product.disco.genero_musical;
      if (genreCount[genre]) {
        genreCount[genre] += 1;
      } else {
        genreCount[genre] = 1;
      }
    }
  });

  const genres = Object.keys(genreCount);
  const data = Object.values(genreCount);

  return {
    genres,
    data
  };
};

const renderGenresChart = (allProducts) => {
  const { genres, data } = getGenresData(allProducts);
  const colors = getDataColors();

  const config = {
    type: 'doughnut',
    data: {
      labels: genres,
      datasets: [{
        label: 'Géneros de Discos',
        data: data,
        borderColor: getDataColors(),
        backgroundColor: getDataColors(20),
      }]
    },
    options: {
      responsive: true,
      plugins: {
        legend: {
          position: 'top',
        },
        title: {
          display: true,
          text: 'Géneros de Discos'
        }
      }
    }
  };

  const ctx = document.getElementById('genreDiskChart').getContext('2d');
  new Chart(ctx, config);
};

printCharts();
