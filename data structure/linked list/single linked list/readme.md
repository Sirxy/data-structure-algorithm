single linked list

单向链表引入
- 也叫单链表，是最简单的一种链表形式
- 其每个节点包含两个区域：数据元素区 `element` 、指针链接区 `next`（指向下一个节点的位置，地址）
    
    ```python
    a = 10
    b = 20
    a, b = b, a 
    ```
    上述 python 变量标识的本质是：
    ```
    a存到了10这个数的地址上了
    b存到了20这个数的地址上了
    = ,右边，使用b，
    a, b = 20, 10
    ```
    改变了a和b维护的东西。
    
    ```python
    def func():
        pass
    a = func  # a指向了func，a就是func了
    ```
    
    ```python
    class Node:
        element
        next  # 于是，通过 node1 的 next 指向 node2 来达到指向效果 node1.next = node2
    ```
    
- 其最后一个节点的指针链接去指向一个空值
- `__head` 指向链表头节点的位置，由 `__head` 出发可以找到链表中任意一个节点


单链表和节点的实现：

节点实现

见 `single_linked_list.py` 中 `Node` 类。

单链表ADT模型

见 `single_linked_list.py` 中 `SingleLinkList` 类。


