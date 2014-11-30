var url = 'http://challenge.code2040.org';

function getToken(data) {
  var tok;

  $.ajax({
    type: 'POST',
    url: url + '/api/register',
    async: false,
    data: JSON.stringify(data),
    dataType: 'json'
  })
  .done(function (token){
    tok = token.result;
  });

  return tok;
};

function getData(path, token) {
  var result;

  $.ajax({
    type: 'POST',
    url: url + path,
    async: false,
    data: JSON.stringify({'token':token}),
    dataType: 'json'
  })
  .done(function (data) {
    result = data;
  });

  return result;
};

function sendData(path, token, data) {
  data['token'] = token;

  var status;
  $.ajax({
    type: 'POST',
    url: url + path,
    async: false,
    data: JSON.stringify(data),
    dataType: 'json'
  })
  .done(function (data){
    if(data.result.indexOf('PASS') > -1) {
      status = true;
    }
    else {
      status = false;
    }
  });

  return status;
};

function stageI(str) {
  return str.split('').reverse().join('');
};

function stageII(needle, haystack) {
  return haystack.indexOf(needle);
}

function stageIII(prefix, strings) {
  return strings.filter(function(el) {
    if(el.substring(0, prefix.length) != prefix)
      return el;
  });
};

function stageIV(interval, date) {
  var newDate = new Date(date);
  newDate.setSeconds(newDate.getSeconds() + interval);
  return newDate.toISOString();
};