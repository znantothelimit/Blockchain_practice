/*

solcjs --bin --abi Hello.sol
solcjs --bin --abi Hello.sol -o build

* const {abi, evm} = require('./Hello.json');
* Hello.json
	{
	  "abi": [...],
	  "evm": {
	    "bytecode": {
	      "object": "0x..."
	    }
	  }
	}

*/

const fs = require('fs');

const abi = JSON.parse(fs.readFileSync('./Hello_sol_Hello.abi', 'utf8'));
const bytecode = '0x' + fs.readFileSync('./Hello_sol_Hello.bin', 'utf8');

// const bytecode = '0x' + fs.readFileSync('Hello_sol_Hello.bin').toString()
// const abi = JSON.parse(fs.readFileSync('Hello_sol_Hello.abi').toString())

const contractJson = {abi, evm: {bytecode: {object: bytecode}}};
fs.writeFileSync('./Hello.json', JSON.stringify(contractJson, null, 2));
