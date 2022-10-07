// Func to allow multiple counts
const makeCounter = () => {
    let count = 0;

  return () => {
    return ++count;
  }
}

// Multiple count vars
const counter1 = makeCounter();
const counter2 = makeCounter();
