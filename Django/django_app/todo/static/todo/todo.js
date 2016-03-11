$(document).ready(function(){

 /*
 To-Do List animation when completing tasks.
 */
  $(".list-group-item").click(function(){
    $(this).children(".todo-text").css("text-decoration" , "line-through");
  });


});
