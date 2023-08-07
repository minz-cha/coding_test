function solution(n) {
    var answer = 0;
    var nArray = n.toString().split('')
    for (let i of nArray){
        answer += parseInt(i)
    }
    return answer;
}