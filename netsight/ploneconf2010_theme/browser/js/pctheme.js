jq(document).ready(function() {
    jq('.schedule .talk h3 a').prepOverlay({
        subtype:'ajax',
	urlmatch:'$',
	urlreplace:' #content > *',
	config:{expose:{color:'#111'}}
    });

    jq('.schedule .talk a.keyword').click(function(event){
	event.preventDefault();
	var kw = 'keyword-'+jq(this).attr('rel');
	if (jq(this).hasClass('selected')){
	    jq('.keywords a.selected').removeClass('selected').attr('title', 'Filter on this topic');
	    jq('.schedule .talk').animate({opacity:0.99},'fast', function(){
		jq(this).attr('style','opacity:');
	    });
	}
	else{
	    jq('.keywords a.selected').removeClass('selected');
	    jq('.schedule .talk').each(function(){
		var talk = jq(this);
		var kw_elem = talk.find(".keywords a[class*='"+kw+"']");
		if(kw_elem.length){
		    talk.animate({opacity:0.99},'fast', function(){
			jq(this).attr('style','opacity:');
		    });
		    kw_elem.addClass('selected').attr('title', 'Remove this filter');
		}
		else{
		    talk.animate({opacity:0.25}, 'fast');
		}
	    });
	}
    });

    
    jq("#banners").cycle({
        fx: 'scrollUp',
        timeout:  4000,
	pause:    0 
    });
    
    
});