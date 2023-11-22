// Async Fn with Promise ...
function getData() {
  return new Promise((resolve, reject) => {
    // Async Operation (Ex: Call API)
    setTimeout(() => {
      const data = "Data arrived ...";
      // if Success in Async Op -> send data by resolve
      resolve(data);
      // if Fail in Async Op -> send data by reject
      // reject("Operation fail in Async Op ...");
    }, 2000);
  });
}

// Define Async Fn
async function getDataAsync() {
  try {
    // �񵿱� �۾��� �����ϰ� ����� ��� ���� await ���
    console.log("Starting in getDataAsync() ...");
    const result = await getData();
    console.log("Waiting Result ...");
    console.log(result);
  } catch (error) {
    console.error("Error =", error);
  }
}

console.log("Before getDataAsync() Fn ...");
getDataAsync();
console.log("After getDataAsync() Fn ...");
