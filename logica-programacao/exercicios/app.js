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

// concatenar listas
let lista1 = [1, 2, 3];
let lista2 = [4, 5, 6];
let novaLista = lista1.concat(lista2);
novaLista.pop();
// console.log(novaLista);

// algoritmo fisher yates
const vogais = ['a', 'e', 'i', 'o', 'u'];

function embaralha(lista) {

    for (let indice = lista.length; indice; indice--) {
        const indiceAleatorio = Math.floor(Math.random() * indice);
        const elemento = lista[indice - 1];
        lista[indice - 1] = lista[indiceAleatorio];
        lista[indiceAleatorio] = elemento;
    }
}

// console.log(embaralha(vogais));
embaralha(novaLista);
console.log(novaLista);


// remover duplicatas
function removerDuplicatas(lista) {
    listaSemDuplicatas = [];
    lista.forEach((elemento) => {
        if(!listaSemDuplicatas.includes(elemento)) {
            listaSemDuplicatas.push(elemento);
        }
    })

    return listaSemDuplicatas;
}

let listaTeste = ["RJ", "MG", "SP", "SC", "SP", "SP", "PR", "PE", "PA", "RJ", "MG"];

console.log(listaTeste);
console.log(removerDuplicatas(listaTeste));