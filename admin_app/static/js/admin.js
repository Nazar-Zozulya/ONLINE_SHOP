// Відкриваємо меню створення продукту
function openDialog(){
    // отримуємо модальне вікно
    var create = document.querySelector('#createProduct')
    // задаємо умову при натисканні на кнопку створити продукт відкриваемо модальне вікно
    document.querySelector('#openCreateProduct').onclick = function() {
        // робимо видимими модальне вікно і задній фон
        create.style.display = 'flex'
        document.querySelector('.cover-modal').style.display = "flex"
    }
}
// Відправляємо цю функцію в main.js
export default openDialog
