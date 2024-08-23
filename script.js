function updateRemoveButtons(){
    const removeButtons = document.querySelectorAll('.ingredient-row .btn-danger')
    if (document.querySelectorAll('.ingredient-row').length <= 3) {
        removeButtons.forEach(button => button.disabled = true)
    } else {
        removeButtons.forEach(button => button.disabled = false)
    }
}

function addIngredient(){
    const ingredientsDiv = document.getElementById('ingredients')
    const ingredientsRow = document.createElement('div')
    ingredientsRow.className = 'ingredient-row'

    const newInput = document.createElement('input')
    newInput.type = 'text'
    newInput.className = 'ingredient ingredient-input'
    newInput.placeholder = `Insira suas informações...`


    
    const removeButton = document.createElement('button')// criou o botao
    removeButton.className = 'btn-danger'
    // coloco uma cor e icone 
    removeButton.innerHTML = '<i class="bi bi-trash"></i>'
    removeButton.style.rigth = '30px'
    removeButton.onclick = () => removeIngredient(removeButton)// deu a funcao ao botao

    ingredientsRow.appendChild(newInput)
    ingredientsRow.appendChild(removeButton)
    ingredientsDiv.appendChild(ingredientsRow)

    updateRemoveButtons()
}

function removeIngredient(button) {
    const ingredientRow = button.parentElement;
    ingredientRow.remove()
    updateRemoveButtons()
}

async function submitForm() {
    const ingredientInputs = document.getElementsByClassName('ingredient')
    const ingredients = [];
    for (let i = 0; i < ingredientInputs.length; i++) {
        if (ingredientInputs[i].value) {
            ingredients.push(ingredientInputs[i].value)
        }
    }
    console.log(ingredients)
    if (ingredients.length < 3) {
        alert('Por favor, preencha pelo menos três campos!')
        return
    }
    const data = {
        ingredientes: ingredients 
    }

    try {
        const response = await fetch('http://localhost:5000/receita', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }, 
            body: JSON.stringify(data)
        })

        const result = await response.json()

        const responseDiv = document.getElementById('response')
        if (result) {
            console.log(result)
            const receita = result.join('')
            console.log(receita)
            responseDiv.innerHTML = receita
        } else {
            responseDiv.innerHTML = `<p>Erro> ${result.Erro}</p>`
        }
        responseDiv.style.display = 'block'
    } catch (error) {
        const responseDiv = document.getElementById('response')
        responseDiv.innerHTML = `<p>Erro: ${error.message}<p>`
        responseDiv.style.display = 'block'
    }
}

document.addEventListener('DOMContentLoaded', updateRemoveButtons)
