// console.log(0);
$( document ).ready(function() {

  var projectContainerSelector = $(".projects");
  var objectSelector = $(".objects");
  var projectSelector = $( ".project" );
  var memberSelector = $( ".member" );
  var modalSelector = $(".modal");
  var closeModalSelector = $( ".close_modal" );

  // Hide and Show project modal ***STARTS***
  var hideTime = 200;
  var offSet = 130;
  var scrollTime = 500;
  var scrollBackId = 0;

  // Navbar clicks STARTS
  // scrollToStoriesSelector.on('click', function(event) {
  //   event.preventDefault();
  //   console.log('hey');
  //   $('html, body').animate({
  //     scrollTop: $(".stories_container").offset().top
  //   }, scrollTime);
  // });
  // Navbar clicks ENDS

function getDetails(url,str){

  $.ajax({
       url: url,
       dataType: "json",
       success: function(data){
          var json = JSON.parse(data);
          populateModal(json,str);
       },
       error: function (data) {
         console.log(data);
         alert('Sorry, try again.');
       }
   });
}

// project click handling **STARTS**
function populateModal(json,str){
  var data;
  if(str=="projects"){
    data = JSON.parse(json.project)[0].fields;
    modalSelector.find('img').attr('src', "http://res.cloudinary.com/guhaar/"+data.image);
  }
  else if(str=="video"){
    data = JSON.parse(json.data)[0].fields;
    modalSelector.find('img').remove();
    modalSelector.find('div.modal_details>div:first-of-type').html(data.url);
  }
  else{
    data = JSON.parse(json.data)[0].fields;
    modalSelector.find('img').attr('src', "http://res.cloudinary.com/guhaar/"+data.image);
  }
  modalSelector.find('h2').html(data.title);
  modalSelector.find('.modal_details p').html(data.description);
}


  objectSelector.on( "click", '.object_details', function( event ) {
      event.preventDefault();
      closeModalSelector.parent().removeClass("hide");
      closeModalSelector.parent().slideDown(hideTime);
      var parentSelector = $(this).parents('.object');
      var id = parentSelector.attr('id');
      var str = parentSelector.attr('object-type');
      var url = "/"+str+"/"+id+"/";
      scrollBackId = id;
      console.log(url);
      getDetails(url,str);
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
      // var url = $(this).attr('url');
      // modalSelector.find('img').attr('src',url);
      var id = $(this).attr('id');
      $.ajax({
           url: "/aboutus/"+id+"/",
           dataType: "json",
           success: function(data){
            member = JSON.parse(data)[0].fields;
            modalSelector.find('img').attr('src', "http://res.cloudinary.com/guhaar/"+member.image);
            modalSelector.find('h2').html(member.name);
            modalSelector.find('p').html(member.short_description);
            modalSelector.find('.member_details>p').html(member.description);
           },
           error: function (data) {
             alert('unexpected Error, try again.');
           }
       });
       $('html, body').animate({
         scrollTop: $(memberSelector.parent('.team')).offset().top-offSet
       }, scrollTime);
  });
  // project click handling ** ENDS **

  closeModalSelector.on( "click", function( event ) {
      event.preventDefault();
      $(this).find('.modal').html('');
      $(this).parent().slideUp(hideTime);
      $('html, body').animate({
        scrollTop: $(".object#"+scrollBackId).offset().top
      }, scrollTime);
      // console.log('hfecd');
  });

  // $('body').not(projectSelector).on('click',function(event){
  //   event.preventDefault();
  //   closeModalSelector.trigger('click');
  // });

// Hide and Show project modal  ***ENDS***
});
