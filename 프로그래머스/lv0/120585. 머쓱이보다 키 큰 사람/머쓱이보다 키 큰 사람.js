function solution(array, height) {
    var answer = 0;
    for (let i of array){
        if (height < i){
            answer += 1
        }
    }
    return answer;
}