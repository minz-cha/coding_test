function solution(numbers) {
    var num = 0;
    for (i = 0; i < numbers.length; i++){
        num += numbers[i]
    }
    return num/numbers.length;
}