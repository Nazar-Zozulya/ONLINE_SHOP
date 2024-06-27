function editImage(){
    // Отримуємо всі кнопки зміни картинки
    const buttonsSumbit = document.querySelectorAll(".change-image")
    // створюемо цикл для всіх кнопок
    for (let count = 0; count < buttonsSumbit.length; count++){
        // Вибираємо конкретну кнопку
        let button = buttonsSumbit[count]
        // Задаємо умову при натисканні на кнопку
        button.addEventListener(
            "click",
            (event) => {
                // отримуємо поле змінни карти нки
                let input = document.querySelector(".input-change")
                // відкриваємо модальне вікно
                document.querySelector(".modal-edit").style.display = "flex"
                // замінюємо картинку
                input.type = "file"
                input.id = button.id
                input.accept = "image/*"
                input.name = "image"
                document.querySelector('.submit-change').value = `image-${button.id}`
            }
        )
    }
}
export default editImage