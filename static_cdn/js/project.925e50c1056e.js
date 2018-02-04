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

function insertDataInDom(parentSelector, htmlData){
  parentSelector.find('div.modal_details>div:first-of-type').html('');
  parentSelector.find('div.modal_details>div:first-of-type').html(htmlData);
}

function populateModal(json,str){
  var data;
  if(str=="projects"){
    data = JSON.parse(json.project)[0].fields;
    src = "http://res.cloudinary.com/guhaar/"+data.image;
    alt = data.title;
    insertDataInDom(modalSelector,'<img src='+src+' alt='+alt+'>');
  }
  else{
    data = JSON.parse(json.data)[0].fields;
    if(data.url){
      insertDataInDom(modalSelector, data.url);
    }else{
      src = "http://res.cloudinary.com/guhaar/"+data.image;
      alt = data.title;
      insertDataInDom(modalSelector,'<img src='+src+' alt='+alt+'>');
    }
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
      var id = $(this).attr('id');
      scrollBackId = id;
      $.ajax({
           url: "/aboutus/"+id+"/",
           dataType: "json",
           success: function(data){
            member = JSON.parse(data)[0].fields;
            src = "http://res.cloudinary.com/guhaar/"+member.image;
            name =  member.name;
            short_description = member.short_description;
            description = member.description;
            str = '<img src='+src+' alt="member thumbnail"><h2>'+name+'</h2><p>'+short_description+'</p>';
            insertDataInDom(modalSelector, str);
            modalSelector.find('.member_details p').html(member.description);
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
      $(this).parent().slideUp(hideTime);
      insertDataInDom(modalSelector, '<img src="" alt="">');
      modalSelector.find('h2').html('');
      modalSelector.find('.modal_details p').html('');
      console.log(".object#"+scrollBackId);
      $('html, body').animate({
        scrollTop: $(".object#"+scrollBackId).offset().top
      }, scrollTime);
  });

// Hide and Show project modal  ***ENDS***
});
