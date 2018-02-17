// console.log(0);
$( document ).ready(function() {

  var projectContainerSelector = $(".projects");
  var objectSelector = $(".objects");
  var projectSelector = $( ".project" );
  var memberSelector = $( ".member" );
  var modalSelector = $(".modal");
  var closeModalSelector = $( ".close_modal" );
  // var closedDonation = false;

  // Hide and Show project modal ***STARTS***
  var hideTime = 200; // used for animating effect
  var offSet = 130; // offset from the top if the body: USED WHILE SCROLLING THE HTML BODY
  var scrollTime = 900;
  var scrollBackId = 0; // Keeping track of where was user when click was triggered to get the user back to the same location on the page

  var fetchedObjects = {}; // To keep track of which item is fetched and which is not in order to minimize the Ajax calls

function getAjaxResults(url,str,id){

  $.ajax({
       url: url,
       dataType: "json",

       success: function(data){
          var json = JSON.parse(data);
          console.log('ajax called!');
          populateModal(str,json);
          fetchedObjects[id]= json;
       },

       error: function (data) {
         console.log(data);
         alert('Sorry, try again.');
       }

   });

}

// project click handling **STARTS**

function insertDataInDom(parentSelector, htmlData){
  // populate the particular dom elements
  parentSelector.find('div.modal_details>div:first-of-type').html('');
  parentSelector.find('div.modal_details>div:first-of-type').html(htmlData);

}

function populateModal(str,json){
  var data;

  if(str=="members"){
     // If User clicked the team members' images
      src = "http://res.cloudinary.com/guhaar/"+json.image;
      name =  json.name;
      short_description = json.short_description;
      description = json.description;
      str = '<img class= "member_thumb" src='+src+' alt="member thumbnail"><h2>'+name+'</h2><p>'+short_description+'</p>';

      insertDataInDom(modalSelector, str);
      modalSelector.find('.member_details p').html(json.description);

  }else {

      if(str=="projects"){
          data = JSON.parse(json.project)[0].fields;
          src = "http://res.cloudinary.com/guhaar/" + data.image;
          alt = data.title;
          insertDataInDom(modalSelector,'<img src=' + src + ' alt=' + alt +'>');
      }else{
          data = JSON.parse(json.data)[0].fields;

          if(data.url){
            insertDataInDom(modalSelector, data.url);
          }
          else{
            src = "http://res.cloudinary.com/guhaar/" + data.image;
            alt = data.title;
            insertDataInDom(modalSelector,'<img src=' + src + ' alt =' + alt + '>');
          }
      }
      modalSelector.find('h2').html(data.title);
      modalSelector.find('.modal_details p').html(data.description);
  }
}

objectSelector.on( "click", '.object_details', function( event ) {
      // event.preventDefault();
      closeModalSelector.parent().removeClass("hide");
      closeModalSelector.parent().slideDown(hideTime);

      var parentSelector = $(this).parents('.object');
      var id = parentSelector.attr('id');
      var str = parentSelector.attr('object-type'); // assign the item type i.e. Project, Video or interview
      var url = "/"+str+"/"+id+"/";

      scrollBackId = id;
      // console.log(url);
      if(fetchedObjects[id]){
        // to check is this item has been fetched before
        console.log('ajax not called');
        populateModal(str,fetchedObjects[id]);
      } else {
        // If not then make ajax call
        getAjaxResults(url,str,id);
      }

      $('html, body').animate({
        scrollTop: $(parentSelector.parents('.objects')).offset().top-offSet
      }, scrollTime);

  });
  // project click handling ** ENDS **

  // member click handling ** STARTS **
memberSelector.on( "click", function( event ) {
      event.preventDefault();
      closeModalSelector.parent().removeClass("hide");
      closeModalSelector.parent().slideDown(hideTime);

      var id = $(this).attr('id');
      scrollBackId = id;
      if(fetchedObjects[id]){
        // to check is this item has been fetched before
        console.log('ajax not called', fetchedObjects[id]);
        populateModal("members",fetchedObjects[id]);

      } else {
        // If not then make ajax call
          $.ajax({
               url: "/aboutus/"+id+"/",
               dataType: "json",

               success: function(data){
                  member = JSON.parse(data)[0].fields;
                  fetchedObjects[id] = member;
                  populateModal("members",fetchedObjects[id]);
               },

               error: function (data) {
                 alert('unexpected Error, try again.');
               }
           });
         }

       $('html, body').animate({
         scrollTop: $(memberSelector.parent('.team')).offset().top-offSet
       }, scrollTime);
  });
  // project click handling ** ENDS **
  closeModalSelector.on( "click", function( event ) {
      event.preventDefault();
      $(this).parents('.banner').slideUp(hideTime);
      closedDonation = true;
      insertDataInDom(modalSelector, '<img src="" alt="">');
      modalSelector.find('h2').html('');
      modalSelector.find('.modal_details p').html('');
      // console.log(".object#"+scrollBackId);

      $('html, body').animate({
        scrollTop: $(".object#"+scrollBackId).offset().top-offSet
      }, scrollTime);

  });
// Hide and Show project modal  ***ENDS***
  setTimeout(function() {
      $("#donation-banner").slideDown(hideTime);
      setTimeout(function() {
          $("#donation-banner").slideUp(hideTime);
      }, 20000);
  }, 4000);

// Functionality For subscribers'
function subscribeMe(email){
  // Sends a post request to create a subscriber
  $.ajax({
       url: '/create-subscriber/',
       type: 'post',
       data:{
         'email':email,
         'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
       },
       dataType: "json",
       success: function(data){
          var json = JSON.parse(data);
          // console.log('ajax called!', json.saved);
          if(json.saved){
            // if subscriber is created successfully
            $.notify("Thank you! Your email has been added successfully.", "success");
          }else {
            // if subscriber already exist
            $.notify("Your email already exists in our server.", "info");
          }
       },

       error: function (data) {
         console.log(data);
         alert('Sorry, try again.');
       }

   });

}

// Email subscription ******STARTS*******
function isValidEmailAddress(emailAddress) {
    var pattern = /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i;
    return pattern.test(emailAddress);
}

$('#subscribe-me').on( "click", function( event ) {
    event.preventDefault();
    // After subscribeMe is clicked
    email = $('#email').val();
    if(isValidEmailAddress(email)){
      $('#email').val('');
      subscribeMe(email);
    }else{
      $.notify("Email you have entered is incorrect!", "error");
    }
});
// Email subscription ******ENDS*******


});
