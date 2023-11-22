// Define Async Fn ...
function fetchData() {
  return new Promise((resolve) => {
    setTimeout(() => {
      const data = "Data arrived ...";
      console.log(data);
      resolve(data);
    }, 2000);
  });
}

fetchData()
  // data가 result가 됨 이후 promise 객체가 또 리턴 그러면 또 .then에서 그 객체가 또 promise 객체 리턴 ... chain 형식으로 동작
  .then((result) => {
    console.log("1st then() =", result);
    // Additional Async Operation ...
    return "Additional Data ...";
  })
  .then((additionalData) => {
    console.log("2nd then() =", additionalData);
  })
  .catch((error) => {
    console.error("Error =", error);
  });
