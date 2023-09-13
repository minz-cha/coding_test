function solution(new_id) {
    answer = []
    // 1,2단계
    new_id = new_id.toLowerCase().replace(/[^\w-.]/g, "")
    // 3단계
    for(let i=0;i< new_id.length;i++){
        if((new_id[i] == ".") && (new_id[i]==new_id[i+1])) {
            continue
        }
        answer.push(new_id[i])
    }
    new_id = answer.join("")
    // 4단계 
    new_id = new_id.charAt(0) == "." ? new_id.slice(1) : new_id
    new_id = new_id.charAt(new_id.length-1) == "." ? new_id.slice(0,-1) : new_id
    // 5단계
    if (new_id == ""){
        return "aaa"
    }
    // 6단계
    new_id = new_id.length >= 16 ? new_id.slice(0,15) : new_id
    new_id = new_id.charAt(new_id.length-1) == "." ? new_id.slice(0,-1) : new_id
    // 7단계
    while (new_id.length < 3) {
        new_id = new_id + new_id.charAt(new_id.length-1)
    }

    return new_id;
}
