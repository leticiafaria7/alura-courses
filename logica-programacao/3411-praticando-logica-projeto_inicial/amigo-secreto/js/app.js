let listaAmigos = [];
let listaDuplas = [];
let numerosSorteados = [];

function adicionar() {
    let amigo = document.getElementById('nome-amigo').value;

    if (listaAmigos.includes(amigo)) {
        alert(`${amigo} já está na lista!`);
        document.getElementById('nome-amigo').value = '';
    } else if (amigo == '') {
        alert(`Inclua o nome de um amigo`);
    } else {
        listaAmigos.push(amigo);
        document.getElementById('lista-amigos').innerHTML = listaAmigos;
        document.getElementById('nome-amigo').value = '';
    }
}

function sortear() {
    if (listaAmigos.length < 3) {
        alert('A lista de amigos deve ter pelo menos 3 amigos!');
    } else {
        listaAmigos.forEach((amigo, indexAmigo) => {
            let numeroSorteado;
    
            do {
                numeroSorteado = Math.floor(Math.random() * listaAmigos.length);
            } while (numeroSorteado == indexAmigo || numerosSorteados.includes(numeroSorteado));
    
            numerosSorteados.push(numeroSorteado);
    
            let amigoSecreto = listaAmigos[numeroSorteado];
            let dupla = `${amigo} → ${amigoSecreto}<br>`;
            listaDuplas.push(dupla);
            console.log(listaDuplas);
        })
    
        document.getElementById('lista-sorteio').innerHTML = listaDuplas.join('');
    }
}

function reiniciar() {
    document.getElementById('lista-amigos').innerHTML = [];
    document.getElementById('nome-amigo').innerHTML = '';
    document.getElementById('lista-sorteio').innerHTML = '';
    listaAmigos = [];
    listaDuplas = [];
    numerosSorteados = [];
}