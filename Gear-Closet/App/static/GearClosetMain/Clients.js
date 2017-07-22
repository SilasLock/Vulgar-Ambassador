/**
 * Created by alasdairjohnson on 7/4/17.
 */
$(document).ready(function () {
  //table
    CreateTable("ClientTable");
    $("#AddClient").bind('click', function(){
        makeClientAddPop();
    });
});



/**
 * Parama tableID: the id of the table we which to create
 * returns: creates a table with modals yay
 */
function CreateTable(tableID) {
    var table = $("#" + tableID).DataTable({ //targets table and creates table
        "ajax": {
            "url": "/api/getClientsMain"
        },
        "columns": [{
                "data": "clientName"
            },
            {
                "data": "clientStudentId"
            },
            {
                "data" : "clientEmail"
            },
            {
                "data" : "clientPhoneNumber"
            },
            {
                "data" : "button"
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

function makeClientAddPop(){
    console.log("clicked");
    $.get('/api/makeClientPopUp')
    .done(function(data) {
            $('#message-model-content').html(data);
            $('#user1Message').modal('show');
          })}

function getModal(id) {
    console.log(id);
    $.get('/api/selectClient/' + id)
    .done(function(data) {
            $('#message-model-content').html(data);
            $('#user1Message').modal('show');
          });
}