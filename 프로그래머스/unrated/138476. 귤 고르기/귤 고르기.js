function solution(k, tangerine) {
    const tan_count = new Map();
    for(let i = 0; i < tangerine.length; i++) {
        const target = tan_count.get(tangerine[i]);
        tan_count.set(tangerine[i], target ? target + 1 : 1);
    }
    const val = Array.from(tan_count.values()).sort((a, b) => b - a);
    let count = 0;
    for(let i = 0; i < val.length; i++) {
        if (k <= 0) break;
        k -= val[i];
        count++;
    }
    return count;
}