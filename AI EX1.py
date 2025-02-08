{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "6ed9804a-e5e6-486a-8383-4820a4686ede",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n"
     ]
    }
   ],
   "source": [
    "class Solution:\n",
    "    def solve(self, board):\n",
    "        visited = {}\n",
    "        flatten = []\n",
    "        for i in range(len(board)):\n",
    "            flatten += board[i]\n",
    "        flatten = tuple(flatten)  # Move tuple conversion outside loop\n",
    "        visited[flatten] = 0\n",
    "\n",
    "        if flatten == (0, 1, 2, 3, 4, 5, 6, 7, 8):\n",
    "            return 0\n",
    "        return self.get_paths(visited)\n",
    "\n",
    "    def get_paths(self, visited):\n",
    "        cnt = 0\n",
    "        while True:\n",
    "            current_nodes = [x for x in visited if visited[x] == cnt]\n",
    "            if len(current_nodes) == 0:  # Fix indentation\n",
    "                return -1\n",
    "\n",
    "            for node in current_nodes:\n",
    "                next_moves = self.find_next(node)\n",
    "                for move in next_moves:\n",
    "                    if move not in visited:\n",
    "                        visited[move] = cnt + 1\n",
    "                        if move == (0, 1, 2, 3, 4, 5, 6, 7, 8):\n",
    "                            return cnt + 1\n",
    "            cnt += 1  # Increment only once per level\n",
    "\n",
    "    def find_next(self, node):\n",
    "        moves = {\n",
    "            0: [1, 3],\n",
    "            1: [0, 2, 4],\n",
    "            2: [1, 5],\n",
    "            3: [0, 4, 6],\n",
    "            4: [1, 3, 5, 7],\n",
    "            5: [2, 4, 8],\n",
    "            6: [3, 7],\n",
    "            7: [4, 6, 8],\n",
    "            8: [5, 7],\n",
    "        }\n",
    "        results = []\n",
    "        pos_0 = node.index(0)\n",
    "\n",
    "        for move in moves[pos_0]:    \n",
    "            new_node = list(node)\n",
    "            new_node[move], new_node[pos_0] = new_node[pos_0], new_node[move]  # Fix swap\n",
    "            results.append(tuple(new_node))\n",
    "        \n",
    "        return results\n",
    "\n",
    "# Example usage\n",
    "ob = Solution()\n",
    "matrix = [\n",
    "    [3, 1, 2],\n",
    "    [4, 7, 5],\n",
    "    [6, 8, 0]\n",
    "]\n",
    "print(ob.solve(matrix))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00376efe-7e66-49bf-a9e7-7f371b6ab129",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b110e58-68e1-4264-8c0f-a2ea35d58266",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
