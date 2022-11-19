## Selection Sort Algo
  - Time complexity is O(n^2)
  - First findout the minimum value and took the value in the right place.


# Algo
```java
void selectionSort(int a[], int n){
    int i=0; index_min = 0;
    for(i = 0; i<n-1; i++){
        index_min = i;
        for(int j = 0; j<n; j++){
            if(a[j] < a[index_min]){
                index_min = j;
            }
        }

        if(index_min != i){
            temp = a[index_min];
            a[index_min] = a[i];
            a[i] = temp;
        }
    }
}
```