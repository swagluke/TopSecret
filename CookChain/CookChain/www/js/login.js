$(function(){
    //event binding
    $('#login').click(login);  
    function login() {
        
        var data = 
            {username: $("#email").val(), 
            password: $("#password").val()};
        //remove this   
        //alert("Email: " + data['email'] + "\nPassword: " + data['pass']);
            
        $.ajax({
            url: domain + '/login',
            type: 'POST',
            data: data, //might need to change 
            success: loginResponse
            //if(result=='success') {
        });
        //window.location.href = "search.html";
    }
 
    function loginResponse(res) {
        var response = JSON.stringify(JSON.parse(res));
	console.log(response)
    	if(response=="\"success\"") {
		console.log("1")
    		window.location.href = "search";
    	} else {
		console.log("2")
    		$("#password").val('');
    		$(".alert-container").append('<div data-alert class="alert-box alert round">Email and/or password incorrect.<a href="#" class="close">&times;</a></div>');
    		$(document).foundation('alert', 'reflow');
    	}
    } 
});
