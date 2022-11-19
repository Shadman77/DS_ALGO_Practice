## Insertion Sort Algo
  - Best case time complexity is O(n)
  - Worst case time complexity is O(n^2)
  - If you confidence max #of elements are already in sorted order. Then insertion sort Algo should use.

# Algo
```java
void insertionSort(int a[], int n){
   for(int i=1; i<n; i++){
    j = i-1;
    item = a[i];
    while(j>=0 && a[j] > item){
        a[j+1] = a[j];
        j--;
    }
    a[j+1] = item;
   }
 }
```