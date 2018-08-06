/**
 * Created by root on 17-10-24.
 */
window["addcheckbit"]={
    add_user_name_checkbit:false,
    add_user_pwd_checkbit:false,
    add_user_email_checkbit:false,
    add_user_phone_checkbit:false
}
function checkusername() {
    var add_user_name=$("input[name='add_user_name']").val();
    //alert(add_user_name);
    if ( add_user_name.length==0){
        $("input[name='add_user_name']").parent().attr("class",'am-u-sm-9 am-form-error');
        $("input[name='add_user_name']").siblings("span").attr("class",'am-icon-times').text('用户名不能为空');
    }
    else{
        $.ajax({
            url:'/user/useraddcheck',
            type:'POST',
            data:{add_user_name:add_user_name},
            success:function(msg){
                var data = jQuery.parseJSON(msg);
                //alert(data.data.add_user_name_checkbit)
                if (data.data.add_user_name_checkbit == true){
                    //显示成功
                    $("input[name='add_user_name']").parent().attr("class",'am-u-sm-9 am-form-success');
                    $("input[name='add_user_name']").siblings("span").attr("class",'am-icon-check').text('');
                    addcheckbit.add_user_name_checkbit=true;
                }
                else {
                    //显示错误
                    $("input[name='add_user_name']").parent().attr("class",'am-u-sm-9 am-form-error');
                    $("input[name='add_user_name']").siblings("span").attr("class",'am-icon-times').text('用户名重复');
                    //显示警告
                    // $("input[name='add_user_name']").parent().attr("class",'am-u-sm-9 am-form-warning');
                    // $("input[name='add_user_name']").after('<span class="am-icon-warning"></span>');
                    addcheckbit.add_user_name_checkbit=false;
                }
            },
            error:function(){
                console.log('检测用户名唯一性失败')
            }
        })
    }
}

function checkuserpwd(){
    var add_user_pwd=$("input[name='add_user_pwd']").val();
    var add_user_pwd_check=$("input[name='add_user_pwd_check']").val();
    if (!!add_user_pwd && (add_user_pwd == add_user_pwd_check)){
        $("input[name='add_user_pwd']").parent().attr("class",'am-u-sm-9 am-form-success');
        $("input[name='add_user_pwd']").siblings("span").attr("class",'am-icon-check').text('');
        $("input[name='add_user_pwd_check']").parent().attr("class",'am-u-sm-9 am-form-success');
        $("input[name='add_user_pwd_check']").siblings("span").attr("class",'am-icon-check').text('');
        addcheckbit.add_user_pwd_checkbit=true;
    }
    else{
        $("input[name='add_user_pwd']").parent().attr("class",'am-u-sm-9 am-form-error');
        $("input[name='add_user_pwd']").siblings("span").attr("class",'am-icon-times').text('两次输入密码不一致');
        $("input[name='add_user_pwd_check']").parent().attr("class",'am-u-sm-9 am-form-error');
        $("input[name='add_user_pwd_check']").siblings("span").attr("class",'am-icon-times').text('两次输入密码不一致');
        addcheckbit.add_user_pwd_checkbit=false;
    }
}

function checkemail() {
    var email=$("input[name='add_user_email']").val();
    if (email.search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/) != -1) {
        $.ajax({
            url:'/user/useraddcheck',
            type:'POST',
            data:{add_user_email:email},
            success:function(arg){
                var obj = jQuery.parseJSON(arg);
                //alert(obj.data.add_user_email_checkbit)
                if (obj.data.add_user_email_checkbit == true){
                    $("input[name='add_user_email']").parent().attr("class", 'am-u-sm-9 am-form-success');
                    $("input[name='add_user_email']").siblings("span").attr("class", 'am-icon-check').text('');
                    addcheckbit.add_user_email_checkbit=true;
                }
                else {
                    $("input[name='add_user_email']").parent().attr("class", 'am-u-sm-9 am-form-error');
                    $("input[name='add_user_email']").siblings("span").attr("class", 'am-icon-times').text('邮箱已被使用');
                    addcheckbit.add_user_email_checkbit=false;
                }
            },
            error:function(){
                console.log('检测电子邮件唯一性失败')
            }
        })
    }
    else {
        $("input[name='add_user_email']").parent().attr("class", 'am-u-sm-9 am-form-error');
        $("input[name='add_user_email']").siblings("span").attr("class", 'am-icon-times').text('邮箱格式错误');
        addcheckbit.add_user_email_checkbit=false;
    }
}
function checkphone() {
    var sMobile = $("input[name='add_user_phone']").val();
    if(!!(/^1[0-9][0-9]\d{8}$/.test(sMobile))){
        $.ajax({
            url:'/user/useraddcheck',
            type:'POST',
            data:{add_user_phone:sMobile},
            success:function(arg){
                var obj = jQuery.parseJSON(arg);
                //alert(obj.data.add_user_phone_checkbit)
                if (obj.data.add_user_phone_checkbit == true){
                    $("input[name='add_user_phone']").parent().attr("class", 'am-u-sm-9 am-form-success');
                    $("input[name='add_user_phone']").siblings("span").attr("class", 'am-icon-check').text('')
                    addcheckbit.add_user_phone_checkbit=true;
                }
                else {
                    $("input[name='add_user_phone']").parent().attr("class", 'am-u-sm-9 am-form-error');
                    $("input[name='add_user_phone']").siblings("span").attr("class", 'am-icon-times').text('电话号码已被使用');
                    addcheckbit.add_user_phone_checkbit=false;
                }
            },
            error:function(){
                console.log('检测联系电话唯一性失败')
            }
        })
    }
    else{
        $("input[name='add_user_phone']").parent().attr("class", 'am-u-sm-9 am-form-error');
        $("input[name='add_user_phone']").siblings("span").attr("class", 'am-icon-times').text('不是标准电话号码');
        addcheckbit.add_user_phone_checkbit=false;
    }
}

function add_user_submit() {
    //alert(addcheckbit.add_user_name_checkbit)
    if (!(addcheckbit.add_user_name_checkbit&&addcheckbit.add_user_pwd_checkbit&&addcheckbit.add_user_email_checkbit&&addcheckbit.add_user_email_checkbit&&addcheckbit.add_user_phone_checkbit) )
        $('#add_user_aleat_error').modal(open)
    else
    {

        $.ajax({
            url:'/user/adduser',
            type:'POST',
            data:{
                add_user_name:$("input[name='add_user_name']").val(),
                add_user_pwd:$("input[name='add_user_pwd']").val(),
                add_user_phone:$("input[name='add_user_phone']").val(),
                add_user_email:$("input[name='add_user_email']").val(),
            },
            success:function (arg) {
                var obj = jQuery.parseJSON(arg);
                if (obj.data.add_user_check == true){
                    delete addcheckbit
                    $('#add_user_aleat_success').modal(open)
                    setTimeout(function(){
                        window.location.href='/'
                    },1000);
                }
                else{
                    console.log(obj.data.error_code)
                }
            },
            error:function (arg) {
                console.log(arg)
            }
        })
    }
}


function login() {
    var login_username=$("input[name='login_username']").val();
    var login_userpwd=$("input[name='login_userpwd']").val();

    //alert($.md5('1234'));
    if(login_username.length==0 || login_userpwd.length==0){
        $('#user_login_error').modal(open)
    }
    else {
        var login_userpwd_md5=$.md5(login_userpwd);
        $.ajax({
            url: '/user/login',
            type: 'POST',
            data: {
                login_username:login_username,
                login_userpwd:login_userpwd_md5,
            },
            success:function (arg) {
                var obj = jQuery.parseJSON(arg);
                //alert(obj.data.login_checkbit);
                if (obj.data.login_checkbit==true){
                    $('#user_login_success').modal(open);
                    setTimeout(function(){
                        window.location.href='/user/index'
                    },1000);
                }
                else {
                    $('#user_login_error').modal(open)
                }
            },
            error:console.log('error'),
        })
    }
}

function logout() {
    //alert('dasjds')
    $.ajax({
            url: '/user/logout',
            type: 'GET',
            success:function (arg) {
                var obj = jQuery.parseJSON(arg);
                //alert(obj.data.login_checkbit);
                if (obj.data.logout_bit==true){
                    $('#user_logout_success').modal(open);
                    setTimeout(function(){
                        window.location.href='/'
                    },1000);
                }
                else {
                    error:console.log('logout-error')
                }
            },
            error:console.log('error'),
        })
}