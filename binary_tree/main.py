# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        head = root
        stack = []
        res = []

        while head or stack:
            if head:
                res.append(head.val)
                if head.right:
                    stack.append(head.right)
                head = head.left
            else:
                head = stack.pop()

        return res

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        head = root
        stack = []
        res = []

        while head or stack:
            while head:
                stack.append(head)
                head = head.left
            
            head = stack.pop()
            res.append(head.val)

            head = head.right
        
        return res    

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        head = root
        stack = []
        res = []

        while head or stack:
            while head:
                stack.append(head)
                head = head.left if head.left else head.right
            head = stack.pop()
            res.append(head.val)
            if stack and stack[len(stack) - 1].left == head:
                head = stack[len(stack) - 1].right
            else:
                head = None
        return res            


def main() -> None:
    # "3 + 5 * 4"
    # [1, None, 2, 3]
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    nk = TreeNode("*", n5, n4)
    n3 = TreeNode(3)
    nq = TreeNode("+", n3, nk)
    root = nq

    solution = Solution()
    print("Preorder Traversal: ", solution.preorderTraversal(root))
    print("Inorder Traversal: ", solution.inorderTraversal(root))
    print("Postorder Traversal: ", solution.postorderTraversal(root))

if __name__ == "__main__":
    main()
