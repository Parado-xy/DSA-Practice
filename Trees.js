// Types of Trees. 
// A nice way to understand a tree is with a recursive explanation. 
// A tree is a data Structure composed of nodes. 
// Each Tree has a root node
// The root node has zero or more child nodes
// Each child node has zero or more child nodes, and so on. 

// The Trees cannot contain cycles. The nodes may or may not be in a particular order, they could have 
// any data types as values, and they may or may not have links back to their parent nodes. 


// A very simple definition for Node:
class TreeNode {
    /**
     * Creates an instance of a tree node.
     * @param {*} value - The value to be stored in the node.
     */
    constructor(value) {
        this.value = value;
        this.children = [];
    }

    /**
     * Adds a child node to the current node.
     * @param {TreeNode} node - The child node to be added.
     */
    addChild(node) {
        this.children.push(node);
    }

    /**
     * Removes a child node from the current node.
     * @param {TreeNode} node - The child node to be removed.
     * @returns {boolean} - True if the child was removed, false if not found.
     */
    removeChild(node) {
        if (this.children.indexOf(node) !== -1) {
            this.children.splice(index, 1);
            return true;
        }
        return false;
    }

    /**
     * Prints the tree structure in a pre-order traversal.
     * @param {number} level - The current level of depth in the tree (used for formatting).
     */
    printTree(level = 0) {
        console.log('  '.repeat(level) + this.value);
        for (let child of this.children) {
            child.printTree(level + 1);
        }
    }
}


const root = new TreeNode('Root');
const child1 = new TreeNode('Child 1');
const child2 = new TreeNode('Child 2');
const grandchild = new TreeNode('Grandchild 1');

// Build the tree
root.addChild(child1);
root.addChild(child2);
child1.addChild(grandchild);

// Print the tree
root.printTree();

// Trees vs. Binary Trees 
// A binary tree is a tree in which each node has up to two children. Not all trees are binary trees.

// There are occasions when you might have a tree that is not a binary tree. For example, suppose you were 
// using a tree to represent a bunch of phone numbers. In this case, you might use a 10-ary tree, with each 
// node having up to 10 children (one for each digit). 
// A node is called a "leaf" node if it has no children.

// A **Binary Search Tree (BST)** is a specific type of binary tree in which each node has the following properties:

// 1. **Node Structure**:
//    - Each node contains a value, a reference to the left child, and a reference to the right child.
   
// 2. **Binary Property**:
//    - Each node can have at most two children, typically referred to as the left and right children.

// 3. **Binary Search Property**:
//    - For any given node:
//      - The value of **all nodes in the left subtree** is **less than** the value of the current node.
//      - The value of **all nodes in the right subtree** is **greater than or equal to** the value of the current node.

// This structure allows for efficient searching, insertion, and deletion of elements because at each node, the search can be directed to either the left or the right subtree based on the comparison of the current node’s value with the target value.

// ### Key Operations in a Binary Search Tree:
// - **Search**: Start at the root and recursively compare the target value with the node’s value. Move left if the target is smaller, and right if larger, until the target is found or the subtree is empty.
// - **Insertion**: Insert the new value at the appropriate leaf position by recursively moving left or right based on the same comparisons.
// - **Deletion**: There are three cases when deleting a node:
//   1. The node has no children (a leaf node): Simply remove the node.
//   2. The node has one child: Remove the node and replace it with its child.
//   3. The node has two children: Find the node’s in-order successor (smallest node in its right subtree), replace the node’s value with that, and then delete the in-order successor.

// ### Example of a Binary Search Tree:

// ```
//         50
//        /  \
//      30    70
//     /  \   /  \
//   20   40 60   80
// ```

// - The left subtree of the root (50) has values less than 50, and the right subtree has values greater than 50.
// - The left child of 30 has a value of 20, and the right child of 30 has a value of 40, maintaining the binary search property at each node.

// ### Time Complexity:
// - **Best/Average Case** (for balanced BSTs): O(log n) for search, insertion, and deletion, where `n` is the number of nodes.
// - **Worst Case** (for unbalanced BSTs): O(n), when the tree degrades to a linked list, e.g., if nodes are inserted in sorted order.

// BSTs are fundamental in many applications where quick lookup and ordered data are required, but care must be taken to ensure that they remain balanced to maintain their efficiency.


// Balanced vs. Unbalanced 
// While many trees are balanced, not all are. Note that balancing a 
// tree does not mean the left and right subtrees are exactly the same size.
// One way to think about it is that a "balanced" tree really means something more like "not terribly imbalanced:
//  ' It's balanced enough to ensure 0( log n) times for insert and find, but it's not necessarily as 
//  balanced as it could be. 

// A **Balanced Binary Search Tree (Balanced BST)** is a special type of binary search tree (BST) that ensures the tree remains "balanced" or approximately balanced, meaning the height of the tree is kept to a minimum to maintain efficient operations (insertion, deletion, and lookup). This balancing prevents the tree from degenerating into a linear structure like a linked list, where the time complexity of these operations would degrade to O(n).

// ### Key Concepts of a Balanced BST:

// 1. **Binary Search Tree Properties**:
//    - Each node has at most two children (left and right).
//    - For any given node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than or equal to the node's value.

// 2. **Balanced Tree Properties**:
//    - The tree is balanced when the heights of the left and right subtrees of any node differ by no more than a constant factor, often 1.
//    - This balance ensures that the tree’s height remains proportional to `log(n)` where `n` is the number of nodes, resulting in better efficiency (O(log n)) for insertions, deletions, and searches.

// ### Types of Balanced Binary Search Trees:

// 1. **AVL Tree**:
//    - An AVL tree is a self-balancing binary search tree where the height difference (or balance factor) between the left and right subtrees of any node is at most 1.
//    - When this balance factor exceeds 1, rotations (left or right) are performed to restore balance.
//    - Operations like insertion and deletion maintain this balance, ensuring that the tree's height is always O(log n).
   
//    **Example**:
//    ```
//             30                      20
//            /   \       Right        /  \
//          20    40     Rotation    10   30
//         /                          /    \
//       10                        null    40
//    ```

// 2. **Red-Black Tree**:
//    - A red-black tree is another self-balancing binary search tree where nodes are assigned a color (red or black) and balance is maintained using color properties.
//    - The tree follows strict rules (e.g., no two red nodes can be adjacent) to maintain balance, ensuring the height is O(log n).
//    - Rotations and color changes ensure that after insertions or deletions, the tree remains balanced.
   
//    **Key Properties**:
//      - The root is always black.
//      - Every path from the root to a leaf has the same number of black nodes.
//      - Red nodes cannot have red children.
   
//    **Example**:
//    ```
//          40(B)
//         /   \
//      20(R)  60(B)
//      /  \
//    10(B) 30(B)
//    ```

// 3. **Splay Tree**:
//    - A splay tree is a self-adjusting binary search tree where recently accessed elements are moved to the root using tree rotations.
//    - Although not perfectly balanced, splay trees maintain good amortized time complexity of O(log n) for all operations.
   
//    **Key Feature**:
//    - The most recently accessed node is "splayed" to the root through rotations, so frequently accessed elements are quicker to access over time.

// 4. **B-tree** (used for disk storage, databases):
//    - A B-tree is a generalized form of a balanced search tree where nodes can have more than two children. It is widely used in databases and file systems to store large amounts of data in a balanced way.
//    - B-trees minimize the number of disk reads and ensure that insertion, deletion, and search operations all run in O(log n) time.
   
//    **Example**:
//    ```
//        [10, 20, 30]
//       /   |   |    \
//     [0-9][11-19][21-29][31-39]
//    ```

// ### Time Complexity for Balanced BST Operations:
// For all balanced BSTs (AVL, Red-Black, etc.), the time complexity for common operations is as follows:
// - **Search**: O(log n)
// - **Insert**: O(log n)
// - **Delete**: O(log n)

// The balancing mechanism ensures that these complexities remain logarithmic, even in the worst case.

// ### Why Balanced Trees Matter:
// Balanced BSTs are essential in scenarios where data is frequently inserted and searched, such as:
// - **Database indexes** (e.g., B-trees).
// - **Memory management** and **file systems**.
// - **Language parsers** and **search engines**.
// - **Real-time applications** that require efficient data handling.

// In contrast to regular BSTs, balanced BSTs avoid the worst-case performance degradation, keeping operations efficient by ensuring the tree height is kept in check.