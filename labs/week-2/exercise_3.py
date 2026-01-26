"""
Exercise 3: Set Operations
TASK: Write tests for the provided function

The function find_common_and_unique is provided below.
- Write at least 5 tests that verify it works correctly.
- Consider: basic cases, empty sets, no overlap, complete overlap, subset relationships, etc
- Write descriptive test function names such as:
    - test_find_common_and_unique_basic()
    - test_find_common_and_unique_no_overlap()
    - test_find_common_and_unique_complete_overlap()
    - test_find_common_and_unique_empty_sets()
"""


def find_common_and_unique(set_a: set[str], set_b: set[str]) -> dict[str, set[str]]:
    """
    Find common elements and unique elements in two sets.

    Args:
        set_a: First set of strings
        set_b: Second set of strings

    Returns:
        Dictionary with keys:
        - 'common': elements in both sets (intersection)
        - 'only_a': elements only in set_a (difference)
        - 'only_b': elements only in set_b (difference)
    """
    return {
        'common': set_a & set_b,
        'only_a': set_a - set_b,
        'only_b': set_b - set_a
    }


# YOUR TESTS HERE
# Write at least 5 tests for find_common_and_unique
# Test function names must start with "test_"

def test_find_common_and_unique_basic():
    """Test with basic sets that have overlapping elements."""
    set_a: set[str] = {"apple", "banana", "cherry"}
    set_b: set[str] = {"banana", "cherry", "pear"}

    found_sets: dict[str, set[str]] = find_common_and_unique(set_a, set_b)
    
    assert found_sets["common"] == {"banana", "cherry"}
    assert found_sets["only_a"] == {"apple"}
    assert found_sets["only_b"] == {"pear"}

def test_find_common_and_unique_no_overlap():
    """Test with sets that have no common elements."""
    set_a: set[str] = {"apple", "grape", "melon"}
    set_b: set[str] = {"banana", "cherry", "pear"}

    found_sets: dict[str, set[str]] = find_common_and_unique(set_a, set_b)
    assert found_sets["common"] == set()
    assert found_sets["only_a"] == {"apple", "grape", "melon"}
    assert found_sets["only_b"] == {"banana", "cherry", "pear"}

def test_find_common_and_unique_complete_overlap():
    """Test with identical sets."""
    set_a: set[str] = {"banana", "cherry", "pear"}
    set_b: set[str] = {"banana", "cherry", "pear"}

    found_sets: dict[str, set[str]] = find_common_and_unique(set_a, set_b)
    assert found_sets["common"] == {"banana", "cherry", "pear"}
    assert found_sets["only_a"] == set()
    assert found_sets["only_b"] == set()

def test_find_common_and_unique_empty_sets():
    """Test with both sets being empty."""
    set_a: set[str] = set()
    set_b: set[str] = set()

    found_sets: dict[str, set[str]] = find_common_and_unique(set_a, set_b)
    assert found_sets["common"] == set()
    assert found_sets["only_a"] == set()
    assert found_sets["only_b"] == set()

def test_find_common_and_unique_one_empty_set():
    """Test with one set being empty, and one not."""
    set_a: set[str] = {"banana", "cherry", "pear"}
    set_b: set[str] = set()

    found_sets: dict[str, set[str]] = find_common_and_unique(set_a, set_b)
    assert found_sets["common"] == set()
    assert found_sets["only_a"] == {"banana", "cherry", "pear"}
    assert found_sets["only_b"] == set()

