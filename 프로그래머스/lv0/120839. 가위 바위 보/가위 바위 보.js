function solution(rsp) {
    var answer = '';
    var rsp = rsp.split('')
    
    for (const element of rsp){
        if (element == '2'){
            answer += '0'
        } else if (element == '0'){
            answer += '5'
        }else {
            answer += '2'
        }
    }
    return answer;
}