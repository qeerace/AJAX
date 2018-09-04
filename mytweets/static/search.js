$('#search-form').submit(function(e){
$.post('/search/', $(this).serialize(), function(data){
$('.tweets').html(data);
});
e.preventDefault();
});
function search_submit() {
     var query = $("#id_query").val();
     $("#search-results").load(
       "/search/?AJAX&query=" + encodeURIComponent(query)
     );
   return false;
   }