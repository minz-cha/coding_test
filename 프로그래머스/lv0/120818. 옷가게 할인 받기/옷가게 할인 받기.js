function solution(price) {
    var answer = 0;
    if (price >= 500000){
        return Math.floor(price*0.8)
    }else if (500000 > price && price >= 300000){
        return Math.floor(price*0.9)
    }else if (300000 > price && price >= 100000){
        return Math.floor(price*0.95)
    }else{
        return price
    }
}