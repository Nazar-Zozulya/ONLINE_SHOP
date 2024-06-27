// Отримуємо кнопку + - і всі продукти у карті
const buttonsMinus = document.querySelectorAll(".minus")
const buttonsPlus = document.querySelectorAll(".plus")
const Products = document.querySelectorAll(".product-in-cart")

// робимо цикл для змінни ціни
for (let count = 0; count < buttonsMinus.length; count++){
    // отримуємо всі кнопки + і -
    let button = buttonsMinus[count]
    let buttonP = buttonsPlus[count]
    // задаємо умову на кнопку мінус
    button.addEventListener(
        type = "click",
        listener = function(event){
            // отримуємо cookies
            let cookies = document.cookie.split("=")[1].split(" ")
            // отримуємо всі кнопки мінус
            let button_id = button.id.split("-")[1]
            // віднімаємо 1 від кількості товару
            if (button_id in cookies || cookies == button_id){
                cookies.splice(cookies.indexOf(button_id), 1)
                button.nextElementSibling.textContent = Number(button.nextElementSibling.textContent) - 1 
                button.nextElementSibling.style.fontFamily = "«Inter», sans-serif"
                button.nextElementSibling.style.fontSize = "28px"
                button.nextElementSibling.style.fontWeight = "700"
                button.nextElementSibling.style.textAlign = "center"
                window.location.reload()
            }
            // якщо кількість продукту 0 видаляємо його
            if (button.nextElementSibling.textContent == '0'){
                document.querySelector(`#product-${button_id}`).remove()
            }
            document.cookie = `product = ${cookies.join(' ')}; path = /`
        }
    )
    // задаємо умову на кнопку плюс
    buttonP.addEventListener(
        type = "click",
        listener = function(event){
            // отримуємо cookies
            let cookies = document.cookie.split("=")[1].split(" ")
            // отримуємо всі кнопки мінус
            let button_id = buttonP.id.split("-")[1]
            // додаємо 1 до кількості товару
            if (button_id in cookies || cookies == button_id){
                cookies.push(button_id)
                buttonP.previousElementSibling.textContent = Number(buttonP.previousElementSibling.textContent) + 1
                button.nextElementSibling.style.fontFamily = "«Inter», sans-serif"
                button.nextElementSibling.style.fontSize = "28px"
                button.nextElementSibling.style.fontWeight = "700"
                button.nextElementSibling.style.textAlign = "center"
                window.location.reload()
            }

            document.cookie = `product = ${cookies.join(' ')}; path = /`
        }
    )
}