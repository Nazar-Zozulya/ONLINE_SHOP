// отримуємо кнопку додавання в cart
const buttonBuy = document.querySelectorAll(selectors = '.buy-button')
// робимо цикл для всіх продуктів
for (let count = 0; count < buttonBuy.length; count++) {
    let button = buttonBuy[count]
    var countInCart = 0
    // задаємо умову на додаванн продукту в cart
    button.addEventListener(type = 'click', listener = function(event){
        // задаємо умову якщо cookies не пуста
        if (document.cookie != ''){
            // обрізаємо cookies
            let currentProduct = document.cookie.split('=')[1]
            // додаємо до cookies продукт
            let idProduct = currentProduct + ' ' + button.value
            document.cookie = `product = ${idProduct}`
            

            currentProduct = document.cookie.split(' ')
            countInCart += 1
            window.location.reload()
            // countCart.textContent = currentProduct.length
        }
        // якщо пуста додаємо продукт по id
        else {
            document.cookie = `product = ${button.id}`
        }
    })
}

