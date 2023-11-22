// Callback Function

console.log();
console.log('*** Start ...');

function getData(callback) {
  setTimeout(() => {
    const data = "Callback Function : Data arrived ...";
    callback(data);
  }, 2000);
}

getData((result) => {
  console.log(result);
});

console.log('*** End ...');
console.log();
