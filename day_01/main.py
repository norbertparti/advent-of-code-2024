from pathlib import Path
from BinaryTree import BinaryTree


def read_input(input_file):
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            left, right = line.split()

            yield left, right

def main(input_file):
    """Main fucntion which reads the input.

    Args:
        input_file (_type_): Text file with 2 columns of numbers.
    """
    left_tree = BinaryTree()
    right_tree = BinaryTree()
    line_count = 1
    for left, right in read_input(input_file):
        left_tree.insert(int(left), line_count)
        right_tree.insert(int(right), line_count)
        line_count += 1

    left = left_tree.inorder_traversal()
    right = right_tree.inorder_traversal()
    summ = 0
    for l, r in zip(left, right):
        diff_value = abs(l[0] - r[0])
        summ += diff_value
    print(left)
    print(right)
    print(summ)


if __name__ == "__main__":
    current_dir = Path(__file__).parent
    input_file = current_dir / "inputs" /"test_input.txt"
    main(input_file)
