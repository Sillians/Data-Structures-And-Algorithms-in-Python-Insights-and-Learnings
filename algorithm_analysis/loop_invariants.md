# loop invariant

A **loop invariant** is a formal property used to prove the correctness of algorithms involving loops. It is a condition that holds true before and after each iteration of a loop, thereby ensuring that the algorithm behaves as expected. To justify the correctness of an algorithm using a loop invariant, the following three steps are typically followed:

---

### 1. **Initialization**
   - Show that the loop invariant is true **before the first iteration** of the loop. This step ensures that the invariant is valid at the start of the loop.

---

### 2. **Maintenance**
   - Show that if the loop invariant is true **before an iteration**, it remains true **after that iteration**. This step ensures that the invariant is preserved throughout the loop execution.

---

### 3. **Termination**
   - Show that when the loop terminates, the invariant combined with the loop's termination condition implies the correctness of the algorithm. This step connects the invariant to the desired final result of the algorithm.

---

### Example: Loop Invariant in Selection Sort

#### Problem: Prove the correctness of the selection sort algorithm using a loop invariant.

#### Algorithm Outline:
1. The array is divided into a sorted and an unsorted region.
2. During each iteration, the smallest element in the unsorted region is moved to the end of the sorted region.

#### Loop Invariant:
At the start of each iteration of the loop, the portion of the array before the current index `i` is sorted and contains the smallest elements from the original array.

#### Proof:
1. **Initialization**:
   - Before the first iteration, the sorted portion is empty (i.e., no elements are considered sorted), which trivially satisfies the invariant.

2. **Maintenance**:
   - During each iteration, the smallest element in the unsorted region is identified and swapped with the first element of the unsorted region. This expands the sorted portion by one element while maintaining its order. Hence, the invariant remains true.

3. **Termination**:
   - When the loop terminates, the sorted portion includes the entire array, and the unsorted region is empty. The invariant ensures that the array is fully sorted at this point.

---

### Importance of Loop Invariants
Using a loop invariant provides a structured and rigorous way to verify the correctness of algorithms, especially those with complex iterative steps. It ties the algorithm's intermediate states to its overall correctness.