const imageRevenue = document.getElementById('revenueImage')

const revenueName = document.getElementById('revenueName')

const ingredientOne = document.getElementById('ingredientOne')
const ingredientTwo = document.getElementById('ingredientTwo')
const ingredientThree = document.getElementById('ingredientThree')
const ingredientFour = document.getElementById('ingredientFour')
const ingredientFive = document.getElementById('ingredientFive')
const ingredientSix = document.getElementById('ingredientSix')

const videoRevenue = document.getElementById('revenueVideo')

const srcRevenue = imageRevenue.getAttribute('src')

function IngredientsRevenue(first, second, third, fourth, fifth, sixth) {
    ingredientOne.textContent = (first)
    ingredientTwo.textContent = (second)
    ingredientThree.textContent = (third)
    ingredientFour.textContent = (fourth)
    ingredientFive.textContent = (fifth)
    ingredientSix.textContent = (sixth)
}

function showSushi() {
    imageRevenue.setAttribute("src", "imagens/sushi.jpg")
    revenueName.textContent = "Sushi"
    IngredientsRevenue("Peixe", "Alga", "Arroz", "Cenoura", "Barata", "Caviar")
    videoRevenue.setAttribute("src", "videos/sushimaker.mp4")
}

function showPizza() {
    imageRevenue.setAttribute("src", "imagens/pizza.jpg")
    revenueName.textContent = "Pizza"
    IngredientsRevenue("Molho de tomate", "Queijo mussarela", "Calabresa fatiada", "Cebola", "Orégano", "Azeitonas")
    videoRevenue.setAttribute("src", "videos/pizzavideo.mp4")
}

function showBurger() {
    imageRevenue.setAttribute("src", "imagens/HamburguerAlcatraComBacon_1-scaled.jpg")
    revenueName.textContent = "Hamburger"
    IngredientsRevenue("Pão", "Carne de Hamburger", "Alface", "Queijo", "Tomate", "Bacon")
    videoRevenue.setAttribute("src", "videos/humburgermaker.mp4")
}

function showBarbecue() {
    imageRevenue.setAttribute("src", "imagens/churrasco.webp")
    revenueName.textContent = "Churrasco"
    IngredientsRevenue("Fogo", "Linguição", "Picanha", "Pão de alho", "Frango", "Coração de galinha")
    videoRevenue.setAttribute("src", "videos/churrracomaker.mp4")
}

function showCake() {
    imageRevenue.setAttribute("src", "imagens/bolo.jpg")
    revenueName.textContent = "Bolo"
    IngredientsRevenue("Chocolate", "Massa de bolo", "Brigadeiro", "Ovo", "Leite", "Vó")
    videoRevenue.setAttribute("src", "videos/cakemaker.mp4")
}

function showBrig() {
    imageRevenue.setAttribute("src", "imagens/brigadeiro.webp")
    revenueName.textContent = "Brigadeiro"
    IngredientsRevenue("Chocolate", "Leite condensado", "Brigadeiro", "Mão", "Forma", "")
    videoRevenue.setAttribute("src", "videos/brigadeiromaker.mp4")
}


