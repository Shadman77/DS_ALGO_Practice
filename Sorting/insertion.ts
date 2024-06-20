enum SortDirection {
  ASC = "asc",
  DESC = "desc",
}

const insertion = (
  arr: number[],
  sortingDirection: SortDirection
): number[] => {
  const ans = arr.map((element) => element);

  for (let index: number = 0; index < ans.length; index++) {
    let target: number = ans[index];
    let targetIndex: number = index;
    for (let indexTwo: number = index; indexTwo < ans.length; indexTwo++) {
      const element: number = ans[indexTwo];
      const condition: boolean =
        sortingDirection == SortDirection.ASC ? element < target : element > target;
      if (condition) {
        target = element;
        targetIndex = indexTwo;
      }
    }
    ans[targetIndex] = ans[index];
    ans[index] = target;
  }

  return ans;
};

const ques: number[] = [5, 4, 8, 9, 10];
console.log(ques);
console.log(insertion(ques, SortDirection.ASC));
console.log(insertion(ques, SortDirection.DESC));
