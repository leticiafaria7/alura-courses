document.getElementById('qtd-pista').textContent = 100;
document.getElementById('qtd-superior').textContent = 200;
document.getElementById('qtd-inferior').textContent = 400;

function comprar() {
    let tipo = document.getElementById('tipo-ingresso');
    let quantidade = parseInt(document.getElementById('qtd').value);
    console.log(quantidade);

    if (quantidade <= 0) {
        alert("A quantidade de ingressos deve ser maior que 0!");
    } else {
        if (document.getElementById(`qtd-${tipo.value}`).textContent - quantidade >= 0) {
            document.getElementById(`qtd-${tipo.value}`).textContent = document.getElementById(`qtd-${tipo.value}`).textContent - quantidade;
        } else {
            let palavraIngresso = quantidade == 1 ? 'ingresso disponível' : 'ingressos disponíveis';
            let tipoIngresso = tipo.options[tipo.selectedIndex].textContent;
            alert(`Há menos de ${quantidade} ${palavraIngresso} para ${tipoIngresso}!`);
        }
    }   
}


// verificar se o número é par ou impar
// let numero = prompt("Escolha um número:")

// function parOuImpar(numero) {
//     if (numero % 2 == 0) {
//         alert(`O número ${numero} é par.`);
//     } else {
//         alert(`O número ${numero} é ímpar.`);
//     }
// }

// parOuImpar(numero);