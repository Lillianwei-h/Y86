$(function(){
    // 建立变量，分配各数据在html中对应的位置，“#”代表ID，已经在html中设置了每个值的ID
    var $pc=$('#pc');
    var $zf=$('#zf');
    var $sf=$('#sf');
    var $of=$('#of');
    var $rax=$('#rax');
    var $rcx=$('#rcx');
    var $rdx=$('#rdx');
    var $rbx=$('#rbx');
    var $rsp=$('#rsp');
    var $rbp=$('#rbp');
    var $rsi=$('#rsi');
    var $rdi=$('#rdi');
    var $r8=$('#r8');
    var $r9=$('#r9');
    var $r10=$('#r10');
    var $r11=$('#r11');
    var $r12=$('#r12');
    var $r13=$('#r13');
    var $r14=$('#r14');
    var $stat=$('#stat');
    var $mem=$('.mem');
    var pause=700;  // 每次数据变化的时间间隔，单位ms
    $.ajax({
        // ajax为jquery库中的一个工具，可以用来直接改变网页上显示的数据而不用刷新网页
        type:'GET',
        url:'answer.json',  // 读取json文件位置
        dataType:"json",
        success:function(datas){    // datas为读取到的json的整个列表
            // console.log(datas);
            function startcpu(){    // cpu开始运行函数
                var i=0;
                interval=setInterval(function(){    // setInterva可以控制每次运行的时间间隔
                    if(datas[i].CC.ZF==false){      // 由于数据为false时前端不输出，则提前改为字符串
                        datas[i].CC.ZF="false";
                    }
                    if(datas[i].CC.SF==false){
                        datas[i].CC.SF="false";
                    }
                    if(datas[i].CC.OF==false){
                        datas[i].CC.OF="false";
                    }
                    $mem.empty();   // 内存同样每次都初始化
                    if(i===0){
                        //第一个循环时，所有其余数据都初始化为空，
                        //这样可以确保再次按下开始按钮时，上次运行的数据会被清空
                        $pc.empty();
                        $zf.empty();
                        $sf.empty();
                        $of.empty();
                        $rax.empty();
                        $rcx.empty();
                        $rdx.empty();
                        $rbx.empty();
                        $rsp.empty();
                        $rbp.empty();
                        $rsi.empty();
                        $rdi.empty();
                        $r8.empty();
                        $r9.empty();
                        $r10.empty();
                        $r11.empty();
                        $r12.empty();
                        $r13.empty();
                        $r14.empty();
                        $stat.empty();
                        // 根据数据内容判断是否“要改变外观”，即如果ZF是true，SF、OF是false，
                        // STAT是SAOK，寄存器是0，就不需要改变外观
                        $pc.addClass('change');
                        if(datas[i].CC.ZF!=true) $zf.addClass('change');
                        if(datas[i].CC.SF!="false") $sf.addClass('change');
                        if(datas[i].CC.OF!="false") $of.addClass('change');
                        if(datas[i].STAT!="SAOK") $stat.addClass('change');
                        if(datas[i].Register.RAX!=0) $rax.addClass('change');
                        if(datas[i].Register.RCX!=0) $rcx.addClass('change');
                        if(datas[i].Register.RDX!=0) $rdx.addClass('change');
                        if(datas[i].Register.RBX!=0) $rbx.addClass('change');
                        if(datas[i].Register.RSP!=0) $rsp.addClass('change');
                        if(datas[i].Register.RBP!=0) $rbp.addClass('change');
                        if(datas[i].Register.RSI!=0) $rsi.addClass('change');
                        if(datas[i].Register.RDI!=0) $rdi.addClass('change');
                        if(datas[i].Register.R8!=0) $r8.addClass('change');
                        if(datas[i].Register.R9!=0) $r9.addClass('change');
                        if(datas[i].Register.R10!=0) $r10.addClass('change');
                        if(datas[i].Register.R11!=0) $r11.addClass('change');
                        if(datas[i].Register.R12!=0) $r12.addClass('change');
                        if(datas[i].Register.R13!=0) $r13.addClass('change');
                        if(datas[i].Register.R14!=0) $r14.addClass('change');
                        // 上传各数据
                        $pc.append(datas[i].PC);
                        $zf.append(datas[i].CC.ZF);
                        $sf.append(datas[i].CC.SF);
                        $of.append(datas[i].CC.OF);
                        $rax.append(datas[i].Register.RAX);
                        $rcx.append(datas[i].Register.RCX);
                        $rdx.append(datas[i].Register.RDX);
                        $rbx.append(datas[i].Register.RBX);
                        $rsp.append(datas[i].Register.RSP);
                        $rbp.append(datas[i].Register.RBP);
                        $rsi.append(datas[i].Register.RSI);
                        $rdi.append(datas[i].Register.RDI);
                        $r8.append(datas[i].Register.R8);
                        $r9.append(datas[i].Register.R9);
                        $r10.append(datas[i].Register.R10);
                        $r11.append(datas[i].Register.R11);
                        $r12.append(datas[i].Register.R12);
                        $r13.append(datas[i].Register.R13);
                        $r14.append(datas[i].Register.R14);
                        $stat.append(datas[i].STAT);
                    }
                    else{
                        // 除内存外的数据都有数据改变时外观改变的功能
                        // 非第一次循环时，与前一次循环中数据比较，若不相同就“要改变外观”，同时上传新数据
                        // 若相同就去除“要改变外观”这个类，即可以消除显示效果
                        if(datas[i].PC!=datas[i-1].PC){
                            $pc.empty();
                            $pc.addClass('change');
                            $pc.append(datas[i].PC);    // 上传pc数据
                        }
                        else{
                            $pc.removeClass('change');
                        }
                        if(datas[i].CC.ZF!=datas[i-1].CC.ZF){
                            $zf.empty();
                            $zf.addClass('change');
                            $zf.append(datas[i].CC.ZF);
                        }
                        else{
                            $zf.removeClass('change');
                        }
                        if(datas[i].CC.SF!=datas[i-1].CC.SF){
                            $sf.empty();
                            $sf.addClass('change');
                            $sf.append('<strong>'+datas[i].CC.SF);
                        }
                        else{
                            $sf.removeClass('change');
                        }
                        if(datas[i].CC.OF!=datas[i-1].CC.OF){
                            $of.empty();
                            $of.addClass('change');
                            $of.append(datas[i].CC.OF);
                        }
                        else{
                            $of.removeClass('change');
                        }
                        if(datas[i].Register.RAX!=datas[i-1].Register.RAX){
                            $rax.empty();
                            $rax.addClass('change');
                            $rax.append(datas[i].Register.RAX);
                        }
                        else{
                            $rax.removeClass('change');
                        }
                        if(datas[i].Register.RCX!=datas[i-1].Register.RCX){
                            $rcx.empty();
                            $rcx.addClass('change');
                            $rcx.append(datas[i].Register.RCX);
                        }
                        else{
                            $rcx.removeClass('change');
                        }
                        if(datas[i].Register.RDX!=datas[i-1].Register.RDX){
                            $rdx.empty();
                            $rdx.addClass('change');
                            $rdx.append(datas[i].Register.RDX);
                        }
                        else{
                            $rdx.removeClass('change');
                        }
                        if(datas[i].Register.RBX!=datas[i-1].Register.RBX){
                            $rbx.empty();
                            $rbx.addClass('change');
                            $rbx.append(datas[i].Register.RBX);
                        }
                        else{
                            $rbx.removeClass('change');
                        }
                        if(datas[i].Register.RSP!=datas[i-1].Register.RSP){
                            $rsp.empty();
                            $rsp.addClass('change');
                            $rsp.append(datas[i].Register.RSP);
                        }
                        else{
                            $rsp.removeClass('change');
                        }
                        if(datas[i].Register.RBP!=datas[i-1].Register.RBP){
                            $rbp.empty();
                            $rbp.addClass('change');
                            $rbp.append(datas[i].Register.RBP);
                        }
                        else{
                            $rbp.removeClass('change');
                        }
                        if(datas[i].Register.RSI!=datas[i-1].Register.RSI){
                            $rsi.empty();
                            $rsi.addClass('change');
                            $rsi.append(datas[i].Register.RSI);
                        }
                        else{
                            $rsi.removeClass('change');
                        }
                        if(datas[i].Register.RDI!=datas[i-1].Register.RDI){
                            $rdi.empty();
                            $rdi.addClass('change');
                            $rdi.append(datas[i].Register.RDI);
                        }
                        else{
                            $rdi.removeClass('change');
                        }
                        if(datas[i].Register.R8!=datas[i-1].Register.R8){
                            $r8.empty();
                            $r8.addClass('change');
                            $r8.append(datas[i].Register.R8);
                        }
                        else{
                            $r8.removeClass('change');
                        }
                        if(datas[i].Register.R9!=datas[i-1].Register.R9){
                            $r9.empty();
                            $r9.addClass('change');
                            $r9.append(datas[i].Register.R9);
                        }
                        else{
                            $r9.removeClass('change');
                        }
                        if(datas[i].Register.R10!=datas[i-1].Register.R10){
                            $r10.empty();
                            $r10.addClass('change');
                            $r10.append(datas[i].Register.R10);
                        }
                        else{
                            $r10.removeClass('change');
                        }
                        if(datas[i].Register.R11!=datas[i-1].Register.R11){
                            $r11.empty();
                            $r11.addClass('change');
                            $r11.append(datas[i].Register.R11);
                        }
                        else{
                            $r11.removeClass('change');
                        }
                        if(datas[i].Register.R12!=datas[i-1].Register.R12){
                            $r12.empty();
                            $r12.addClass('change');
                            $r12.append(datas[i].Register.R12);
                        }
                        else{
                            $r12.removeClass('change');
                        }
                        if(datas[i].Register.R13!=datas[i-1].Register.R13){
                            $r13.empty();
                            $r13.addClass('change');
                            $r13.append(datas[i].Register.R13);
                        }
                        else{
                            $r13.removeClass('change');
                        }
                        if(datas[i].Register.R14!=datas[i-1].Register.R14){
                            $r14.empty();
                            $r14.addClass('change');
                            $r14.append(datas[i].Register.R14);
                        }
                        else{
                            $r14.removeClass('change');
                        }
                        if(datas[i].STAT!=datas[i-1].STAT){
                            $stat.empty();
                            $stat.addClass('change');
                            $stat.append(datas[i].STAT);
                        }
                        else{
                            $stat.removeClass('change');
                        }
                    }
                    // 上传内存数据
                    for(var j in datas[i].Memory){
                        $mem.append('<li>'+j+' : '+datas[i].Memory[j]+'</li>');
                    }
                    i++;
                    // 当循环次数等于列表长度，停止
                    if(i>=datas.length) clearInterval(interval);
                },pause);
            }
            // 设置单击标题栏为开始cpu
            $('#start').on('click',function(){
                startcpu();
            });
        }
    });
});