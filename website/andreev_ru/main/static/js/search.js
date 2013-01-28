App = {
    search: {
        selector: '.search-box',
        defaultTimeout: 200,
        timeout: null,
        search: function(){
            var query = $(App.search.selector).val();
            if (query.length >= 3) {
                console.log('/' + window.Config.lang + '/search_json/?query=' + query);
                $.get('/' + window.Config.lang + '/search_json/?query=' + query, function(data){
                    App.search.receive(data)
                });
            } else {
                App.search.receive([]);
            }
        },
        receive: function(items){
            console.log(items);

            if (items.length > 0) {
                var results = _.map(items, function(item){ return App.search.render(item) });
                var result =  _.reduce(results, function(memo, value){ return memo + value}, '');
                $('.search-popover-results').html(result);
                $('.search-popover-all-results').html('<a href="#">' + window.Config.all_results + '</a>');
            } else {
                $('.search-popover-results').html('');
                $('.search-popover-all-results').html(window.Config.no_results);
            }
        },
        render: function(item){
            var template =
                '<li>' +
                '    <a class="search-popover-link" href="@href">' +
                '    <div class="search-popover-image"><img src="@image"></div>' +
                '    <div class="search-popover-description"><h5>@heading</h5>@content</div>' +
                '    </a>' +
                '</li>';
            return template
                .replace('@href',    item.href)
                .replace('@image',   item.image)
                .replace('@heading', item.heading)
                .replace('@content', item.content)
        }
    }
};


$(function(){

    // Prepare ui

    $('.search-box').keyup(function() {
        var query = $(App.search.selector).val();
        if (query.length >= 3) {
            $('.search-popover').addClass('search-popover-focused');
        } else {
            $('.search-popover').removeClass('search-popover-focused');
        }
    });

    $('.search-box').focusout(function() {
        $('.search-popover').removeClass('search-popover-focused');
    });
    $('.search-box').focus(function() {
        var query = $(App.search.selector).val();
        if (query.length >= 3) {
            $('.search-popover').addClass('search-popover-focused');
        }
    });


    var template = $('#search-result').html();

    App.search.timeout = null;
    $(App.search.selector).keyup(function(){
        if (App.search.timeout != null) { clearTimeout(App.search.timeout); }
        App.search.timeout = setTimeout(App.search.search, App.search.defaultTimeout)
    });


    $('.search-popover-all-results').click(function(){
        var query = $(App.search.selector).val();
        window.location = window.Config.search_url + '?query=' + query
    });

});
