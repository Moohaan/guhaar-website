// console.log(0);
$( document ).ready(function() {
  // console.log(0);
  // var scrollToStoriesSelector = $(".scroll_story");
  // var storiesSectionSelector = $(".stories_container");
  var projectContainerSelector = $(".projects");
  var projectSelector = $( ".project" );
  var memberSelector = $( ".member" );
  var modalSelector = $(".modal");
  var closeModalSelector = $( ".close_modal" );

  // Hide and Show project modal ***STARTS***
  var hideTime = 200;
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



// project click handling **STARTS**
  projectSelector.on( "click", '.project_details', function( event ) {
      event.preventDefault();
      closeModalSelector.parent().removeClass("hide");
      closeModalSelector.parent().slideDown(hideTime);
      var id = $(this).parents('.project').attr('id');
      scrollBackId = id;
      $.ajax({
           url: "/projects/"+id+"/",
           dataType: "json",
           success: function(data){
            //  alert('worked!!');
              var json = JSON.parse(data);
              project = JSON.parse(json.project)[0].fields;
              // var noOfVideos = JSON.parse(json.videos).length;
              // console.log(noOfVideos, JSON.parse(json.videos));
              console.log(json);
              // if(noOfVideos>0){
              //   // var html = '<p>Related to this project</p>';
              //   var html = '';
              //   /*for(var i =0; i<noOfVideos; i++){
              //     // stories = JSON.parse(json.stories)[0].fields;
              //     // interviews = JSON.parse(json.interviews)[0].fields;
              //     videos = JSON.parse(json.videos)[i].fields;
              //     html+='<iframe id="player" type="text/html" width="300px" height="220px" src="'+videos.url+'" frameborder="0"></iframe>';
              //   }*/
              //   modalSelector.find('.project_related_content').append(html);
              // }
              modalSelector.find('img').attr('src', project.image.url);
              modalSelector.find('h2').html(project.title);
              modalSelector.find('.modal_details p').html(project.description);
           },
           error: function (data) {
             console.log(data);
             alert('Sorry, try again.');
           }
       });
      $('body').addClass('stop-scrolling');
      $('html, body').animate({
        scrollTop: $(projectSelector.parent('.projects')).offset().top-120
      }, scrollTime);
  });
  // project click handling ** ENDS **

  // member click handling ** STARTS **
  memberSelector.on( "click", function( event ) {
      event.preventDefault();
      closeModalSelector.parent().removeClass("hide");
      closeModalSelector.parent().slideDown(hideTime);
      var url = $(this).attr('url');
      modalSelector.find('img').attr('src',url);
      var id = $(this).attr('id');
      $.ajax({
           url: "/aboutus/"+id+"/",
           dataType: "json",
           success: function(data){
            //  alert('worked!!');
            member = JSON.parse(data)[0].fields;
            modalSelector.find('h2').html(member.name);
            modalSelector.find('p').html(member.short_description);
            modalSelector.find('.member_details>p').html(member.description);
            console.log(member);
           },
           error: function (data) {
            //  console.log(data);
             alert('Sorry, try again.');
           }
       });
       $('html, body').animate({
         scrollTop: $(memberSelector.parent('.team')).offset().top-120
       }, scrollTime);
      // console.log(pk);
      // $(document).scroll().disable();
  });
  // project click handling ** ENDS **

  closeModalSelector.on( "click", function( event ) {
      event.preventDefault();
      modalSelector.find('.project_related_content').html('');
      $(this).parent().slideUp(hideTime);
      $('html, body').animate({
        scrollTop: $(".project#"+scrollBackId).offset().top
      }, scrollTime);
      // console.log('hfecd');
  });

  // $('body').not(projectSelector).on('click',function(event){
  //   event.preventDefault();
  //   closeModalSelector.trigger('click');
  // });

// Hide and Show project modal  ***ENDS***
});
