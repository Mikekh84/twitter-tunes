$(document).ready(function() {
    update_one($('#trends > ul > li:first'));
    $('#trends').on('click', 'li', function(){
        update($(this));
    })
});

function check_loaded(iframe){
    if(iframe.attr('src') == '../static/loading.gif'){
        return true;
    }
    return false;
}

function update_next(cur_trend){
    next_trend_iframe = cur_trend.next().children('article').children('iframe');
    if(check_loaded(next_trend_iframe)){
        update_one(cur_trend.next());
    }
}

function update(trend){
    iframe = trend.children('article').children('iframe')
    if(check_loaded(iframe)){
        $.get('/youtube/' + trend.attr('id'), function(data){
            iframe.attr('src', data.url);
            update_next(trend);
        })
    } else {
        update_next(trend);
    }
}

function update_one(trend){
    iframe = trend.children('article').children('iframe');
    $.get('/youtube/' + trend.attr('id'), function(data){
        iframe.attr('src', data.url);
    })
}
