/**
 * Created by alasdairjohnson on 5/14/17.
 */
$(document).ready( function() {
    $("#local").dynatable({
        dataset: {
            records: JSON.parse($("#music").text())
        }
    });
});

 $(function() {
    $('a#calculate').bind('click', function() {
      $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $("#result").text(data.result);
      });
      return false;
    });
  });
