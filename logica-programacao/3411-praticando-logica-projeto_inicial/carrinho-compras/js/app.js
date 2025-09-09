let totalGeral;
limpar();

function adicionar() {
    // recuperar valores: nome do produto, quantidade e valor
    let produto = document.getElementById('produto').value;
    let nomeProduto = produto.split('-')[0];
    let valorUnitario = parseInt(produto.split('R$')[1]);
    let quantidade = parseInt(document.getElementById('quantidade').value);

    // verificar se a quantidade inserida é maior que 0
    if (quantidade <= 0) {
        alert('A quantidade deve ser maior que 0!')
    } else {
        // calcular o preço (subtotal)
        let preco = quantidade * valorUnitario;

        // adicionar no carrinho
        let carrinho = document.getElementById('lista-produtos');
        carrinho.innerHTML = carrinho.innerHTML + `<section class="carrinho__produtos__produto">
        <span class="texto-azul">${quantidade}x</span> ${nomeProduto} <span class="texto-azul">R$${preco}</span>
        </section>`;

        totalGeral = totalGeral + preco;

        // atualizar o valor total
        let total = document.getElementById('valor-total');
        total.textContent = `R$ ${totalGeral}`;

        // limpar quantidade
        document.getElementById('quantidade').value = 0;
    }

}

function limpar() {
    totalGeral = 0;
    document.getElementById('lista-produtos').innerHTML = '';
    document.getElementById('valor-total').textContent = "R$ 0";
}