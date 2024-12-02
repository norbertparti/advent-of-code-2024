from BinaryTree import BinaryTree
import pytest

def test_inorder_traversal():
    tree = BinaryTree()
    
    # Insert values with duplicates
    tree.insert(5, 50)
    tree.insert(3, 30)
    tree.insert(5, 55)
    tree.insert(7, 70)
    tree.insert(5, 52)
    
    # Check if inorder traversal maintains both BST property and insertion order for duplicates
    expected = [(3, 30), (5, 50), (5, 55), (5, 52), (7, 70)]
    assert tree.inorder_traversal() == expected

if __name__ == "__main__":
    pytest.main()