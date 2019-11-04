$(document).ready(function(){
    $("form.input").submit(function(validate){
      var firstname =document.getElementById("stylistfirstname").value;
      var lastname =document.getElementById("stylistlastname").value;
      var email=document.getElementById("stylistemail").value;
      var phone = documet.getElementById("stylistphonenumber").value
        var password =document.getElementById("Yourpassword").value;
        var message = document.getElementById("message").value;
        var content = document.getElementsByClassName("content".value)
  
    //     // if (username == ""){
    //     //   alert("please enter username");
    //     //   formLogin.username.focus();
    //     //   return false;
    //     // }
    //     // if (password == ""){
    //     //   alert("Please input password!")
    //     //   formLogin.password.focus();
    //     //   return false;
    //     // }
        if (firstname =="ben", lastname=="king", email=="ben@gmail.com", phone=="0710000000" && password =="123"){   
          // alert("Login successful");
          window.location.href ="stylistsignup.html";
          return false;
          $(content).hide();
          $(message).show();
        }
          else{
            // alert("Login failed! enter right  username and password.")
            $(message).show();
            event.preventDefault();
          }
        });
    });

    // var stylistWebsite = "stylistsignup"
    // localStorage.setItem('stylistWebsite',stylistWebsite);

  
