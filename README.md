# Procrastination Sort

**“Why do it now… when you can panic later?”**

Procrastination Sort is a highly relatable (but terribly inefficient) sorting algorithm inspired by real human behavior.

Instead of sorting immediately, it delays progress, pretends to work, and only becomes productive when the pressure is high enough.

---

## How it Works

This algorithm operates in three phases:

### 🔴 Phase 1: Procrastination

Does absolutely nothing.
Just vibes. Maybe scrolls a bit. Thinks about starting… but doesn’t.

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
