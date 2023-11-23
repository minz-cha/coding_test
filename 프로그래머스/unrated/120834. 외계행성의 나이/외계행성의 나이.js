function solution(age) {
    var answer = '';
    const alphabet = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j']
    const arr = age.toString().split('').map(Number);
    
    for (let i of arr){
        answer += alphabet[i]
    }
    return answer;
}