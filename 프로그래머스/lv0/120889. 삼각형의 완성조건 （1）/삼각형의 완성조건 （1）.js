function solution(sides) {
    var answer = 0
    var max_ = Math.max(...sides)
    var index = sides.indexOf(max_)
    sides.splice(index,1)
    
    if (max_ < sides[0]+sides[1]){
        answer = 1
    }else{
        answer = 2
    }
    return answer
}