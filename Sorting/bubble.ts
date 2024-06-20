const bubbleSort = (arr: number[]): number[] => {
  const ans: number[] = arr.map((element) => element);
  for (let index = 0; index < ans.length; index++) {
    for (let indexTwo = 0; indexTwo < ans.length - index; indexTwo++) {
      const firstElement: number = ans[indexTwo];
      const secondElement: number = ans[indexTwo + 1];
      if (firstElement > secondElement) {
        ans[indexTwo] = secondElement;
        ans[indexTwo + 1] = firstElement;
      }
    }
  }
  return ans;
};

const arr: number[] = [10, 8, 5, 6, 4, 1, 2, 3, 7, 9];
const ans: number[] = bubbleSort(arr);

console.log(arr, ans);
