$(document).ready(function(){
    $('.modal').modal();
    $('select').material_select();
  });
  
  function toggleModal() {
    $('#modal1').modal('open');
  }
  
  function toggleMedsModal() {
    $('#meds_modal').modal('open');
  }
  
  function submitNewSubject(errors) {
    console.log(errors);
    $('#new_patient_form').submit();
  }
  
  function addNewMedication(csrftoken) {
    let name = $("#med_name").val();
    let dosage = $("#med_dosage").val();
    
    var payload = { med : {'name' : name, 'dosage' : dosage} };
    $.ajaxSetup({
      url: "/psych_app/dashboard/new_med",
      headers: {'X-CSRFToken': csrftoken},
      dataType: 'json',
      success: function (data, textStatus, jqXHR) {
        console.log(data);
        console.log(textStatus);
        console.log(jqXHR);
      }
    });
    var request = $.ajax({
      data: payload,
    }).success(function(response) {
      console.log(response);
    }).fail(function (error) {
        console.log(error);
    });
  }
  