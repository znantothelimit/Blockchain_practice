// SPDX-License-Identifier: MIT

// solidity compile을 위한 명령어
// solcjs --bin --abi Hello.sol 

// Solidity 버전 지정
pragma solidity ^0.8.0;

// Hello 스마트 계약 정의
contract Hello {
    // greeting 변수 선언 및 공개 접근자 설정
    string public greeting;

    // 생성자(constructor ; 객체 생성 위함) 함수: 계약 배포 시 초기화를 위해 호출되는 함수
    // memory에 저장됨 -> 휘발성
    constructor(string memory initialGreeting) {
        // greeting 변수 초기화
        greeting = initialGreeting;
    }

    // greeting 값을 반환하는 함수 (읽기 전용 ; view ; 가스가 안들어감)
    function getGreeting() public view returns (string memory) {
        return greeting;
    }

    // greeting 값을 설정하는 함수
    // 가스 사용: 상태 변수를 변경하는 트랜잭션은 가스가 필요하며 사용자(개발자의 EOA)가 지불해야 함
    // 가스 비용은 트랜잭션을 처리하는 마이너에게 보상으로 지급됨
    function setGreeting(string memory newGreeting) public {
        greeting = newGreeting;
    }
}
