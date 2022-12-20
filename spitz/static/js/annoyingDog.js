var annoyingDog = $('.annoying-dog');
var annoyingDogAudio = $('body').find('audio')[0];

annoyingDog.hover(function(){
  annoyingDogAudio.play();
  $('.pet-me').hide();
  $('.pet-me2').show();
  $('.pet-me3').hide();
  $('.pet-me4').show();
}, function(){
  annoyingDogAudio.pause();
  $('.pet-me').show();
  $('.pet-me2').hide();
  $('.pet-me3').show();
  $('.pet-me4').hide();
});