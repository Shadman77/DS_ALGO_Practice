const insertion = (arr: number[]): number[] => {
  const ans: number[] = arr.map((element) => element);
  for (let index = 0; index < ans.length; index++) {
    const target: number = ans[index];
    for (let indexTwo = 0; indexTwo < index; indexTwo++) {
      const current: number = ans[indexTwo];
      console.log(target, current)
      if (target < current) {
        ans[index] = current;
        ans[indexTwo] = target;
        break;
      }
    }
  }
  return ans;
};

const ques: number[] = [9, 6, 5, 1, 2];
console.log(insertion(ques));
