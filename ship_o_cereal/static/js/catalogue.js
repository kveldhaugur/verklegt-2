function searchFromHistory(object) {
    $('#search-box').val(object);
    document.searchForm.submit();
}

function sortByProperty(property){
   return function(a,b){
      if(a[property] > b[property])
         return 1;
      else if(a[property] < b[property])
         return -1;
      return 0;
   }
}

function sortByPropertyInverse(property){
   return function(a,b){
      if(a[property] < b[property])
         return 1;
      else if(a[property] > b[property])
         return -1;
      return 0;
   }
}

$(document).ready(function() {
    $('#sort-by').trigger('change');
    $('#sort-by').change(function(e) {
        e.preventDefault();
        var selectedOption = $(this).children("option:selected").val();
        $.ajax( {
            url: 'get_tags/',
            type: 'GET',
            contenttype: 'application/json; charset=utf-8',
            data: {
                recentSearch: recentSearch,
                recentTag: recentTag,
            },
            dataType: 'json',
            success: function(resp) {
                if (selectedOption === 'lth') {
                    order = 'Price';
                    var newArr = resp.data.sort(sortByProperty(order));
                } else if (selectedOption === 'htl'){
                    order = 'Price';
                    var newArr = resp.data.sort(sortByPropertyInverse(order));
                } else if (selectedOption === 'az'){
                    order = 'Name';
                    var newArr = resp.data.sort(sortByProperty(order));
                } else {
                    order = 'Name';
                    var newArr = resp.data.sort(sortByPropertyInverse(order));
                }

                var newHtml = newArr.map(d => {
                    return `<div class="card" style="width: 18rem;">
                            <a href="/catalogue/${d.ItemID}">
                                <img src="/static/images/Items/${d.Image}?v=${d.updated_at}" class="card-img-top" alt="${d.Image}"/>
                                <div class="item-price">${d.Price} kr.</div>
                                <div class="card-body">
                                    <h5 class="card-title">${d.Name}</h5>
                                    <a href="/catalogue/${d.ItemID}" class="btn btn-primary">See Details</a>
                                    <button data-quantity="1" data-item=${d.ItemID} data-action="add" class="btn btn-primary add-btn update-cart">Add to Cart</button>
                                </div>
                            </a>
                        </div>`
                });
                $('.items').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        }).then((response) =>{
            addCartListeners();
        })
    });
});

$(document).ready(function() {
    $('#filter-by').trigger('change');
    $('#filter-by').change(function(e) {
        e.preventDefault();
        var filterbutton = document.getElementById('filter_by_hidden');
        filterbutton.click();
    });
});

function ShowHistory() {
    var x = document.getElementById("history_container");
    x.classList.toggle("show")
}

function performAjax (searchText) {
    $.ajax( {
            url: '/catalogue/?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="card" style="width: 18rem;">
                            <a href="/catalogue/${d.ItemID}">
                                <img src="/static/images/Items/${d.Image}?v=${d.updated_at}" class="card-img-top" alt="${d.Image}"/>
                                <div class="item-price">${d.Price} kr.</div>
                                <div class="card-body">
                                    <h5 class="card-title">${d.Name}</h5>
                                    <a href="/catalogue/${d.ItemID}" class="btn btn-primary">See Details</a>
                                    <button data-quantity="1" data-item=${d.ItemID} data-action="add" class="btn btn-primary add-btn update-cart">Add to Cart</button>
                                </div>
                            </a>
                        </div>`
                });
                $('.items').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    .then((response) =>{
            addCartListeners();
        })
};