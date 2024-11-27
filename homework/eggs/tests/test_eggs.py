import math
import hashlib
from homework.eggs.eggs import eggs_solution

egg_break_floor = None
breaks_call_count = 0
eggs_broken_count = 0


def breaks(floor):
    """Simulates the egg breaking check."""
    global breaks_call_count, eggs_broken_count
    breaks_call_count += 1
    if floor > egg_break_floor:
        eggs_broken_count += 1
        return True
    return False


def md5_hash(number):
    """Returns the MD5 hash of a given number as a string."""
    return hashlib.md5(str(number).encode()).hexdigest()

y
class TestEggSolution:
    def setup_method(self):
        """Reset global variables before each test."""
        global egg_break_floor, breaks_call_count, eggs_broken_count
        egg_break_floor = None
        breaks_call_count = 0
        eggs_broken_count = 0

    def test_all_possible_scenarios(self, capsys):
        """Test all floors from 0 to 100 as the breaking floor."""
        global egg_break_floor, breaks_call_count, eggs_broken_count

        min_drops = float("inf")
        max_drops = 0
        total_drops = 0
        success_count = 0
        error_list = []

        for floor in range(101):
            egg_break_floor = floor
            breaks_call_count = 0
            eggs_broken_count = 0

            result = eggs_solution(breaks)

            if result != floor:
                error_list.append(
                    f"Failed for floor {floor}: Expected {floor}, got {result}"
                )

            if eggs_broken_count > 2:
                error_list.append(f"Failed for floor {floor}: Broke more than 2 eggs.")

            if result == floor and eggs_broken_count <= 2:
                success_count += 1

            total_drops += breaks_call_count
            min_drops = min(min_drops, breaks_call_count)
            max_drops = max(max_drops, breaks_call_count)

        mean_drops = total_drops / 101

        print("Eggs task:")
        print(f"Minimum drops: {min_drops}")
        print(f"Maximum drops: {max_drops}")
        print(f"Mean drops: {mean_drops:.2f}")
        print(f"Total successful tests: {success_count}")

        optimal_md5 = "aab3238922bcc25a6f606eb525ffdc56"

        if success_count != 101:
            print("Errors encountered:")
            for error in error_list:
                print(error)
            assert False, f"Test failed with {101 - success_count} unsuccessful cases."
        elif md5_hash(math.ceil(max_drops)) == optimal_md5 and success_count == 101:
            print("Congratulations! Your solution achieved optimal performance.")
        else:
            print("Good solution, but not optimal performance.")
