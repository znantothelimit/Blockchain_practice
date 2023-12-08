const express = require('express');
const app = express();
const PORT = 3000;

const {Web3} = require('web3');

app.use(express.static('public'));

app.use(express.json()); // Parse JSON requests

/*
app.get('/getAccounts', async (req, res) => {
  try {
  	console.log('in window.ethereum ...');
    const {accounts} = req.body; // Expecting accounts to be sent in the request body

    if (!accounts || !Array.isArray(accounts)) {
      return res.status(400).json({error: 'Invalid Request Payload ...'});
    }

    // Your server-side logic using MetaMask accounts
    // Example: Log the accounts received from the client
    console.log('MetaMask Accounts =', accounts);

    // Respond with a success message (or any other response you need)
    res.json({message: 'MetaMask accounts received successfully'});
  } catch (error) {
    console.error('Error handling MetaMask accounts:', error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
});
*/

app.post('/getAccounts', async (req, res) => {
  try {
    const {accounts} = req.body;

    if (!accounts || !Array.isArray(accounts)) {
      return res.status(400).json({error: 'Invalid request payload'});
    }

    // Your server-side logic using MetaMask accounts
    // Example: Log the accounts received from the client
    console.log('MetaMask Accounts =', accounts);

    // Respond with a success message (or any other response you need)
    res.json({message: 'MetaMask accounts received successfully'});
  } catch (error) {
    console.error('Error handling MetaMask accounts =', error);
    res.status(500).json({error: 'Internal Server Error'});
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
