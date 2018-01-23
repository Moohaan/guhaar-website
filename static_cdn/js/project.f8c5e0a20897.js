// console.log(0);
$( document ).ready(function() {
  // console.log(0);
  var projectSelector = $( ".project" );
  var memberSelector = $( ".member" );
  var modalSelector = $(".modal");
  var closeModalSelector = $( ".close_modal" );

  // Hide and Show project modal ***STARTS***
  var hideTime = 200;

// project click handling **STARTS**
  projectSelector.on( "click", function( event ) {
      event.preventDefault();
      closeModalSelector.parent().removeClass("hide");
      closeModalSelector.parent().slideDown(hideTime);
      var id = $(this).attr('id');
      $.ajax({
           url: "/projects/"+id+"/",
           dataType: "json",
           success: function(data){
            //  alert('worked!!');
              var json = JSON.parse(data);
              project = JSON.parse(json.project)[0].fields;
              var noOfVideos = JSON.parse(json.videos).length;
              console.log(noOfVideos, JSON.parse(json.videos));
              console.log(json);
              if(noOfVideos>0){
                // var html = '<p>Related to this project</p>';
                var html = '';
                for(var i =0; i<noOfVideos; i++){
                  // stories = JSON.parse(json.stories)[0].fields;
                  // interviews = JSON.parse(json.interviews)[0].fields;
                  videos = JSON.parse(json.videos)[i].fields;
                  html+='<iframe id="player" type="text/html" width="300px" height="220px" src="'+videos.video_youtube_url+'" frameborder="0"></iframe>';
                }
                modalSelector.find('.project_related_content').append(html);
              }
              modalSelector.find('img').attr('src','/media/'+ project.project_img);
              modalSelector.find('h2').html(project.project_title);
              modalSelector.find('.project_details>p').html(project.project_description);
           },
           error: function (data) {
             console.log(data);
             alert('Sorry, try again.');
           }
       });
      $('body').addClass('stop-scrolling');
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
             console.log(data);
             alert('Sorry, try again.');
           }
       });
      // console.log(pk);
      // $(document).scroll().disable();
  });
  // project click handling ** ENDS **

  closeModalSelector.on( "click", function( event ) {
      event.preventDefault();
      modalSelector.find('.project_related_content').html('');
      $(this).parent().slideUp(hideTime);
      // console.log('hfecd');
  });

// Hide and Show project modal  ***ENDS***
});
