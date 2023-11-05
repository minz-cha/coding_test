function solution(people, limit) {
    people = people.sort((a, b) => b - a)
    let answer = 0
    let [first, last] = [0, people.length-1]
    
    while(first <= last){
        let sum = people[first] + people[last]
        if (sum <= limit){
            last -= 1
        }
        first += 1
        answer += 1
    }
    return answer;
}