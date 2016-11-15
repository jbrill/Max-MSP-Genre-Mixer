function sendUser() {
  var name=document.getElementById( "new_username_input" );
  var fname=document.getElementById( "new_firstname_input" );
  var lname=document.getElementById( "new_lastname_input" );
  var emailin=document.getElementById( "new_email_input" );

  $.ajax({
    type: 'POST',
    contentType: "application/json; charset=UTF-8",
    url: 'http://0.0.0.0:3000/ij1dz07o/p3/api/v1/user',
    data: {
      username:name,
      firstname:fname,
      lastname:lname,
      email:emailin
    },
    success: function (response) {
      window.location.replace("http://0.0.0.0:3000/ij1dz07o/p3/login");
    }
  });

  return false;

}
