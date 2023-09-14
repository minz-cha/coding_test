function solution(k, m, score) {
    var answer = 0;
    var count = 0;
    var min = 9;
    const temp = score.length % m 

    score.sort((a, b) => b - a);   
    score = score.slice(0, score.length-temp)
    
    for (let i = 0; i < score.length; i++){
        count += 1
        if (min > score[i]){
            min = score[i]
        }
        if (count == m){
            answer += min * m
            count = 0
            min = 9
        }
    }    
    
    return answer;
}