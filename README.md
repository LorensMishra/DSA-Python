---

# Stack and Queue – Data Structure Logic

This repository explains the **core logic of Stack and Queue data structures**, including their operations, working principles, and time–space complexities.

---

## 📌 Stack

### 🔹 What is a Stack?

A **Stack** is a **linear data structure** that follows the **LIFO principle**:

> **LIFO – Last In, First Out**

The element added last is removed first.

---

### 🔹 Basic Operations

* **Push** – Insert an element at the top
* **Pop** – Remove the top element
* **Peek / Top** – View the top element without removing it
* **isEmpty** – Check if stack is empty

---

### 🔹 Stack Logic (Concept)

* Insertion and deletion happen **only at one end** called the **top**
* Uses a single pointer/index (`top`) to track the last element

---

### 🔹 Time & Space Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |

**Space Complexity:** `O(n)` (depends on number of elements)

---

### 🔹 Applications of Stack

* Function calls (call stack)
* Expression evaluation
* Undo/Redo operations
* Parenthesis checking
* Backtracking algorithms

---

## 📌 Queue

### 🔹 What is a Queue?

A **Queue** is a **linear data structure** that follows the **FIFO principle**:

> **FIFO – First In, First Out**

The element added first is removed first.

---

### 🔹 Basic Operations

* **Enqueue** – Insert element at the rear
* **Dequeue** – Remove element from the front
* **Front / Peek** – View front element
* **isEmpty** – Check if queue is empty

---

### 🔹 Queue Logic (Concept)

* Insertion happens at the **rear**
* Deletion happens at the **front**
* Uses two pointers:

  * `front` → removal
  * `rear` → insertion

---

### 🔹 Time & Space Complexity

| Operation | Time Complexity |
| --------- | --------------- |
| Enqueue   | O(1)            |
| Dequeue   | O(1)            |

**Space Complexity:** `O(n)` (stores n elements)

---

### 🔹 Applications of Queue

* CPU scheduling
* Printer scheduling
* Breadth First Search (BFS)
* Customer service systems
* Data buffering

---

## 📌 Stack vs Queue

| Feature   | Stack        | Queue      |
| --------- | ------------ | ---------- |
| Order     | LIFO         | FIFO       |
| Insertion | Top          | Rear       |
| Deletion  | Top          | Front      |
| Use Case  | Backtracking | Scheduling |

---

## 📌 Summary

* **Stack** works on **LIFO**
* **Queue** works on **FIFO**
* Both are fundamental data structures used in **DSA, operating systems, and real-world applications**
* Understanding their **logic and operations** is essential for coding interviews

---

⭐ If you find this helpful, consider starring the repository!

## ✍️ Author

**Lorens Mishra**

---

