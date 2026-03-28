# Procrastination Sort

**“Why do it now… when you can panic later?”**

**For dependencies: You just need the visualization lib from python, "matplolib"**

## How it Works

This algorithm operates in three phases:

### 🔴 Phase 1: Procrastination

Does absolutely nothing.

---

### 🟡 Phase 2: Fake Productivity

Looks busy, but isn’t actually making meaningful progress.

* Performs random swaps
* Rearranges elements without a clear goal
* May even make the array worse

---

### 🟢 Phase 3: Panic Mode

Deadline hits. Survival instincts activate.

* Executes an actual sorting algorithm (usually Bubble Sort)
* Rapid, chaotic, but effective
* Somehow gets the job done at the last minute

---

## Time Complexity

| Phase           | Complexity                   |
| --------------- | ---------------------------- |
| Procrastination | O(1) (emotionally O(stress)) |
| Fake Work       | O(n) to O(n²)                |
| Panic Mode      | O(n²)                        |

### Overall:

**O(n²)** — dominated by the final panic sorting phase.


### PS. This is basically just a delayed bubble sort. Made just for funsies.
