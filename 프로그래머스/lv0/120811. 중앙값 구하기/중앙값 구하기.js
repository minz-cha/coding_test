function solution(array) {
    var answer = 0;
    array = array.sort((a,b) => a-b)
    answer = parseInt(array.length / 2)
    return array[answer]
}