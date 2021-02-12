let endpoint = "http://api.scraperapi.com?api_key=[key]&url=https://am-i-eligible.covid19vaccine.health.ny.gov/api/list-providers";

let interesting = ["Jones Beach - Field 3", "SUNY Stony Brook University Innovation and Discovery Center", "Aqueduct Racetrack - Racing Hall"];

let apikey = "[sendgrid key]";

let mail_from = "foo@bar.com";
let mail_to = ["blah@gmail.com", "5555555555@txt.att.net"];

function get_apts_avail() {
  let response = UrlFetchApp.fetch(endpoint, {'muteHttpExceptions':true});
  // Logger.log(response.getContentText());
  // Logger.log(response.getAllHeaders());
  let all_places = JSON.parse(response.getContentText()).providerList;
  let places_with_appt = all_places.filter(place=>place.availableAppointments === "AA").map(place=>place.providerName);
  return places_with_appt;
}

function run_checker() {
  let places_with_appt = get_apts_avail();
  var scriptProperties = PropertiesService.getScriptProperties();
  Logger.log("Places with appointment:");
  Logger.log(places_with_appt);
  interesting.forEach(interested => {
    if (places_with_appt.some(place=>place === interested)){
      Logger.log(interested + " Has an appointment");
      if(scriptProperties.getProperty(interested) !== "1") {
        Logger.log("Sending email for "+ interested);
        let auth = "Bearer " + apikey;
        let body = {
            "personalizations": [{"to": mail_to.map(email=>({"email": email}))}],
            "from": {"email": mail_from},
            "subject": "Vaccine availablility update",
            "content": [{"type": "text/plain", "value": interested + " Has an appointment available"}]
        }
        UrlFetchApp.fetch("https://api.sendgrid.com/v3/mail/send", {
          "method": "POST",
          "headers":
          {
            "Authorization": auth,
            "Content-Type": "application/json"
          },
          "payload": JSON.stringify(body)
        });
        scriptProperties.setProperty(interested, "1");
      }
    } else{
      if(scriptProperties.getProperty(interested) !== null){
        Logger.log(interested + " is no longer available");
        scriptProperties.deleteProperty(interested);
      }
    }
  })
}

function resetProperties() {
  var scriptProperties = PropertiesService.getScriptProperties();
  scriptProperties.deleteAllProperties();
}