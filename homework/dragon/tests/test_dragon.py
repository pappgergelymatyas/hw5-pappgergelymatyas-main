import math
from homework.dragon.dragon import dragon_solution

# Global variable and counter for testing
last_dead_cow_rank = None
is_dead_call_count = 0


def is_dead(cow_rank):
    """Returns True if the cow with the given rank is dead; otherwise, False."""
    global is_dead_call_count, last_dead_cow_rank
    is_dead_call_count += 1
    print(cow_rank)
    return cow_rank <= last_dead_cow_rank if last_dead_cow_rank is not None else False


class TestDragonSolution:
    def setup_method(self):
        """Reset global variables before each test."""
        global last_dead_cow_rank, is_dead_call_count
        last_dead_cow_rank = None
        is_dead_call_count = 0

    def test_all_alive(self):
        """Test case where all cows are alive."""
        global last_dead_cow_rank
        last_dead_cow_rank = None
        num_cows = 5

        expected_result = 0
        assert dragon_solution(is_dead, num_cows) == expected_result

    def test_all_dead(self):
        """Test case where all cows are dead."""
        global last_dead_cow_rank
        num_cows = 5
        last_dead_cow_rank = num_cows

        assert dragon_solution(is_dead, num_cows) == num_cows

    def test_partial_dead(self):
        """Test case where some cows up to a rank are dead."""
        global last_dead_cow_rank
        last_dead_cow_rank = 3
        num_cows = 5

        assert dragon_solution(is_dead, num_cows) == last_dead_cow_rank

    def test_edge_case_single_cow_alive_right(self):
        """Test case with only the smallest cow alive."""
        global last_dead_cow_rank
        last_dead_cow_rank = 4
        num_cows = 5

        assert dragon_solution(is_dead, num_cows) == last_dead_cow_rank

    def test_edge_case_single_cow_alive_left(self):
        """Test case with only the smallest cow alive."""
        global last_dead_cow_rank
        last_dead_cow_rank = 3
        num_cows = 11

        assert dragon_solution(is_dead, num_cows) == last_dead_cow_rank

    def test_edge_case_first_cow_dead(self):
        """Test case where only the largest cow is dead."""
        global last_dead_cow_rank
        last_dead_cow_rank = 1
        num_cows = 5

        assert dragon_solution(is_dead, num_cows) == last_dead_cow_rank

    def test_dragon_solution_efficiency(self):
        """Test binary search efficiency by checking function call count."""
        global last_dead_cow_rank, is_dead_call_count
        num_cows = 1000
        last_dead_cow_rank = 500
        is_dead_call_count = 0

        result = dragon_solution(is_dead, num_cows)

        assert result == last_dead_cow_rank

        max_calls = math.ceil(math.log2(num_cows)) + 1
        assert (
            is_dead_call_count <= max_calls
        ), f"Expected at most {max_calls} calls, but got {is_dead_call_count}"

    def test_large_number_of_cows_all_alive(self):
        """Test with a large number of cows where all cows are alive."""
        global last_dead_cow_rank, is_dead_call_count
        last_dead_cow_rank = None
        is_dead_call_count = 0
        num_cows = 10**6

        result = dragon_solution(is_dead, num_cows)
        assert result == 0

    def test_large_number_of_cows_partial_dead(self):
        """Test with a large number of cows where some cows are dead starting from the largest."""
        global last_dead_cow_rank, is_dead_call_count
        num_cows = 10**6
        last_dead_cow_rank = 500000
        is_dead_call_count = 0

        result = dragon_solution(is_dead, num_cows)
        assert result == last_dead_cow_rank
