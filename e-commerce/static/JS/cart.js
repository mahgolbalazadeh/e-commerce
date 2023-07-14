var updateBtn = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function () {
        var productID = this.dataset.product;
        var action = this.dataset.action;
        console.log('Product ID :', productID, 'Action: ', action)
        console.log('User:', user)

        if (user === 'AnonymousUser') {
            console.log('you are not logged in!');
        } else {
            updateUserOrder(productID, action)
        }
    })
}

/*calling view Json*/

function updateUserOrder(productID, action) {
    console.log('You are logged in, data sent...')
    var url = '/update_item/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'productID': productID,
            'action': action,
        })
    })

        .then((response) => {
            return response.json()
        }).then((data) => {
        console.log('Data: ', data);
    })
}