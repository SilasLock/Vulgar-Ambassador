/**
 * Created by alasdairjohnson on 6/3/17.
 */

$(document).ready(function () {
    //table
    CreateTable("local");
    //bind backpack to tree
    $("#backpack").bind('click', function(){
        makeBackpackPop();
    });
});



function makeBackpackPop(){
    console.log("clicked");
    $.get('/api/getBackpackPopUp')
    .done(function(data) {
            $('#message-model-content').html(data);
            $('#user1Message').modal('show');
          });
}



function min() {
    console.log("minamizing")
    $('#user1Message').modal('hide');
    $('#calModal').modal('show');
  }
//https://www.youtube.com/watch?v=JmtM9f9Ns90
function getModal(id) {
    console.log(id);
    $.get('/api/getItem/' + id)
    .done(function(data) {
            $('#message-model-content').html(data);
            $('#user1Message').modal('show');
          });
}
/**
 * Parama tableID: the id of the table we which to create
 * returns: creates a table with modals yay
 */
function CreateTable(tableID) {
    var table = $("#" + tableID).DataTable({ //targets table and creates table
        "ajax": {
            "url": "/api/getInv"
        },
        "columns": [{
                "data": "itemName"
            },
            {
                "data": "itemCatagory"
            }
        ]
        //, "initComplete": function() {
        //     bindModal(dataType);
        // }
    })
    $("#" + tableID + " tbody").on('click', 'tr', function() {
        getModal(table.row(this).data().id);
    });
}