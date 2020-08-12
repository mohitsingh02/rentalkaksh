function fn1()
{
    var mob = document.getElementById("mob").value;
    var nam = document.getElementById("nam").value;

    var namch = /^[A-Za-z]{3,30}+([\A-Za-z]+)*/;
    var regx = /^[6-9]\d{9}$/;

    if(namch.test(nam))
    {
        document.getElementById("nam").style.border = "solid 1px green";
    }
    else{
        document.getElementById("nam").style.border = "solid 1px red";
        return false;
    }


    if(regx.test(mob))
    {
        document.getElementById("mob").style.border = "solid 1px green";
    }
    else{
        document.getElementById("mob").style.border = "solid 1px red";
        return false;
    }


}
