$(document).ready(function(){

 /*
 To-Do List animation when completing tasks.
 */
  $("a.chkbx").click(function(){
    $(this).parent().siblings().children("span.todo-text").css("text-decoration" , "line-through");

    // onclick mark item as completed and update database is_complete attribute
    // for that model.
   /*var modelID = $(this).attr("id");
    $.post( window.location.href + "complete/",
            { 'model' : modelID },
            function(){
            $(this).parent().css("background-color", "lightblue");
    });// end of post request*/

  }); // end of click




});// end of main script
