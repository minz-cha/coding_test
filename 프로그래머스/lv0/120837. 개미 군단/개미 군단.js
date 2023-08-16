function solution(hp) {
    const first = parseInt(hp / 5)
    const second = parseInt((hp%5)/3)
    const third = (hp%5)%3
    return first + second + third;
}