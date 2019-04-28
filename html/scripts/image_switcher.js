// Image switcher code

var myImage = document.querySelector('img');

myImage.onclick = function() {
  var mySrc = myImage.getAttribute('src');
  if(mySrc === 'images/Beiersdorf-New-Headquarters.png') {
    myImage.setAttribute ('src','images/BDF_Logo.png');
  } else {
    myImage.setAttribute ('src','images/Beiersdorf-New-Headquarters.png');
  }
}