function solution(n, k) {
    k = k - parseInt(n/10)
    answer = n*12000 + k*2000
    return answer;
}