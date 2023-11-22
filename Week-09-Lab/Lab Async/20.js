// Promises

console.log();
console.log('*** Start ...');

function getData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      const data = "Promises : Data arrived ...";
      resolve(data);
      // In case of failure: reject("An error occurred while fetching data ...");
    }, 2000);
  });
}

getData()
  .then((result) => {
    console.log(result);
  })
  .catch((error) => {
    console.error(error);
  });


console.log('*** End ...');
console.log();
