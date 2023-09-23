function solution(a, b) {
    var days = 0
    const month = [31,29,31,30,31,30,31,31,30,31,30,31]
    for (let i=0; i< a-1; i++){
        days += month[i]
    }
    days += b
    switch (days % 7){
        case 1:
            return "FRI"
        case 2: 
            return "SAT"
        case 3:
            return "SUN"
        case 4:
            return "MON"
        case 5:
            return "TUE"
        case 6:
            return "WED"
        default:
            return "THU"
    }
}