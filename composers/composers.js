function play() {
 $('#status').html('<i class="fa fa-cog fa-spin" style="font-size:30px;color:gray;"></i>');

 $.ajax({
  url: '/composers/',
  method: 'POST',
//  data: {
//   m: $('#id').val(),
//   a: $('#id2').val()
//  },

  dataType: 'html',
  success: function success(html) {
   $('#status').html(html);
  }
 });

};

$(document).click(function(e) {
  if (e.target.id == "play") {
    play();
  }
});
