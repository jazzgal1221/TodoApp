// moment.js language configuration
// language : esperanto (eo)
// author : Colin Dean : https://github.com/colindean
// komento: Mi estas malcerta se mi korekte traktis akuzativojn en tiu traduko.
//          Se ne, bonvolu korekti kaj avizi min por ke mi povas lerni!
(function(){function e(e){e.lang("eo",{months:"januaro_februaro_marto_aprilo_majo_junio_julio_a\u016dgusto_septembro_oktobro_novembro_decembro".split("_"),monthsShort:"jan_feb_mar_apr_maj_jun_jul_a\u016dg_sep_okt_nov_dec".split("_"),weekdays:"Diman\u0109o_Lundo_Mardo_Merkredo_\u0134a\u016ddo_Vendredo_Sabato".split("_"),weekdaysShort:"Dim_Lun_Mard_Merk_\u0134a\u016d_Ven_Sab".split("_"),weekdaysMin:"Di_Lu_Ma_Me_\u0134a_Ve_Sa".split("_"),longDateFormat:{LT:"HH:mm",L:"YYYY-MM-DD",LL:"D-\\an \\de MMMM, YYYY",LLL:"D-\\an \\de MMMM, YYYY LT",LLLL:"dddd, \\l\\a D-\\an \\d\\e MMMM, YYYY LT"},meridiem:function(e,t,n){return e>11?n?"p.t.m.":"P.T.M.":n?"a.t.m.":"A.T.M."},calendar:{sameDay:"[Hodia\u016d je] LT",nextDay:"[Morga\u016d je] LT",nextWeek:"dddd [je] LT",lastDay:"[Hiera\u016d je] LT",lastWeek:"[pasinta] dddd [je] LT",sameElse:"L"},relativeTime:{future:"je %s",past:"anta\u016d %s",s:"sekundoj",m:"minuto",mm:"%d minutoj",h:"horo",hh:"%d horoj",d:"tago",dd:"%d tagoj",M:"monato",MM:"%d monatoj",y:"jaro",yy:"%d jaroj"},ordinal:"%da",week:{dow:1,doy:7}})}typeof define=="function"&&define.amd&&define(["../."],e),typeof window!="undefined"&&window.moment&&e(window.moment)})();