const makeCounter = () => {
    let count = 0;

  return () => {
    return ++count;
  }
}

const counter1 = makeCounter();
const counter2 = makeCounter();
counter1()
counter1() // 2

counter2()
counter2()
counter2() // 3
