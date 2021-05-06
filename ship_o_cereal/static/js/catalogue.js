$(function() {
  $('#search-box').keypress(function(e) {
    var key = e.which;
    if (key == 13) // the enter key code
    {
      $('#search-btn').click();
      return false;
    }
  });
});

$(document).ready(function() {
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        if (window.location.pathname !== '/catalogue/') {
                  window.location.replace("/catalogue");
                };

        $.ajax( {
            url: '/catalogue/?search_filter=' + searchText,
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
                                    <a href="#" class="btn btn-primary">Add to Cart</a>
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
});


const sort_by = (field, reverse, primer) => {
  const key = primer ?
    function(x) {
      return primer(x[field])
    } :
    function(x) {
      return x[field]
    };
  reverse = !reverse ? 1 : -1;

  return function(a, b) {
    return a = key(a), b = key(b), reverse * ((a > b) - (b > a));
  }
}

$(document).ready(function() {
    $('#sort-by').trigger('change');
    $('#sort-by').change(function(e) {
        e.preventDefault();

        $.ajax( {
            url: '/catalogue/',
            type: 'GET',
            success: function(resp) {
                console.log(resp)

            },
            error: function(xhr, status, error) {
                // TODO Show toaster
                console.error(error);
            }
        })
    });
});
