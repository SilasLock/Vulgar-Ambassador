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
            "url": "/api/getClientsCheckedOut"
        },
        "columns": [
            {
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
                "data" : "numberCheckedOut"
            }
        ]
        // , "initComplete": function() {
        //     bindModal(dataType);
        // }
    });
    $("#" + tableID + " tbody").on('click', 'tr', function() {
        getModal(table.row(this).data().id);
    });
    }
//
// function makeClientAddPop(){
//     console.log("clicked");
//     $.get('/api/makeClientPopUp')
//     .done(function(data) {
//             $('#message-model-content').html(data);
//             $('#user1Message').modal('show');
//           })}
//
function getModal(id) {
    console.log(id);
    $.get('/api/getClientsCheckedoutItems/' + id)
    .done(function(data) {
            $('#message-model-content').html(data["html"]);
            setDropDown(data["data"]);
            $('#user1Message').modal('show');
            $('#checkIn').on('click', function () {
            var checkbox = $(".itemCheckBox input:checkbox")
            console.log($(checkbox))
            })
          });
}
//Things that need to be done
//now we have it so that the we can access the id which is the checkedOut id as well as
//we need to put together a json response with the values for checkItemIn(self, clientID, Itemid, numberReturned)
//we also need to grab the numberReturned

function setDropDown(data){
    for (var key in data){
        setNumber(data[key]["CheckoutID"],data[key]["numCheckedOut"],data[key]["numCheckedOut"])
    }
}

function setNumber(classID, numberSelected, range){
    var $select = $("select." + classID);
    for (var i=1;i<=range;i++){
        $select.append($('<option></option>').val(i).html(i))
    }
    $select.val(numberSelected)
}
function sendData(){

}

/**
 * Created by ajohnson on 7/24/2017.
 */
