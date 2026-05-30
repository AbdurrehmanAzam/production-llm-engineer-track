# 🧠 Phase 2: Algorithm Engineering Log

This log tracks algorithmic problem-solving with a strict focus on identifying space-time complexity tradeoffs.

### 1. Contains Duplicate (LeetCode #217)
* **Approach:** Hash Set detects duplicates by tracking seen elements.
* **Time Complexity:** O(n) - Single pass through the array.
* **Space Complexity:** O(n) - Hash set may store up to n elements.

### 2. Valid Anagram (LeetCode #242)
* **Approach:** Hash Map (Frequency Counter) to count character occurrences.
* **Time Complexity:** O(n) - Iterating through strings of length n.
* **Space Complexity:** O(n) / O(1) - O(1) if bounded by a 26-character alphabet.

### 3. Two Sum (LeetCode #1)
* **Approach:** Single-pass Hash Map for complement lookup (value -> index).
* **Time Complexity:** O(n) - Single pass through the array.
* **Space Complexity:** O(n) - Hash map stores up to n elements.
