$(function(){
    $('#sendcreditcard').click(sendcreditcard);
function sendcreditcard() {
    alert("You have submitted your creditcard");
    var data = 
        {CCNumber: $("#CCNumber").val(), 
        CCCode: $("#CCCode").val(),
        ExpDate: $("#ExpDate").val(),
        CCType: $("#CCType").val()		
    };
            
    $.ajax({
        url: domain + '/creditcard',
        type: 'POST',
        data: data, 
    });	
}
});
