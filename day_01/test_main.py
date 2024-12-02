from BinaryTree import BinaryTree
import pytest

def test_insert_and_find():
    tree = BinaryTree()
    
    # Test single value
    tree.insert(5, 50)
    assert tree.find(5) == [50]
    
    # Test duplicate keys
    tree.insert(5, 30)
    tree.insert(5, 70)
    assert tree.find(5) == [50, 30, 70]
    
    # Test multiple keys
    tree.insert(3, 25)
    tree.insert(7, 75)
    assert tree.find(3) == [25]
    assert tree.find(7) == [75]

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

def test_find_nonexistent():
    tree = BinaryTree()
    tree.insert(5, 50)
    
    assert tree.find(10) is None

if __name__ == "__main__":
    pytest.main()