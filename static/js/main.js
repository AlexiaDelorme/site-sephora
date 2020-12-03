/* Image carousel */

$(function () {
  var mastHead = $("#masthead");
  var backgrounds = [
    'url("https://site-sephora.s3.eu-west-3.amazonaws.com/img/paris.jpg")',
    'url("https://site-sephora.s3.eu-west-3.amazonaws.com/img/bg-2.jpg")',
    'url("https://site-sephora.s3.eu-west-3.amazonaws.com/img/bg-3.jpg")',
    'url("https://site-sephora.s3.eu-west-3.amazonaws.com/img/bg-4.jpg")',
    'url("https://site-sephora.s3.eu-west-3.amazonaws.com/img/bg-5.jpg")',
  ];
  var current = 0;

  function nextBackground() {
    mastHead.css(
      "background-image",
      backgrounds[(current = ++current % backgrounds.length)]
    );

    setTimeout(nextBackground, 5700);
  }
  setTimeout(nextBackground, 5000);
  mastHead.css("background-image", backgrounds[0]);
});
