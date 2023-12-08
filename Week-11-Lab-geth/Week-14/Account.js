// npm init
// npm i web3
// node Account.js

const {Web3} = require('web3');

const url = 'http://127.0.0.1:8545'; // geth
const web3 = new Web3(new Web3.providers.HttpProvider(url)); 

web3.eth.getAccounts()
  .then(accounts => {
    console.log('Accounts:', accounts);

    // Now you can use 'web3' to interact with the Ethereum blockchain
  })
  .catch(error => {
    console.error('Error fetching accounts:', error);
  });
