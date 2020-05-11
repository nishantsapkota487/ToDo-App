$(document).ready(function(){
  var button, userValue;
  button = document.getElementById('add')
  button.addEventListener('click',function(){
    userValue = document.getElementById('form').value
    console.log(userValue);
    $.ajax({
      type:'GET',
      url:'/check/',
      data:{
        'user_value':userValue
      },
      type:'GET',
      success:function(response){
        alert(response.message)
      }
    })
  })
})
