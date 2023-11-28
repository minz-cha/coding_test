function solution(emergency) {
    const answer = [];
    const temp = [...emergency]; 
    emergency.sort((a, b) => b - a);
    
    for (const i of temp) {
        const index = emergency.indexOf(i);
        answer.push(index + 1);
    }
    
    return answer;
}

