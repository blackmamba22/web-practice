$(document).ready(function(){

 /*
 To-Do List animation when completing tasks.
 */
  $("a.chkbx").click(function(){
    $(this).parent().parent().siblings().children("span.todo-text").css("text-decoration" , "line-through");

    // submits checkbox form to mark item as completed.
    $(this).parent().submit();

  }); // end of click




});// end of main script
