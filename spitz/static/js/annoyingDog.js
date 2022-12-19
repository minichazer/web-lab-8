var annoyingDog = $('.annoying-dog');
var annoyingDogAudio = $('body').find('audio')[0];

annoyingDog.hover(function(){
  annoyingDogAudio.play();
  $('.pet-me').hide();
  $('.pet-me2').show();
}, function(){
  annoyingDogAudio.pause();
  $('.pet-me').show();
  $('.pet-me2').hide();
});