// Common URL to API challenge
var url = 'http://challenge.code2040.org';

/**
 * This function grabs the token from the 
 * API and returns it to the user.
 */
function getToken(data) {
  var tok;

  // Request a POST to the API
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

/**
 * This function gets the data from the API
 * server. The path and token must be provided.
 * The function returns the data in a result
 * object. 
 */
function getData(path, token) {
  var result;

  // Send POST request to API
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

/**
 * This function sends back data to the API
 * Challenge server. Path, token, and data must
 * be provided. Returns true if the API accepted
 * the solution, false otherwise.
 */
function sendData(path, token, data) {
  data['token'] = token;

  var status;

  // Again send POST request.
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


/**
 * This function reverses a string.
 */
function stageI(str) {
  return str.split('').reverse().join('');
};

/**
 * This function finds the index of needle in the
 * haystack array.
 */
function stageII(needle, haystack) {
  return haystack.indexOf(needle);
}

/**
 * This function returns all the strings in the
 * strings array that do not begein with the
 * prefix
 */
function stageIII(prefix, strings) {
  return strings.filter(function(el) {
    if(el.substring(0, prefix.length) != prefix)
      return el;
  });
};

/**
 * This function adds the interval to the date
 * and returns it back in the same ISO format.
 */
function stageIV(interval, date) {
  var newDate = new Date(date);
  newDate.setSeconds(newDate.getSeconds() + interval);
  return newDate.toISOString();
};