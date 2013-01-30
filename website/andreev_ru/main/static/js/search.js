App = {
    search: {
        selector: '.search-box',
        hidden_marker_class: 'search-popover-focused',
        popover_selector: '.search-popover',
        container_selector: '.search-container',
        defaultTimeout: 200,
        timeout: null,
        search: function(){
            var query = $(App.search.selector).val();
            if (query.length >= 3) {
                console.log('/' + window.Config.lang + '/search_json/?query=' + query);
                $.get('/' + window.Config.lang + '/search_json/?query=' + query, function(data){
                    App.search.receive(data);
                });
            } else {
                App.search.receive([]);
            }
        },
        receive: function(items){
            console.log(items);

            if (items.length > 0) {
                var results = _.map(items, function(item){ return App.search.render(item); });
                var result =  _.reduce(results, function(memo, value){ return memo + value; }, '');
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
                .replace('@content', item.content);
        },
        show: function(){
            $(App.search.popover_selector).addClass(App.search.hidden_marker_class);
            $(document).bind(
                'focusin' + App.search.container_selector +
                ' click' + App.search.container_selector,
                ' tap' + App.search.container_selector,
                function(e){
                
                if ($(e.target).closest(App.search.container_selector).length) return;
                $(document).unbind(App.search.container_selector);
                App.search.hide();

            });
        },
        hide: function(){
            $(App.search.popover_selector).removeClass(App.search.hidden_marker_class);
        },
        on_activity: function(){
            var query = $(App.search.selector).val();
            if (query.length >= 3) {
                App.search.show();
            } else {
                App.search.hide();
            }
        }
    }
};




$(function(){

    $(document).bind('tap.search-container', function(e){
        if ($(e.target).closest(App.search.container_selector).length === 0) {
            App.search.hide();
            $('form').blur();
        }
    });

    // Prepare ui
    var search_box = $(App.search.container_selector);
    var search_input = $(App.search.selector);


    search_input.keyup(App.search.on_activity).focus(App.search.on_activity);

    App.search.timeout = null;
    $(App.search.selector).keyup(function(){
        if (App.search.timeout !== null) { clearTimeout(App.search.timeout); }
        App.search.timeout = setTimeout(App.search.search, App.search.defaultTimeout);
    });


    $('.search-popover-all-results').click(function(){
        var query = $(App.search.selector).val();
        window.location = window.Config.search_url + '?query=' + query;
    });

});
