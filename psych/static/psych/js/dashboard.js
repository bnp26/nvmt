$(document).ready(function(){
    $('.modal').modal();
    $('select').formSelect();
});

function toggleModal() {
  $('#modalSubj').modal('open');
}

function toggleMedsModal() {
  $('#modalMeds').modal('open');
}

function toggleMedIssuesModal() {
  $('#modalMedIssues').modal('open');
}

function togglePsychIssuesModal() {
  $('#modalPsychIssues').modal('open');
}

function submitNewSubject(errors) {
  console.log(errors);
  $('#new_patient_form').submit();
}

function addNewMedication(csrftoken, url) {
  let name = $("#med_name").val();
  let dosage = $("#med_dosage").val();
  
  var payload = {'name': name, 'dosage': dosage};
  $.ajax({
    type: "POST",
    url: url,
    headers: {'X-CSRFToken': csrftoken},
    dataType: 'json',
    data: payload,
    success: function (data, textStatus, jqXHR) {
      console.log(data);
      console.log(textStatus);
      console.log(jqXHR);
    },
    fail: function (error) {
      console.log(error);
    }
  });
}

function addNewMedicalDiagnosis(csrftoken, url) {
  let name = $("#med_issue_name").val();
  
  var payload = {'name': name};
  $.ajax({
    type: "POST",
    url: url,
    headers: {'X-CSRFToken': csrftoken},
    dataType: 'json',
    data: payload,
    success: function (data, textStatus, jqXHR) {
      console.log(data);
      console.log(textStatus);
      console.log(jqXHR);
    },
    fail: function (error) {
      console.log(error);
    }
  });
}

function addNewPsychologicalDiagnosis(csrftoken, url) {
  let name = $("#psych_issue_name").val();
  
  var payload = {'name': name};
  $.ajax({
    type: "POST",
    url: url,
    headers: {'X-CSRFToken': csrftoken},
    dataType: 'json',
    data: payload,
    success: function (data, textStatus, jqXHR) {
      console.log(data);
      console.log(textStatus);
      console.log(jqXHR);
    },
    fail: function (error) {
      console.log(error);
  }
  });
}

function generateNewTest(url) {
  window.location.replace(url);
}