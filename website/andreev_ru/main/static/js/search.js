App = window.App || {
    search: {
        selector: '.search-box',
        defaultTimeout: 200,
        timeout: null,
        search: function(){
            var query = $(App.search.selector).val();
            if (query.length >= 3) {
                $.get('/' + window.Config.lang + '/search/?query=' + query, function(data){
                    App.search.receive(data)
                });
            } else {
                App.search.receive([]);
            }
        },
        receive: function(items){
            var template =
                '<li>' +
                '    <a class="search-popover-link" href="@href"></a>' +
                '    <div class="search-popover-image"><img src="@image"></div>' +
                '    <div class="search-popover-description"><h5>@heading</h5> @content</div>' +
                '</li>';
            var results = _.map(items, function(item){ return App.search.render(template, item) });
            var result =  _.reduce(results, function(memo, value){ return memo + value}, '');

            $('.search-popover-results').html(result);
        },
        render: function(string, item){
            return string
                .replace('@href',    item.href)
                .replace('@image',   item.image)
                .replace('@heading', item.heading)
                .replace('@content', item.content)
        }
    }
};


$(function(){

    // Prepare ui

    $('.search-box').focus(function() {
        $('.search-popover').addClass('search-popover-focused');
    });

    $('.search-box').focusout(function() {
        $('.search-popover').removeClass('search-popover-focused');
    });




    var template = $('#search-result').html();


    App.search.timeout = null;
    $(App.search.selector).keyup(function(){
        if (App.search.timeout != null) { clearTimeout(App.search.timeout); }
        App.search.timeout = setTimeout(App.search.search, App.search.defaultTimeout)
    });


});