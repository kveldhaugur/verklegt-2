var updateBtns = document.getElementsByClassName('update-cart')

for(var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var ItemID = this.dataset.item
        var action = this.dataset.action
        var quantity = this.dataset.quantity
        console.log('ItemID', ItemID, 'action', action, 'quantity', quantity)

        console.log('USER', user)
        if (user === 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            updateUserOrder(ItemID, action, quantity)
        }
    })
}

function updateUserOrder(ItemID, action) {
    console.log('User is logged in, sending data')

    var url = '/update_item/'

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
}