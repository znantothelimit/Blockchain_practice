// const Web3 = require('web3'); // 전체 할당 (밑으로 수정)
const {Web3} = require('web3'); // 일부만 할당 deconstruction assignment, Web3 받아와야 하므로 Web3 변수명 유지필수!
const web3 = new Web3('http://127.0.0.1:7545'); // ganache로 들어가는 출입문 ; provider

const {abi, evm} = require('./Hello.json');
const initialGreeting = 'Hello, World ...';

var defaultAccount;
var contractAddress;

// async : 비동기로 동작하는 함수임을 js engine에 알림
// await : 비동기 함수 내에서 비동기로 처리할 것들에 대해 await 처리 async와 같이 쓰임
// solidity로 작성된 hello.sol 내 Contract 객체 내 함수를 부르는 비동기 함수 
async function callContract(deployedContract) {
  try {
    /* hello.sol 파일 내 greeting 값을 반환하는 함수 (읽기 전용 ; view ; 가스가 안들어감)
    function getGreeting() public view returns (string memory) {
        return greeting;
    } 
    를 부름, greeting 리턴될 때를 모르기때문에 끝날 때 동작하도록 await 처리!!*/
    const greeting = await deployedContract.methods.getGreeting().call();
    console.log('Greeting:', greeting);

    // call other contract function ?
    // const result = await deployedContract.methods.someFunction(parameter).call();
    // console.log('Result:', result);
  } catch (error) {
    console.error('Error:', error);
  }
}


function waitTenSeconds() {
  console.log("Wait for 5 seconds ...");
  
  // Callback function will be run after 5 sec = 5000 ms
  setTimeout(() => {
    console.log("\n5 seconds have passed ... !\n");
  }, 5000);
}

// 코드 구조가 중요!!!
const deployContract = async () => {
  // javascript Engine이 resolve(성공), reject(실패) 처리 -> promise
  return new Promise(async (resolve, reject) => { 
    try {
      // 배포를 하려면 누군가(개발자)가 EOA 사용하여 배포
      const accounts = await web3.eth.getAccounts();
      // Ganache의 경우 10 크기의 배열, Ganache 프로그램 내 index 확인
      const deployer = accounts[1];
      defaultAccount = accounts[1];

      // 위에서 바이트코드와 함께 json파일로 읽어온 abi, abi 규격에 맞춰서 helloContract Deploy
      const helloContract = new web3.eth.Contract(abi);

      /*     
      // 생성자(constructor ; 객체 생성 위함) 함수: 계약 배포 시 초기화를 위해 호출되는 함수
      // memory에 저장됨 -> 휘발성
         constructor(string memory initialGreeting) {
         // greeting 변수 초기화
         greeting = initialGreeting;
        }
        hello.sol 내 이 부분을 읽어옴
      */
      const deployTransaction = helloContract.deploy({
        data: evm.bytecode.object,
        arguments: [initialGreeting],
      });

      const deployReceipt = await deployTransaction.send({
        from: accounts[1],
        gas: '1000000',
      });

      contractAddress = deployReceipt.options.address; // 배포된 주소 -> CA ; 이 주소로 호출

      console.log('1. Deploy Account:', defaultAccount);
      console.log('1. Contract deployed to:', contractAddress);

      resolve({defaultAccount, contractAddress});
    } catch (error) {
      console.error('Error:', error);
      reject(error);
    }
  });
};

(async () => {
  try {
    const {defaultAccount, contractAddress} = await deployContract();
    console.log('2. Deploy Account:', defaultAccount);
    console.log('2. Contract deployed to:', contractAddress);

    const deployedContract = new web3.eth.Contract(abi, contractAddress);
    console.log('\n***** Before call: callContract *****');
    callContract(deployedContract);
    console.log('\n***** After call: callContract *****\n');

    console.log('3. Contract deployed to:', contractAddress);
    console.log('\n')

  } catch (error) {
    console.error('Error:', error);
  }
})();

console.log('***** Before call: waitTenSeconds *****');
waitTenSeconds();
console.log('***** After call: waitTenSeconds *****\n');

console.log('4. Contract deployed to:', contractAddress);
console.log('\n')
