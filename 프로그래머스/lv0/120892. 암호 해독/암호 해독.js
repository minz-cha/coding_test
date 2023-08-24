function solution(cipher, code) {
    var answer = '';
    for (i=0; i<cipher.length; i++){
        if (i % code == code-1){
            answer += cipher.at(i)
        }
    }
    return answer;
}