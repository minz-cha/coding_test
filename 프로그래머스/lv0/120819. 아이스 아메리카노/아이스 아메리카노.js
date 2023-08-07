function solution(money) {
    var answer = [];
    answer.push(parseInt(money/5500))
    money = money - 5500 *(parseInt(money/5500))
    answer.push(money)
    return answer;
}