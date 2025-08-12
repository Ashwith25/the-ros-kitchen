# The ROS Kitchen: A Beginner's Guide to ROS2

This repository contains the source code for "The ROS Kitchen," a blog series designed to teach the fundamentals of ROS2 using a fun restaurant analogy.

-----

## Blog Series 📝

  * **Part 1: A Beginner’s Guide to Nodes, Topics, and Services**
      * [Link](https://medium.com/@pashwith25/welcome-to-the-ros-kitchen-part-1-ee47cfa786a9)
  * **Part 2: A Beginner's Guide to Scaling Your Robot with Parameters and Namespaces**
      * In Writing!
  * **Part 3: Coming Soon\!**

-----

## How to Run This Project 🚀

These instructions will guide you on how to build and run the code for each part of the series.

### 1\. Clone the Repository

First, clone this repository into your ROS2 workspace.

```bash
cd ~/ros2_ws
git clone git@github.com:Ashwith25/the-ros-kitchen.git
```

### 2\. Build the Packages

Navigate to the root of your workspace (e.g., `~/ros2_ws`) and run `colcon build`. This command will build all the packages (`part1`, `part2`, etc.) in this repository.

```bash
cd ~/ros2_ws
colcon build
```

### 3\. Source the Workspace

After the build is complete, you need to source your workspace's setup file so ROS2 can find your new packages.

```bash
source install/setup.bash
```

### 4\. Run the Nodes

You can now run the nodes from each part of the series. Remember to open a new terminal for each `ros2 run` command.

**Example for Part 1 (All in separate terminals):**

```bash
ros2 run part1 waiter

ros2 run part1 chef
```

**Example for Part 2 (All in separate terminals):** 

```bash
ros2 run part2 waiter --ros-args -r __ns:=/italian -p menu_items:="['Lasagna', 'Spaghetti', 'Risotto']"
ros2 run part2 chef --ros-args -r __ns:=/italian

ros2 run part2 waiter --ros-args -r __ns:=/chinese -p menu_items:="['Fried Rice', 'Dumplings', 'Chow Mein']"
ros2 run part2 chef --ros-args -r __ns:=/chinese
```

## Feedback
If you run into any problems or have any questions while following the tutorial, please feel free to create an issue on this repository or add a comment on the blog post. All feedback is welcome!
