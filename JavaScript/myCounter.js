const Counter = () => {
    let count = 0;
    return () => {
        return count++;
    }
}

const count1 = Counter();
const count2 = Counter();
