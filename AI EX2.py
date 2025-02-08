{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "e40b40ff-a26c-45e2-b4be-aa32efb7703e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number of queens\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Solution exists. Placements of queens:\n",
      "[1, 0, 0, 0, 0, 0, 0, 0]\n",
      "[0, 0, 0, 0, 1, 0, 0, 0]\n",
      "[0, 0, 0, 0, 0, 0, 0, 1]\n",
      "[0, 0, 0, 0, 0, 1, 0, 0]\n",
      "[0, 0, 1, 0, 0, 0, 0, 0]\n",
      "[0, 0, 0, 0, 0, 0, 1, 0]\n",
      "[0, 1, 0, 0, 0, 0, 0, 0]\n",
      "[0, 0, 0, 1, 0, 0, 0, 0]\n"
     ]
    }
   ],
   "source": [
    "print(\"Enter the number of queens\")\n",
    "N = int(input())\n",
    "\n",
    "# Create a chessboard NxN matrix with all elements set to 0\n",
    "board = [[0] * N for _ in range(N)]\n",
    "\n",
    "def is_safe(i, j):\n",
    "    \"\"\"Check if placing a queen at board[i][j] is safe.\"\"\"\n",
    "    # Checking vertically and horizontally\n",
    "    for k in range(N):\n",
    "        if board[i][k] == 1 or board[k][j] == 1:\n",
    "            return False\n",
    "\n",
    "    # Checking diagonally\n",
    "    for k in range(N):\n",
    "        for l in range(N):\n",
    "            if (k + l == i + j or k - l == i - j) and board[k][l] == 1:\n",
    "                return False\n",
    "                \n",
    "    return True\n",
    "\n",
    "def solve_n_queens(n):\n",
    "    \"\"\"Recursive function to solve N-Queens problem using backtracking.\"\"\"\n",
    "    if n == 0:\n",
    "        return True\n",
    "\n",
    "    for i in range(N):\n",
    "        for j in range(N):\n",
    "            if not is_safe(i, j):\n",
    "                continue\n",
    "\n",
    "            if board[i][j] != 1:\n",
    "                board[i][j] = 1\n",
    "\n",
    "                if solve_n_queens(n - 1):\n",
    "                    return True\n",
    "\n",
    "                board[i][j] = 0  # Backtrack\n",
    "\n",
    "    return False\n",
    "\n",
    "# Check if a solution exists\n",
    "if solve_n_queens(N):\n",
    "    print(\"Solution exists. Placements of queens:\")\n",
    "    for row in board:\n",
    "        print(row)\n",
    "else:\n",
    "    print(\"No solution exists.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ab69d162-56b2-4988-96c4-0dd37d8e729b",
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
