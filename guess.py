from typing import List, Literal, Tuple

Method = Literal["slow", "binary"]


def build_range(start: int, end: int) -> List[int]:
    assert isinstance(start, int) and isinstance(end, int), "start and end must be integers"
    assert start <= end, "start must be smaller than end"
    return list(range(start, end + 1))


def guess_number(target: int, nums: List[int], method: Method = "slow") -> Tuple[int, int]:
    assert isinstance(target, int), "target must be an integer"
    assert isinstance(nums, list), "nums must be a list"
    assert all(isinstance(x, int) for x in nums), "all elements in nums must be integers"
    assert len(nums) == len(set(nums)), "nums must be with no duplicates"
    assert len(nums) > 0, "nums must not be empty"
    assert target in nums, "target must be inside nums"
    assert method in ("slow", "binary"), "method must be 'slow' or 'binary'"

    if method == "slow":
        guesses = 0
        for x in nums:
            guesses += 1
            if x == target:
                return x, guesses
        return target, guesses

    arr = sorted(nums)
    low, high = 0, len(arr) - 1
    guesses = 0
    while low <= high:
        mid = (low + high) // 2
        guesses += 1 
        if arr[mid] == target:
            return arr[mid], guesses
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return target, guesses


def run_from_input() -> None:
    start = int(input("Enter start of range: ").strip())
    end = int(input("Enter end of range: ").strip())
    target = int(input("Enter the target number: ").strip())
    method = input("Enter method ('slow' or 'binary'): ").strip()

    nums = build_range(start, end)
    found, guesses = guess_number(target, nums, method)
    print(f"Guessed number: {found}, total guesses: {guesses}")


def run_from_input_candidates() -> None:
    raw = input("Enter candidate integers (you could use space or comma to separate them): ").strip()
    parts = [p for p in raw.replace(",", " ").split() if p]
    candidates = [int(p) for p in parts]
    if len(candidates) == 0:
        raise AssertionError("candidates must not be empty")
    if len(candidates) != len(set(candidates)):
        raise AssertionError("candidates must be unique")
    if not all(isinstance(x, int) for x in candidates):
        raise AssertionError("all candidates must be ints")

    target = int(input("Enter the target number: ").strip())
    if target not in candidates:
        raise AssertionError("target must be inside candidates")

    method = input("Enter method ('slow' or 'binary'): ").strip()
    if method not in ("slow", "binary"):
        raise AssertionError("method must be 'slow' or 'binary'")

    found, guesses = guess_number(target, candidates, method)
    print(f"Guessed number: {found}, total guesses: {guesses}")


if __name__ == "__main__":
    run_from_input()
