function app() {
    const campo_valor_litro_alcool = document.getElementById('valor_litro_alcool')
    const teste = document.getElementById('teste')
    console.log('teste -> '+teste)
    console.log('campo_valor_litro_alcool -> '+campo_valor_litro_alcool)
    teste.innerText = 'Seu palpite está muito baixo234!'
}
app()