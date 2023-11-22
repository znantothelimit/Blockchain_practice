// Async and Await

console.log();
console.log('*** Start ...');

function getData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      const data = "Async/Await : Data arrived ...";
      resolve(data);
    }, 2000);
  });
}

async function getDataAsync() {
  const result = await getData();
  console.log(result);
}

getDataAsync();

console.log('*** End ...');
console.log();
