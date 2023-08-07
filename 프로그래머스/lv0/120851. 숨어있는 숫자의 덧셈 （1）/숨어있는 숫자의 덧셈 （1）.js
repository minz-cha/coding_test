function solution(my_string) {
    var answer = 0;
    var regex = /[^0-9]/g //숫자 아닌 문자만 선택
    var result = my_string.replace(regex, "")
    var nArray = result.toString().split("")
    for (let i of nArray){
        answer += parseInt(i)
    }
    return answer;
}