# Lab 6: Security Modelling and Analysis

Security Modelling and Analysis is a critical component of cybersecurity, enabling organizations to identify, assess, and prioritise risks to their information systems. This lab will cover attack trees to better understand security modelling and analysis approaches.

## 5.1. Attack Trees

Attack Trees are a graphical representation of potential attacks on a system. They help in understanding the various ways an attacker can compromise a system and the steps involved in each attack.

### 5.1.1. Attack Tree Implementation

We will custom build the attack tree from scratch. The attack tree will be a simple tree structure where each node represents a potential attack or sub-attack. We need to create a class for the attack tree and implement methods to add children, remove children, and print the tree. The skeleton code is provided below.

```python
DEPTH = 4

class AttackTreeNode:
    def __init__(self, name):
        self.name = name
        self.AND_children = []
        self.OR_children = []

    def add_AND_child(self, child_node):
        self.AND_children.append(child_node)
    
    def add_OR_child(self, child_node):
        self.OR_children.append(child_node)

    def remove_AND_child(self, child_node):
        self.AND_children.remove(child_node)

    def remove_OR_child(self, child_node):
        self.OR_children.remove(child_node)

    def print_tree(self, type=None, is_start=True, level=0, and_type=0, or_type= 0):

        if is_start:
            if type == "AND" and (and_type > 1):
                print(" " * level + "AND" + " " * (DEPTH-3), end="")    
            elif type == "OR" and (or_type > 1):
                print(" " * level + "OR" + " " * (DEPTH-2), end="")
            else:
                print(" " * DEPTH + " " * level, end="") 
        else:
            print(" " * DEPTH + " " * level, end="") 
        print(self.name)

        child_start = True
        for child in self.AND_children:
            # print(is_start)
            child.print_tree("AND", child_start, level + DEPTH, len(self.AND_children), len(self.OR_children))
            child_start = False
        for child in self.OR_children:
            # print(is_start)
            child.print_tree("OR", child_start, level + DEPTH, len(self.AND_children), len(self.OR_children))
            child_start = False

```

You can use the following code to test that it is working. It should print the attack tree in indented format the same as the one in the lectures.

```python
if __name__ == "__main__":
    root1 = AttackTreeNode("1. Adversary gains access to PI")
    
    child11 = AttackTreeNode("1.1 Gain access to DB")
    child12 = AttackTreeNode("1.2 Login as target user")
    child13 = AttackTreeNode("1.3 Hijack user session")
    child14 = AttackTreeNode("1.4 Passively intercept data")
    
    child111 = AttackTreeNode("1.1.1 Exploit sys app or kernel")

    child121 = AttackTreeNode("1.2.1 Bruteforce")

    child1211 = AttackTreeNode("1.2.1.1 username")
    child1212 = AttackTreeNode("1.2.1.2 password")

    child122 = AttackTreeNode("1.2.2 Steal credentials")

    child131 = AttackTreeNode("1.3.1 steal user session cookie")

    child141 = AttackTreeNode("1.4.1 identify user connection initiation")
    child142 = AttackTreeNode("1.4.2 sniff network traffic")

    root1.add_OR_child(child11)
    root1.add_OR_child(child12)
    root1.add_OR_child(child13)
    root1.add_OR_child(child14)
    
    child11.add_AND_child(child111)

    child12.add_AND_child(child121)
    child12.add_AND_child(child122)

    child121.add_OR_child(child1211)
    child121.add_OR_child(child1212)

    child13.add_OR_child(child131)

    child14.add_AND_child(child141)
    child14.add_AND_child(child142)
    
    root1.print_tree()
```

#### TASK 1

Now for the code, add the fields to assign metric values. Replicate the metrics used in the lecture slides (i.e., possibility and cost). The metric values are assigned to each leaf node in the tree. The intermediate nodes will need to use leaf node values to calculate the metric for themselves, all the way to the root as explained in the lectures. Once completed, test the code to see if you get the same result as in class or not.

#### TASK 2

Let's construct the attack tree for another attack scenario.\
You are evaluating the security of a web application. The application has a login page, a registration page, and a password reset page. The application uses HTTPS for secure communication. The application is hosted on a cloud server. The application has a database that stores user information. You may draw a diagram to better understand the scenario.

1. Create the attack tree for the above scenario. The root node should be "Web Application Exploited". Conduct research and come up with at least 4 children nodes to the root. Expand the children nodes appropriately, such that your attack tree has at least 3 levels, but no more than 4 levels.
2. Implement a new metric, probability of attack success, to your attack tree implementation. The probability is calculated in the following way:
   * if the gate is AND, you multiply them all together.
   * if the gate is OR, you have to use the equation (1 - (1 - p1) \* (1 - p2) \* ... \* (1 - pn)), where p is the probability of each child node.
3. For the purpose of the lab, we'll assign arbitrary values to the metrics. For example, the cost of the attack is 100 and the likelihood is 0.5. You can assign different values to different nodes, but make sure that the values are reasonable.
4. Run the code to see the output. Change some values to see how the output changes.

### 5.1.2. Security Optimization

The attack tree can be used to identify the most critical vulnerabilities in the system. By analyzing the tree, we can determine which attacks are most likely to succeed and which ones would have the most significant impact. This information can be used to prioritize security measures and allocate resources effectively.

Imagine yourself as a security operator. Your are to improve the security of your system from Task 2 above. You have enough resources to implement one security feature that will mitigate one attack from your design from Task 2. Which one would you choose and why?

To do this, you can try the exhaustive search method - try to remove the metric value of each leaf node in the attack tree to see how the output value changes. One that gives the most improvement is the one you should choose.

#### TASK 3

Implement the exhaustive search algorithm to find optimal solution in your attack tree.

### 5.1.3. Evaluating larger trees

The one we generated above are simple to visualise and solve. However, in practice, these trees tend to get very large. Let us simulate this by implementing a random attack tree generator. The generator will create a tree with a given number of nodes and a given depth. The nodes will be randomly generated and the tree will be randomly generated as well. The generator will also assign random metric values to the nodes.

Once done, try to run your exhaustive search algorithm on the generated tree. What do you observe? Why? You should try to evaluate the efficiency of your algorithm to better understand why you observe such behaviour. You can use the time module to measure the time taken to run your algorithm. You can also use the random module to generate random numbers.

#### TASK 4 (Optional) Efficient Optimisation

This is an optional task.

Try to come up with an efficient algorithm to solve the problem. You can use any algorithm you like, but you need to justify why your algorithm is efficient. You can also use any data structure you like, but you need to justify why your data structure is efficient. You can also use any programming language you like, but you need to justify why your programming language is efficient.

You can see that cybersecurity involves not only security, but also programming and algorithms. This is a good example of how cybersecurity is a multidisciplinary field. You can also see that cybersecurity is not just about finding vulnerabilities, but also about finding solutions to the problems. This is a good example of how cybersecurity is a problem-solving field.

### 5.2. Conclusion

In this lab, we have learned about attack trees and how to implement them. We have also learned about security optimization and how to evaluate larger trees. We have also learned about the importance of algorithms and data structures in cybersecurity. This lab has given us a good understanding of how to approach security problems and how to solve them.

{% hint style="info" %}
This is the last lab! Please remember to complete your portfolio and the project, and revise completed labs for the upcoming lab quiz.
{% endhint %}
