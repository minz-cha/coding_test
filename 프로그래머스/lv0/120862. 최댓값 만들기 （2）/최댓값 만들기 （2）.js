function solution(numbers) {
    var answer = 0;
    numbers = numbers.sort((a,b)=>a-b)
    var a = numbers[0] * numbers[1]
    var b =  numbers[numbers.length - 1] * numbers[numbers.length - 2];
    answer = (a>b) ? a : b
    return answer;
}