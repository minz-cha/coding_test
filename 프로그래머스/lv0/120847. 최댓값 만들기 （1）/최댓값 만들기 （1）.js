function solution(numbers) {
    numbers.sort(function(a, b)  {
        return a - b;
    });
    return numbers.at(-1) * numbers.at(-2)
    
}