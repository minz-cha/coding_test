function solution(array) {
    const answer = []
    const maxValue = Math.max(...array);
    const index_ = array.indexOf(maxValue)
    answer.push(maxValue)
    answer.push(index_ )
    return (answer)
}