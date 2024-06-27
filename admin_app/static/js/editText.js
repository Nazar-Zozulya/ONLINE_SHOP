function editText(){
    // отримуємо всі кнопки
    const changeName = document.querySelectorAll(".change-text")
    const changePrice = document.querySelectorAll(".change-price")
    const changeSale = document.querySelectorAll(".change-sale")
    const changePreviousPrice = document.querySelectorAll(".change-previous-price")
    // умова на змінну імені
    for (let count = 0; count < changeName.length; count++){
        let button = changeName[count]
        button.addEventListener(
            "click",
            (event) => {
                console.log('change name')
                let input = document.querySelector(".input-change")
                document.querySelector(".modal-edit").style.display = "flex"
                document.querySelector('.cover-modal').style.display = "flex"
                
                input.type = "text"
                input.id = button.id
                input.name = "name"
                let ohh = input.value
                document.querySelector('.submit-change').value = `name-${button.id}`
                console.log(ohh)
            }
        )
    }
    // умова на змінну ціни
    for (let count = 0; count < changePrice.length; count++){
        let button = changePrice[count]
        button.addEventListener(
            "click",
            (event) => {
                console.log('change price')
                let input = document.querySelector(".input-change")
                document.querySelector(".modal-edit").style.display = "flex"
                document.querySelector('.cover-modal').style.display = "flex"
                
                input.type = "number"
                input.id = button.id
                input.name = "price"
                document.querySelector('.submit-change').value = `price-${button.id}`
            }
        )
    }
    // умова на змінну знижки
    for (let count = 0; count < changeSale.length; count++){
        let button = changeSale[count]
        button.addEventListener(
            "click",
            (event) => {
                console.log('change sale')
                let input = document.querySelector(".input-change")
                document.querySelector(".modal-edit").style.display = "flex"
                document.querySelector('.cover-modal').style.display = "flex"
                
                input.type = "number"
                input.id = button.id
                input.name = "sale"
                document.querySelector('.submit-change').value = `sale-${button.id}`
            }
        )
    }
    // умова на минулу ціну
    for (let count = 0; count < changePreviousPrice.length; count++){
        let button = changePreviousPrice[count]
        button.addEventListener(
            "click",
            (event) => {
                console.log('change previous price')
                let input = document.querySelector(".input-change")
                document.querySelector(".modal-edit").style.display = "flex"
                document.querySelector('.cover-modal').style.display = "flex"
                
                input.type = "number"
                input.id = button.id
                input.name = "previous_price"
                document.querySelector('.submit-change').value = `previous_price-${button.id}`
            }
        )
    }
}

export default editText