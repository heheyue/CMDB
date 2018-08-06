/**
 * Created by root on 17-12-15.
 */


function Memu_list(msg,str) {
    for (var i=0 ; i < msg.length; i++) {
        if (msg[i].hasOwnProperty("system_memu")){
            if (msg[i].hasOwnProperty("active")  && (msg[i].active==true) ){
                str = str + '<li class="tpl-left-nav-item"><a href="javascript:;" class="nav-link tpl-left-nav-link-list active"><i class="'+msg[i].icon +'"></i><span>' +msg[i].title + '</span><i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right tpl-left-nav-more-ico-rotate"></i></a><ul class="tpl-left-nav-sub-menu" style="display:block"><div class="menu_left_ul">';
                str = Memu_list(msg[i].system_memu,str);
            }
            else{
                str = str + '<li class="tpl-left-nav-item"><a href="javascript:;" class="nav-link tpl-left-nav-link-list"><i class="'+msg[i].icon +'"></i><span>' +msg[i].title + '</span><i class="am-icon-angle-right tpl-left-nav-more-ico am-fr am-margin-right"></i></a><ul class="tpl-left-nav-sub-menu"><div class="menu_left_ul">';
                str = Memu_list(msg[i].system_memu,str);
            }
        }else{
            if (msg[i].hasOwnProperty("active") && (msg[i].active==true) ){
                str= str + '<li class="tpl-left-nav-item"><a class="nav-link tpl-left-nav-link-list active" href="' + msg[i].url + '"><i class="'+msg[i].icon +'"></i><span>' + msg[i].title + '</span></a></li>';
            }
            else {
                str= str + '<li class="tpl-left-nav-item"><a class="nav-link tpl-left-nav-link-list" href="' + msg[i].url + '"><i class="'+msg[i].icon +'"></i><span>' + msg[i].title + '</span></a></li>';
            }
            // str= str + '<li class="tpl-left-nav-item"><a class="nav-link tpl-left-nav-link-list" href="' + msg[i].url + '"><i class="'+msg[i].icon +'"></i><span>' + msg[i].title + '</span></a></li>';
        }
    }
    str= str+'</div></ul>'
    return str
}
function escape2Html(str) {
 var arrEntities={'lt':'<','gt':'>','nbsp':' ','amp':'&','quot':'"'};
 return str.replace(/&(lt|gt|nbsp|amp|quot);/ig,function(all,t){return arrEntities[t];});
}
function show_Memu(msg) {
    instr=escape2Html(msg)
    var obj = jQuery.parseJSON(instr);
    str='';
    // str = Memu_list(obj.data.system_memu,str);
    // alert(obj);
    str = Memu_list(obj,str);
    $("div.system_memu").before(str);
}
