// Use this file in Google Sheet Script to receive webhook alert from Aruba Central

function doPost(e) {
  if (e == null || e.postData == null || e.postData.contents == null) {
    return;
  }
  //  var requestJSON = e.postData.contents;

  // Parse json

  var params = JSON.parse(e.postData.contents);

  // Set Spread Sheet

  var ss = SpreadsheetApp.getActive();
  var sheet = ss.getActiveSheet();

  // Get headers from Spread Sheet
  var headers = sheet.getRange(1,1,1,sheet.getLastColumn()).getValues()[0];

  // Get value for each headers
  var values = [];
  
  for (i in headers){
    var header = headers[i];
    if (header == "time"){
      val = params["details"]["time"];
    }else{
      val = params[header];
    }
    values.push(val);
  }

  // Add line
  sheet.appendRow(values);
}
