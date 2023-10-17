function showTime() {
  var bdate = 29;
  var bmonth = 10;
  var byear = 2001;
  today = new Date();
  var year = today.getFullYear();
  var month = today.getMonth() + 1;

  var date = today.getDate();
  var todayyear = Number.parseFloat(year);
  var todaymonth = Number.parseFloat(month);
  var todays = Number.parseFloat(date);
  var thr = Number.parseFloat(today.getHours());
  var tmin = Number.parseFloat(today.getMinutes());
  console.log(todays);

  if (todays < bdate) {
    days = todays - bdate + 30;
    todaymonth = todaymonth - 1;
  } else {
    days = todays - bdate;
  }

  if (todaymonth < bmonth) {
    months = todaymonth - bmonth + 12;
    todayyear = todayyear - 1;
  } else {
    months = todaymonth - bmonth;
  }
  if (thr + 6 > 24) {
    var hr = thr + 6 - 24;
  } else {
    var hr = thr + 6;
  }
  if (tmin + 10 > 60) {
    var min = tmin + 10 - 60;
  } else {
    var min = tmin + 10;
  }
  age = todayyear - byear;
  var Time =
    age +
    " : " +
    months +
    " : " +
    days +
    " : " +
    hr +
    " : " +
    min +
    " : " +
    today.getSeconds() +
    " : " +
    today.getMilliseconds();
  document.getElementById("age").innerHTML = "My Age at the moment :- " + Time;
}
setInterval(showTime, 1);
