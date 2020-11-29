/* Image carousel */

$(function () {
  var mastHead = $("#masthead");
  var backgrounds = [
    'url("/static/img/paris.jpg")',
    'url("/static/img/bg-2.jpg")',
    'url("/static/img/bg-3.jpg")',
    'url("/static/img/bg-4.jpg")',
    'url("/static/img/bg-5.jpg")',
  ];
  var current = 0;

  function nextBackground() {
    mastHead.css(
      "background-image",
      backgrounds[(current = ++current % backgrounds.length)]
    );

    setTimeout(nextBackground, 6000);
  }
  setTimeout(nextBackground, 5000);
  mastHead.css("background-image", backgrounds[0]);
});
