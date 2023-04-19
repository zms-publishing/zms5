const get_results = async (q) => {
	const response = await fetch(`zcatalog_adapter/zcatalog_opensearch_connector/search_json?q=${q}`);
	const data = await response.json();
	compile_results(q, data);
	return false;
};

const compile_results = (q, data) => {
	data = postprocess_results(q, data);
	var hb_results_tmpl = Handlebars.compile( $('#hb_results_html').html() );
	var hb_results_html = hb_results_tmpl(data);
	$('.search-results').html( hb_results_html );

	//###@WORK############################
	debugger;
	var total = data.total;
	var fn = function(pageIndex) {
		var url = window.location.href;
		return AssembleUrlParameter(url,{"pageIndex:int":pageIndex});
	};
	GetPagination(fn,total,10,0);
	//####################################

	return false;
};

const postprocess_results = (q, data) => {
	var total = data.hits.total.value;
	var res = { 'hits':[], 'total':total, 'query':q };
	data["hits"]["hits"].forEach(x => {
		var source = x["_source"];
		var highlight = x["highlight"];
		var hit = {"path":x["_id"], "href":source["loc"], "title":source["title"], "snippet":source["standard_html"]}; 
		if (typeof highlight !== "undefined") {
			if (typeof highlight["title"] !== "undefined") {
				hit["title"] = highlight["title"];
			}
			if (typeof highlight["standard_html"] !== "undefined") {
				hit["snippet"] = highlight["standard_html"];
			}
		}
		if (hit["snippet"].length > 200) {
			hit["snippet"] = hit["snippet"].substr(0,200) + "...";
		}
		res.hits.push(hit)
	})
	return res;
};

const render_path = async (el) => {
	$.get(url='get_breadcrumbs_by_uuid', data={ 'id' : el.dataset.id }, function(data, status) {
		$(el).html(data);
		console.log(el.dataset.id, status)
	});
};

$(function() {
	$(".search-form form").submit(async function() {
		var q = $("input",this).val();
		console.log("q",q);
		$(".search-results").html(`<h2>Suche nach <code>${q}</code></h2><div title="Loading..." class="spin"></div>`);
		await get_results(q);
		$('ul.path').each(function() {
			$(this).removeClass('hidden');
			render_path(this);
		})
		return false;
	});
});