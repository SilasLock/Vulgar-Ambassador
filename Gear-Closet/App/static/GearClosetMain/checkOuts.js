/**
 * Created by alasdairjohnson on 7/4/17.
 */
$(document).ready(function () {
  //table
    CreateTable("CheckoutTable");
    // $("#AddClient").bind('click', function(){
    //     makeClientAddPop();
    // });
});



/**
 * Parama tableID: the id of the table we which to create
 * returns: creates a table with modals yay
 */
function CreateTable(tableID) {
    var table = $("#" + tableID).DataTable({ //targets table and creates table
        "ajax": {
            "url": "/api/getCheckout"
        },
        "columns": [{
                "data": "clientName"
            },
            {
                "data": "studentID"
            },
            {
                "data" : "itemName"
            },
            {
                "data" : "numberOut"
            },
            {
                "data" : "dateCheckedOut"
            }
        ]
        //, "initComplete": function() {
        //     bindModal(dataType);
        // }
    })
//     $("#" + tableID + " tbody").on('click', 'tr', function() {
//         getModal(table.row(this).data().id);
//     });
// }
//
// function makeClientAddPop(){
//     console.log("clicked");
//     $.get('/api/makeClientPopUp')
//     .done(function(data) {
//             $('#message-model-content').html(data);
//             $('#user1Message').modal('show');
//           })}
//
// function getModal(id) {
//     console.log(id);
//     $.get('/api/selectClient/' + id)
//     .done(function(data) {
//             $('#message-model-content').html(data);
//             $('#user1Message').modal('show');
//           });
}/**
 * Created by ajohnson on 7/24/2017.
 */
