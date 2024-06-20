function selecionar() {
    let produto = document.getElementById('produto').value;
    // alert(produto);
    console.log(produto);

    document.getElementById('opcao-selecionada').textContent = produto;
}

// converter temperatura
function converter() {
    let unidadeInicial = document.getElementById('tipo-unidade').value;
    let temperaturaInicial = document.getElementById('temperatura').value;

    if (unidadeInicial == 'celsius') {
        temperaturaConvertida = parseInt(temperaturaInicial * (9/5) + 32);
        unidadeFinal = 'fahrenheit';
    } else {
        temperaturaConvertida = parseInt((temperaturaInicial - 32) * (5/9));
        unidadeFinal = 'celsius';
    }
    
    let textoOutput = `${temperaturaInicial} graus ${unidadeInicial} equivalem a ${temperaturaConvertida} graus ${unidadeFinal}`
    document.getElementById('output').innerHTML = textoOutput;
}

// (0 °C × 9/5) + 32 = 32 °F