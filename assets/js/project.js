/**
 * Created by root on 18-7-18.
 */
// 检测全局标记
window["addcheckbit"]={
    add_ProjectName_checkbit:false,
    add_ProjectFrom_checkbit:false,
    add_ProjectUser_checkbit:false,
    add_ProjectMsg_checkbit:false,
}
// 项目名唯一性检测
function CheckProjectName() {
    var add_ProjectName=$("input[name='add_ProjectName']").val();
    // alert(add_ProjectName);
    if ( add_ProjectName.length==0){
        $("input[name='add_ProjectName']").parent().attr("class",'am-u-sm-9 am-form-error');
        $("input[name='add_ProjectName']").siblings("span").attr("class",'am-icon-times').text('项目名称不能为空');
    }
    else{
        $.ajax({
            url:'/project/chechprojectname',
            type:'POST',
            data:{add_ProjectName:add_ProjectName},
            success:function(msg){
                var data = jQuery.parseJSON(msg);
                //alert(data.data.add_user_name_checkbit)
                if (data.data.add_ProjectName_checkbit == true){
                    //显示成功
                    $("input[name='add_ProjectName']").parent().attr("class",'am-u-sm-9 am-form-success');
                    $("input[name='add_ProjectName']").siblings("span").attr("class",'am-icon-check').text('');
                    addcheckbit.add_ProjectName_checkbit=true;
                }
                else {
                    //显示错误
                    $("input[name='add_ProjectName']").parent().attr("class",'am-u-sm-9 am-form-error');
                    $("input[name='add_ProjectName']").siblings("span").attr("class",'am-icon-times').text('项目名称重复');
                    //显示警告
                    // $("input[name='add_user_name']").parent().attr("class",'am-u-sm-9 am-form-warning');
                    // $("input[name='add_user_name']").after('<span class="am-icon-warning"></span>');
                    addcheckbit.add_ProjectName_checkbit=false;
                }
            },
            error:function(){
                console.log('检测用户名唯一性失败')
            }
        })
    }
}
// 检测项目所属部门不能为空
function CheckProjectFrom() {
    var add_ProjectFrom=$("input[name='add_ProjectFrom']").val();
    // alert(add_ProjectFrom);
    if ( add_ProjectFrom.length==0){
        $("input[name='add_ProjectFrom']").parent().attr("class",'am-u-sm-9 am-form-error');
        $("input[name='add_ProjectFrom']").siblings("span").attr("class",'am-icon-times').text('项目所属部门不能为空');
    }
    else{
        $("input[name='add_ProjectFrom']").parent().attr("class",'am-u-sm-9 am-form-success');
        $("input[name='add_ProjectFrom']").siblings("span").attr("class",'am-icon-check').text('');
        addcheckbit.add_ProjectFrom_checkbit=true;
    }
}
// 检测项目负责人不能为空
function CheckProjectUser() {
    var add_ProjectUser=$("input[name='add_ProjectUser']").val();
    // alert(add_ProjectUser);
    if ( add_ProjectUser.length==0){
        $("input[name='add_ProjectUser']").parent().attr("class",'am-u-sm-9 am-form-error');
        $("input[name='add_ProjectUser']").siblings("span").attr("class",'am-icon-times').text('项目负责人不能为空');
    }
    else{
        $("input[name='add_ProjectUser']").parent().attr("class",'am-u-sm-9 am-form-success');
        $("input[name='add_ProjectUser']").siblings("span").attr("class",'am-icon-check').text('');
        addcheckbit.add_ProjectUser_checkbit=true;
    }
}
// 检测项目描述不能为空
function CheckProjectMsg() {
    var add_ProjectMsg=$("textarea[name='add_ProjectMsg']").val();
    // alert(add_ProjectMsg);
    if ( add_ProjectMsg.length==0){
        $("textarea[name='add_ProjectMsg']").parent().attr("class",'am-u-sm-9 am-form-error');
        $("textarea[name='add_ProjectMsg']").siblings("span").attr("class",'am-icon-times').text('项目描述不能为空');
    }
    else{
        $("textarea[name='add_ProjectMsg']").parent().attr("class",'am-u-sm-9 am-form-success');
        $("textarea[name='add_ProjectMsg']").siblings("span").attr("class",'am-icon-check').text('');
        addcheckbit.add_ProjectMsg_checkbit=true;
    }
}
// 项目添加提交
$(function() {
  $('#doc-prompt-toggle').on('click', function() {
    $('#project_add').modal({
      relatedTarget: this,
      onConfirm: function(e) {
          if (!(addcheckbit.add_ProjectName_checkbit&&addcheckbit.add_ProjectFrom_checkbit&&addcheckbit.add_ProjectUser_checkbit&&addcheckbit.add_ProjectMsg_checkbit) )
            {
                $('#add_Project_error').modal(open);
            }
          else
              {
                  $.ajax({
                      url:'/project/addproject',
                      type:'POST',
                      data:{
                          add_ProjectName:$("input[name='add_ProjectName']").val(),
                          add_ProjectFrom:$("input[name='add_ProjectFrom']").val(),
                          add_ProjectUser:$("input[name='add_ProjectUser']").val(),
                          add_ProjectMsg:$("textarea[name='add_ProjectMsg']").val(),
                      },
                      success:function (arg) {
                          var obj = jQuery.parseJSON(arg);
                          if (obj.data.add_project_check == true){
                              delete addcheckbit
                              $('#add_user_aleat_success').modal(open)
                              setTimeout(function(){window.location.href='/project/index'},1000);
                          }
                          else{
                              console.log(obj.data.error_code)
                          }
                      },
                      error:function (arg) {
                           console.log(arg)
                      }
                  })
        // alert($("input[name='add_ProjectName']").val() + '|' + $("input[name='add_ProjectFrom']").val() + '|' +$("input[name='add_ProjectUser']").val()  + '|' + $("textarea[name='add_ProjectMsg']").val());
        // alert('输入' + e.data || '');
              }
      },
      onCancel: function(e) {
        // alert('取消');
      }
    });
  });
});
// 点击编辑跳转到编辑页面
function GoToProjectUpdate(rag) {
    Tourl='/project/update?ID='+rag;
    setTimeout(function(){window.location.href=Tourl},0);
    // window.location.href(url);
    // alert('aaa')
}
// 编辑页面提交
function SaveUpdate(arg){
  // alert(arg);
  var ID=arg;
  var Update_ProjectFrom=$("input[name='Update_ProjectFrom']").val();
  var Update_ProjectUser=$("input[name='Update_ProjectUser']").val();
  var Update_ProjectMsg=$("textarea[name='Update_ProjectMsg']").val();
  // alert(Update_ProjectFrom);
  // alert(Update_ProjectUser);
  // alert(Update_ProjectMsg);
  if (Update_ProjectFrom.length == 0 ) {
    // alert('asdasdas');
    $("input[name='Update_ProjectFrom']").parent().attr("class",'am-u-sm-7 am-form-error');
  }
  else{
    $("input[name='Update_ProjectFrom']").parent().attr("class",'am-u-sm-7');
  }
  if (Update_ProjectUser.length == 0 ) {
    // alert('asdasdas');
    $("input[name='Update_ProjectUser']").parent().attr("class",'am-u-sm-7 am-form-error');
  }
  else{
    $("input[name='Update_ProjectUser']").parent().attr("class",'am-u-sm-7');
  }
  if (Update_ProjectMsg.length == 0 ) {
    // alert('asdasdas');
    $("textarea[name='Update_ProjectMsg']").parent().attr("class",'am-u-sm-7 am-form-error');
  }
  else{
    $("textarea[name='Update_ProjectMsg']").parent().attr("class",'am-u-sm-7 ');
  }

  if ( ID && Update_ProjectFrom && Update_ProjectUser && Update_ProjectMsg) {
    $.ajax({
        url:'/project/update',
        type:'POST',
        data:{
            Update_Project_Id:ID,
            Update_Project_From:Update_ProjectFrom,
            Update_Project_User:Update_ProjectUser,
            Updat_Project_Msg:Update_ProjectMsg,
        },
        success:function (arg) {
            var obj = jQuery.parseJSON(arg);
            if (obj.data.UpCheck == true){
                // delete addcheckbit
                $('#Update_Success').modal(open)
                setTimeout(function(){window.location.href='/project/index'},1000);
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
  else{
    $('#Update_Error').modal(open)
  }

}
// 编辑页面取消跳转项目首页
function Return_ProjectIndex(rag) {
    // Tourl='/project/update?ID='+rag;
    setTimeout(function(){window.location.href='/project/index'},0);
    // window.location.href(url);
    // alert('aaa')
}

// 删除确认
function DeleatConfirm(arg){
  $('#deleat_project_info'+arg).modal(open)
}
// 删除项目
function Deleat_Project(arg){
  // alert(arg);
  $.ajax({
        url:'/project/deleat',
        type:'POST',
        data:{
            DeleatId:arg,
        },
        success:function (arg) {
            var obj = jQuery.parseJSON(arg);
            if (obj.data.DeleatBit == true){
                // delete addcheckbit
                $('#deleat_project').modal(open)
                setTimeout(function(){window.location.href='/project/index'},1000);
            }
            else{
              $('#deleat_project_error').modal(open)
              console.log(obj.data.error_code)
            }
        },
        error:function (arg) {
             console.log(arg)
        }
    })
}
