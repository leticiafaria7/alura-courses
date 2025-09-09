let titulo = document.querySelector('h1');
titulo.innerHTML = 'Hora do desafio!';

function verificarClickConsole() {
    console.log("O botão 'Console' foi clicado!")
}

function verificarClickAlert() {
    alert("Eu amo JS!")
}

function verificarPrompt() {
    let cidade = prompt('Diga o nome de uma cidade no Brasil:')
    alert(`Estive em ${cidade} e lembrei de você!`)
}

function verificarSoma() {
    let numero1 = prompt("Escolha um número inteiro:")
    let numero2 = prompt("Escolha outro número inteiro:")
    let soma = parseInt(numero1) + parseInt(numero2)
    alert(`A soma de ${numero1} e ${numero2} é ${soma}`)
}