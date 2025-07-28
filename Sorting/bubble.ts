enum SortDirection {
  Asc = "asc",
  Desc = "dsc",
}

const bubbleSort = (arr: number[], direction: SortDirection): number[] => {
  const ans: number[] = arr.map((element) => element);
  for (let index = 0; index < ans.length; index++) {
    for (let indexTwo = 0; indexTwo < ans.length - index; indexTwo++) {
      const firstElement: number = ans[indexTwo];
      const secondElement: number = ans[indexTwo + 1];

      const condition: boolean =
        direction === SortDirection.Asc
          ? firstElement > secondElement
          : secondElement > firstElement;

      if (condition) {
        ans[indexTwo] = secondElement;
        ans[indexTwo + 1] = firstElement;
      }
    }
  }
  return ans;
};

const arr: number[] = [10, 8, 5, 6, 4, 1, 2, 3, 7, 9];
const ansAsc: number[] = bubbleSort(arr, SortDirection.Asc);
const ansDsc: number[] = bubbleSort(arr, SortDirection.Desc);

console.log(arr, ansAsc, ansDsc);
