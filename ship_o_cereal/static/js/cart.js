var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var ItemID = this.dataset.item
        var action = this.dataset.action
        if (this.name === 'intfield') {
            var quantity = document.getElementById('add-to-cart-amount-btn').value
        }
        else {
            var quantity = this.dataset.quantity
        }
        console.log('ItemID', ItemID, 'action', action, 'quantity', quantity)

        console.log('USER', user)
        if (user === 'AnonymousUser') {
            console.log('Not logged in')
        }
        updateUserOrder(ItemID, action, quantity)
    })
}

function promoCodeValidation() {
    insertedPromo = document.getElementById('promo-box').value
    totalPrice = document.getElementById('total-price').innerHTML

    var url = '/cart/promo/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({
            'promo_name': insertedPromo,
            'total_price': totalPrice
        })
    })
        .then((response) =>{
            return response.json()
        })
        .then((data) =>{
            console.log('data', data)
            var varia = window.location.href.split('/')
            if (varia[varia.length-2] == "cart") {
                window.location.reload()
            }
        })
}

function updateUserOrder(ItemID, action, quantity) {
    console.log('User is logged in, sending data')

    var url = '/cart/edit_item/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'ItemID': ItemID, 'action': action, 'quantity': quantity})
    })
    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data', data)

    })
    .then((data) => {
        var varia = window.location.href.split('/')
        if (varia[varia.length-2] == "cart") {
            window.location.reload()
        } else {
            document.getElementById('add-alert').innerHTML = `<div class="alert alert-warning alert-dismissible fade show" role="alert">
                    <strong>Added!</strong> You can view the item in the shopping cart.
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>`
        }
    })
}


