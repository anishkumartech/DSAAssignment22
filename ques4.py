def check_traversal_match(inorder, preorder, postorder):
    if len(inorder) == len(preorder) == len(postorder) == 0:
        return True

    if len(inorder) != len(preorder) or len(inorder) != len(postorder):
        return False

    if len(inorder) == len(preorder) == len(postorder) == 1:
        return inorder[0] == preorder[0] == postorder[0]

    root = preorder[0]

    # Find the index of the root in the inorder traversal
    root_index = inorder.index(root)

    # Check if the left subtree matches
    left_inorder = inorder[:root_index]
    left_preorder = preorder[1:1 + len(left_inorder)]
    left_postorder = postorder[:len(left_inorder)]
    left_match = check_traversal_match(left_inorder, left_preorder, left_postorder)

    # Check if the right subtree matches
    right_inorder = inorder[root_index + 1:]
    right_preorder = preorder[1 + len(left_inorder):]
    right_postorder = postorder[len(left_inorder):-1]
    right_match = check_traversal_match(right_inorder, right_preorder, right_postorder)

    return left_match and right_match

# Example usage
inorder = [4, 2, 5, 1, 3]
preorder = [1, 2, 4, 5, 3]
postorder = [4, 5, 2, 3, 1]

if check_traversal_match(inorder, preorder, postorder):
    print("Yes")
else:
    print("No")
