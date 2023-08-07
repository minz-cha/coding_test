function solution(num_list) {
    var answer = [];
    var count = 0
    for (i=0; i < num_list.length; i++){
        if (num_list[i]%2 == 0){
            count += 1
        }
    }
    answer.push(count)
    answer.push(num_list.length-count)
    return answer;
}