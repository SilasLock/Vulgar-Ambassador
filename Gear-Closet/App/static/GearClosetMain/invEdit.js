/**
 * Created by ajohnson on 8/16/2017.
 */
/**
 * Parama tableID: the id of the table we which to create
 * returns: creates a table with modals yay
 */
$(document).ready(function () {
    //table
    CreateTable("invTable");
    //bind backpack to tree
});


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
            },
            {
                "data": "itemQuantity"
            },
            {
                "data": "itemQuantityOut"
            },
            {
                "data": "itemPrice"
            }
        ]
    });
    $("#" + tableID + " tbody").on('click', 'tr', function() {
        getModal(table.row(this).data().id);
    });
}

function getModal(id) {
    console.log(id);
    $.get('/api/editItem/' + id)
    .done(function(data) {
            $('#message-model-content').html(data);
            $('#user1Message').modal('show');
          });
}