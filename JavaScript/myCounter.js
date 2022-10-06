const makeCounter = () => {
    let count = 0;

  return () => {
    return ++count;
  }
}

const counter1 = makeCounter();
const counter2 = makeCounter();
