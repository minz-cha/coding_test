function solution(array) {
    let counting = new Map();
    let countArray = new Array;
    let maxKey;
    let maxValue = -1;
    let hasMultipleMaxValues = false;
    
    for (let i of array){
        if (!counting.has(i)){
            counting.set(i,1);
        }else if (counting.has(i)){
            counting.set(i, counting.get(i)+1);
        }
    }
    
    for (let [key, value] of counting) {
        if (value > maxValue) {
            maxValue = value;
            maxKey = key;
            hasMultipleMaxValues = false;
        }else if (value === maxValue) {
            hasMultipleMaxValues = true;
        }
    }
    
    return (hasMultipleMaxValues) ? -1: maxKey;
     
}
