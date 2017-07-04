/**
 * Created by alasdairjohnson on 6/3/17.
 */

$(document).ready(function () {
  //table
    $.ajax({
      url: '/api/getInv',
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
});

// function createTable(data){
//     console.log(data)
//     $('#local').dynatable({
//       dataset: {
//         records: data
//       }
//     });
//
// }


// function on_click() {
//     console.log("clicked")
//   $.get($SCRIPT_ROOT + "/itemPopUp")//load the route
//      .done(function(data) {//get the data from render temlate
//          $('#message-model-content').html(data);//load that data in the modal
//          $('#user1Message').modal('show');// show the modal
//          $("#postReply").bind( 'click', min);//minamize the modal and close it
//             })
//     }
function min() {
    console.log("minamizing")
    $('#user1Message').modal('hide');
    $('#calModal').modal('show');
  }
//https://www.youtube.com/watch?v=JmtM9f9Ns90
function makePop(id) {
    console.log(id);
    // console.log($.get($SCRIPT_ROOT + '/edit/getItem/' + id))
    $.get('/api/getItem/' + id)
    .done(function(data) {
            $('#message-model-content').html(data);
            $('#user1Message').modal('show');
          });
}