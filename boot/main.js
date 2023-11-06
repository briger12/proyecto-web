let app = document.getElementById('typewriter');
 
let typewriter = new Typewriter(app, {
  loop: true,
  delay: 75,
});
 
typewriter
  .pauseFor(2500)
  .typeString('La Capital del salamin picado fino cortado a 35 grados')
  .pauseFor(200)
  .deleteChars(10)
  .start();