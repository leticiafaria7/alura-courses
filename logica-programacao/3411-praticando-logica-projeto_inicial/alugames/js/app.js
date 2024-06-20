let n_jogos_alug = 0;

function contarJogosAlugados() {
    console.log(`Número de jogos alugados: ${n_jogos_alug}`)
}

function alterarStatus(id) {

    let game = document.getElementById(`game-${id}`);
    let imagem = game.querySelector('.dashboard__item__img');
    let botao = game.querySelector('.dashboard__item__button');
    
    if (imagem.classList.contains('dashboard__item__img--rented')) {
        let confirmacao = prompt("Confirma a devolução do jogo? - Digite 's' para sim e 'n' para não")
        if (confirmacao == 's') {
            imagem.classList.remove('dashboard__item__img--rented');
            botao.classList.remove('dashboard__item__button--return');
            botao.textContent = 'Alugar';
            n_jogos_alug--;
        }
    } else {
        let confirmacao = prompt("Confirma que quer alugar o jogo? - Digite 's' para sim e 'n' para não")
        if (confirmacao == 's') {
            imagem.classList.add('dashboard__item__img--rented');
            botao.classList.add('dashboard__item__button--return');
            botao.textContent = 'Devolver';
            n_jogos_alug++;
        }
    }

    contarJogosAlugados()
}

// Inicializa a contagem considerando que os jogos já começam alugados
// document.addEventListener('DOMContentLoaded', function() {
//     n_jogos_alug = document.querySelectorAll('.dashboard__item__img--rented').length;
//     contarJogosAlugados();
// });

// // Função para verificar se a frase é um palíndromo
// let frase = prompt('Escreva uma palavra ou frase para verificar se é um palíndromo:')

// function verificarPalindromo(string) {

//     // remover espaços
//     var str_sem_espaco = string.replace(/\s/g, '');

//     // remover caracteres especiais e deixar em minúsculo
//     var str_sem_espaco_e_carat_esp = str_sem_espaco.normalize("NFD").replace(/[\u0300-\u036f]/g, "").replace(/[^\w\s]/gi, '').toLowerCase();

//     // transformar cada caracter em um item da lista, inverter e juntar
//     var str_reversed = str_sem_espaco_e_carat_esp.split("").reverse().join("");

//     if (str_sem_espaco_e_carat_esp == str_reversed) {
//         return alert(`Esta palavra / frase é um palíndromo!`)
//     } else {
//         return alert(`Esta palavra / frase não é um palíndromo.`)
//     }
// }

// verificarPalindromo(frase)

// ordenar lista
// let numero1 = prompt("Diga um número:")
// let numero2 = prompt("Diga outro número:")
// let numero3 = prompt("Diga mais um número:")

// let lista = [numero1, numero2, numero3]

// alert(`Números ordenados: ${lista.sort()}`)