// função olá mundo ------------------------------------------------------------------------

// function olaMundo() {
//     console.log("Olá mundo!")
// }

// olaMundo()


// função olá fulano ------------------------------------------------------------------------

// let nome = prompt("Qual o seu nome?")

// function olaFulano(nome) {
//     alert(`Olá, ${nome}!`)
// }

// olaFulano(nome = nome)

// função dobro -----------------------------------------------------------------------------

// let numero = prompt("Fale um número:")


// function dobro(numero) {
//     let dobro = parseInt(numero) * 2
//     alert(`O dobro de ${numero} é ${dobro}.`)
// }

// dobro(numero = numero)

// função média ------------------------------------------------------------------------------

// let numero1 = prompt("Fale um número:")
// let numero2 = prompt("Fale outro número:")
// let numero3 = prompt("Fale mais um número:")

// function media(numero1, numero2, numero3) {
//     let media = (parseInt(numero1) + parseInt(numero2) + parseInt(numero3)) / 3
//     alert(`A média dos 3 números informados é ${media}.`)
// }

// media(numero1, numero2, numero3)

// função maior ------------------------------------------------------------------------------

// let numero1 = prompt("Fale um número:")
// let numero2 = prompt("Fale outro número:")

// function maior(numero1, numero2) {
//     if (numero1 > numero2) {
//         alert(`O maior número é ${numero1}.`)
//     } else if (numero1 == numero2) {
//         alert(`Os dois números informados são iguais.`)
//     } else {
//         alert(`O maior número é ${numero2}`)
//     }
// }

// maior(numero1, numero2)

// IMC ----------------------------------------------------------------------------------------

// let altura = prompt('Qual a sua altura (em cm)?');
// let peso = prompt('Qual é o seu peso (em kg)?');

// function textoAvaliacao(imc) {
//     if (imc < 18) {
//         avaliacao = "abaixo do ideal";
//     } else if (imc <= 25) {
//         avaliacao = "dentro do ideal";
//     } else if (imc <= 30) {
//         avaliacao = "alto";
//     } else {
//         avaliacao = "você está com obesidade";
//     }

//     return avaliacao
// }

// function imc(altura, peso) {
//     let imc = peso / ((altura / 100) ** 2);
//     alert(`Seu IMC é ${parseInt(imc)} (${textoAvaliacao(imc)})`);
// }

// imc(altura, peso)

// fatorial ------------------------------------------------------------------------------------

// let numero = prompt("Diga um número para ter seu fatorial calculado:");

// function calcularFatorial(numero) {
//     let numeroInicial = numero;
//     let fatorial = numero;
//     while (numero > 1) {
//         numero--;
//         fatorial = fatorial * (numero);
//     }
//     // return(fatorial)
//     alert(`O fatorial de ${numeroInicial} é ${fatorial}.`)
// }

// calcularFatorial(numero);

// converter dólar ------------------------------------------------------------------------------------
// let valor = prompt('Diga um valor em reais para ser convertido em dólar (use "." como separador de centavos):');

// function converterDolar(valor) {
//     dolar = (valor * 4.8).toFixed(2);
//     alert(`R$ ${valor} são US$ ${dolar}`);
// }

// converterDolar(valor);

// perimetro -----------------------------------------------------------------------------------------

// let largura = prompt("Qual a largura da sala (em metros)?")
// let comprimento = prompt("Qual o comprimento da sala (em metros)?")

// function exibirTextoNaTela(tag, texto) {
//     let campo = document.querySelector(tag);
//     campo.innerHTML = texto;
// }

// function calcularArea(largura, comprimento) {
//     let area = largura * comprimento;
//     return area;
// }

// function calcularPerimetro(largura, comprimento) {
//     let perimetro = (largura * 2) + (comprimento * 2);
//     return perimetro;
// }

// let area = calcularArea(largura, comprimento)
// let perimetro = calcularPerimetro(largura, comprimento)

// alert(`A área da sala é ${area} m² e o seu perímetro é ${perimetro} m.`)

// exibirTextoNaTela('h1', 'Calcular perímetro da sala')
// exibirTextoNaTela('p', `A área da sala é ${area} e o seu perímetro é ${perimetro}.`)


// tabuada --------------------------------------------------------------------------------------------
let numero = prompt("Diga um número");

function mostrarTabuada(numero) {
    for (let i = 1; i <= 10; i++) {
        let resultado = numero * i;
        console.log(`${numero} x ${i} = ${resultado}`);
    }
}

// Exemplo de uso
mostrarTabuada(numero);



