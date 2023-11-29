// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

contract Voting {

    address votingManagerAddress;

    struct Candidate {
        address candidateAddress;
        uint votedCount;
    }

    struct VotingData {
        uint votedCandidateIndex;
        bool alreadyVoted;
    }

    modifier onlyManager() {
        require(msg.sender == votingManagerAddress);
        _;
    }

    mapping(address => VotingData) public voterToVotingData;

    Candidate[] public candidateList;

    constructor() {
        votingManagerAddress = msg.sender;
    }

    function registerCandidate(address _candidateAddress) onlyManager public {
        Candidate memory newCandidate = Candidate({
            candidateAddress: _candidateAddress,
            votedCount: 0
        });

        candidateList.push(newCandidate);
    }

    function letsVote(uint _candidateIndex) public {
        VotingData memory fetchedVotingData = voterToVotingData[msg.sender];
        // If voter vote for the first candidate in the list - the index is always 0
        if(_candidateIndex == 0) {
            require(fetchedVotingData.alreadyVoted == false, "You already voted for the first candidate");
            _addNewVote(_candidateIndex);
        }
        else {
            require(fetchedVotingData.votedCandidateIndex != _candidateIndex && fetchedVotingData.alreadyVoted == false, "You already voted for this candidate");
            _addNewVote(_candidateIndex);
        }
    }

    function _addNewVote(uint _candidateIndex) private {
        VotingData memory newVote = VotingData({
            votedCandidateIndex: _candidateIndex,
            alreadyVoted: true
        });

        voterToVotingData[msg.sender] = newVote;
        candidateList[_candidateIndex].votedCount++;
    }

    function numberOfCandidates() public view returns(uint) {
        return candidateList.length;
    }
}
