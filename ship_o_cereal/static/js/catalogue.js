var filteredArr = [];

/*$(function() {
  $('#search-box').keypress(function(e) {
    var key = e.which;
    if (key == 13) // the enter key code
    {
      $('#search-btn').click();
      return false;
    }
  });
});*/

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
                // TODO Show toaster
                console.error(error);
            }
        }).then((response) =>{
            addCartListeners();
        })
    });
});


/*$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();

        $.ajax( {
            url: '/catalogue/',
            type: 'GET',
            success: function(resp) {
                var newHtml = resp.data.map(d => {
                    return `<div class="card" style="width: 18rem;">
                            <a href="/catalogue/${d.ItemID}">
                                <img src="/static/images/Items/${d.Image}?v=${d.updated_at}" class="card-img-top" alt="${d.Image}"/>
                                <div class="item-price">$${d.Price}</div>
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
                // TODO Show toaster
                console.error(error);
            }
        })
    });
});*/


$(document).ready(function() {
    $('#filter-by').trigger('change');
    $('#filter-by').change(function(e) {
        e.preventDefault();
        var filterbutton = document.getElementById('filter_by_hidden');
        filterbutton.click();
        /*
        var selectedOption = Number($(this).children("option:selected").val());
        $.ajax( {
            url: 'get_tags/?search_filter=' + recentSearch,
            type: 'GET',
            success: function(resp) {
                var newArr = resp.data
                var filteredArr = []
                for (i = 0; i < newArr.length; i++) {
                    if (newArr[i].Tags.includes(selectedOption)) {
                        filteredArr.push(newArr[i]);
                    }
                };

                var newHtml = filteredArr.map(d => {
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

            },
            error: function(xhr, status, error) {
                // TODO Show toaster
                console.error(error);
            }
        })
        .then((response) =>{
            addCartListeners();
        })*/
    });
});

function ShowHistory() {
    var x = document.getElementById("history_container");
    x.classList.toggle("show")
}

/*$(document).ready(function() {
    $('.search-btn').on('click', function(e) {
        e.preventDefault();

        var searchText = $('#search-box').val();
        recentSearch = searchText;
        //moveToCatalogue();
        performAjax(searchText);
    });
});*/

function performAjax (searchText) {
    $.ajax( {
            url: '/catalogue/?search_filter=' + searchText,
            type: 'GET',
            /*beforeSend: function() {
               if (window.location.pathname !== '/catalogue/') {
                    window.location.replace('/catalogue/');
                };
            },*/
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
                // TODO Show toaster
                console.error(error);
            }
        })
    .then((response) =>{
            addCartListeners();
        })
};