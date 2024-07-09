$(document).ready(function() {

    function checkEmailAvailability(key,step){
        const msg = $('#msg');
        console.log('steps', step)
        // check-email-availability
        $.ajax({
            url: window.BASE_URL + 'api/check-email-availability/' + key + '/',
            type: 'GET',
            dataType: 'json',
            success: function (data) {
            console.log(data)
            if (step ==1){
                if (data.exist) {
                    msg.text('This email is already registered with us, please try another email').removeClass('text-secondary').addClass('text-danger');
                  } else {
                    msg.text('Valid email address').removeClass('text-danger').addClass('text-success');
                    $('#password1').attr('disabled', false);
                  }
            }else if(step ==2){
                if (data.exist) {
                    msg.text('').removeClass('text-danger').addClass('text-success');
                    $('#btn_login').attr('disabled', false);
                    $('#password2').attr('disabled', false);
                  } else {
                    msg.text('Your email is not registered with us').removeClass('text-success').addClass('text-danger');
                    $('#btn_login').attr('disabled', true);
                    $('#password2').attr('disabled', true);
                  }
            }
              
            }
          })
    }
    // validate email
    $("#email").on('input', function(){
        const email = $('#email').val();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const msg = $('#msg');
        $('#btn_create_account').attr('disabled', true);
        if (emailRegex.test(email)) {
            checkEmailAvailability(email,1)
            
        } else {
            msg.text('Please Enter valid email address').removeClass('text-success').addClass('text-secondary');
            $('#password1').attr('disabled', true);
        }
    })

    $("#email2").on('input', function(){
        const email = $('#email2').val();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const msg = $('#msg');
        $('#btn_create_account').attr('disabled', true);
        if (emailRegex.test(email)) {
            checkEmailAvailability(email,2)
        } else {
            msg.text('Please Enter valid email address').removeClass('text-success').addClass('text-secondary');
            $('#password1').attr('disabled', true);
        }
    })

    $("#forgot_password_email").on('input', function(){
        const email = $('#forgot_password_email').val();
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        const msg = $('#msg');
        if (emailRegex.test(email)) {
            $('#submit_request').attr('disabled', false)
        } else {
            msg.text('Please Enter valid email address').removeClass('text-success').addClass('text-secondary');
            $('#submit_request').attr('disabled', true);
        }
    })

    

    // password 1 validation
    $('#password1').on('input', function() {
        const pas1 = $('#password1').val();
        const pass_length = pas1.length;
        const msg = $('#msg');

        $('#btn_create_account').attr('disabled', true);
        if(pass_length >8 && pass_length < 20){
            msg.text('Password ok!').removeClass('text-secondary').addClass('text-success');
            $('#password2_layout').removeClass('d-none');
            $('#password2').attr('disabled', false);

        }else{
            msg.text('Password length must be more than 8 and less than 20 characters').removeClass('text-success').addClass('text-secondary');
            $('#password2').attr('disabled', true);
        }
    });

    // confirm password validation
    $('#password2').on('input', function() {
        const pas1 = $('#password1').val();
        const pas2 = $('#password2').val();
        const pass_length = pas1.length;
        const msg = $('#msg');

        console.log(pas1.length);
        if(pas1 == pas2){
            msg.text('Password match!').removeClass('text-secondary').addClass('text-success');
            $('#btn_create_account').attr('disabled', false);
        }else{
            msg.text('Password not match..').removeClass('text-success').addClass('text-secondary');
            $('#btn_create_account').attr('disabled', true);
        }
    });
});