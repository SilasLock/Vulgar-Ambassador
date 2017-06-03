/**
 * Created by alasdairjohnson on 5/14/17.
 */

$(document).ready(function () {
  //Side Bar
  var trigger = $('.hamburger'),
      overlay = $('.overlay'),
     isClosed = false;

    trigger.click(function () {
      hamburger_cross();
    });

    function hamburger_cross() {

      if (isClosed == true) {
        overlay.hide();
        trigger.removeClass('is-open');
        trigger.addClass('is-closed');
        isClosed = false;
      } else {
        overlay.show();
        trigger.removeClass('is-closed');
        trigger.addClass('is-open');
        isClosed = true;
      }




  }
  $('[data-toggle="offcanvas"]').click(function () {
        $('#wrapper').toggleClass('toggled');
  });
  //table
$.ajax({
  url: '/edit/getInv',
  success: function(data){
    $('#local').dynatable({
      dataset: {
        records: data["records"]
        }
      // writers: {
      // _rowWriter: myRowWriter
      //   },
      // readers: {
      // _rowReader: myRowReader
      //   }
    });
    $("span.itemName").bind('click', function() {
        var contentPanelId = jQuery(this).attr("id");
        makePop(contentPanelId);
    });
  }
});




    $(window).bind('resize', function(e){
		$(".affix").css('width',$(".container-fluid" ).width());
	});
	$(window).on("scroll", function() {
		$(".affix").css('width',$(".container-fluid" ).width());
	});
// console.log($("span.itemName"))
});

function createTable(data){
    console.log(data)
    $('#local').dynatable({
      dataset: {
        records: data
      }
    });

}

function on_click() {
    console.log("clicked")
  $.get($SCRIPT_ROOT + "/itemPopUp")//load the route
     .done(function(data) {//get the data from render temlate
         $('#message-model-content').html(data);//load that data in the modal
         $('#user1Message').modal('show');// show the modal
         $("#postReply").bind( 'click', min);//minamize the modal and close it
            })
    }
function min() {
    console.log("minamizing")
    $('#user1Message').modal('hide');
    $('#calModal').modal('show');
  }
//https://www.youtube.com/watch?v=JmtM9f9Ns90
function makePop(id) {
    console.log(id);
    console.log($.get($SCRIPT_ROOT + '/edit/getItem/' + id))
    $.get($SCRIPT_ROOT + '/edit/getItem/' + id)
    .done(function(data) {
            $('#message-model-content').html(data);
            $('#user1Message').modal('show');
          });
}
 // $(function() {
 //    $('#showConversation').bind('click', function() {
 //     console.log("show conversation clicked");
 //     $.get( "/view_conversation")
 //          .done(function(data) {
 //            $('#message-model-content').html(data);
 //            $('#user1Message').modal('show');
 //          });
 //    });

function myRowWriter(rowIndex, record, columns, cellWriter) {
    var tr = '';

    // grab the record's attribute for each column
    for (var i = 0, len = columns.length; i < len; i++) {
      tr += cellWriter(columns[i], record);
    }
    // console.log(record)
    return '<tr data-stuff=' + record.customData + '>' + tr + '</tr>';
  }

function myRowReader(rowIndex, rowElement, record) {
    record.customData = $(rowElement).data('stuff');
  }
  // $(function() {
  //   $('a#calculate').bind('click', function() {
  //     $.getJSON($SCRIPT_ROOT + '/_add_numbers', {
  //       a: $('input[name="a"]').val(),
  //       b: $('input[name="b"]').val()
  //     }, function(data) {
  //       $("#result").text(data.result);
  //     });
  //     return false;
  //   });
  // });
