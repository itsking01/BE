#include <iostream>
#include <vector>

using namespace std;

bool isSafe(vector<vector<int>>& board, int row, int col, int n) {
    for (int x = col; x >= 0; x--) {
        if (board[row][x] == 1) {
            return false;
        }
    }

    int i = row;
    int j = col;

    while (i >= 0 && j >= 0) {
        if (board[i][j] == 1) {
            return false;
        }

        i--;
        j--;
    }

    i = row;
    j = col;

    while (i < n && j >= 0) {
        if (board[i][j] == 1) {
            return false;
        }

        i++;
        j--;
    }

    return true;
}

bool nQueens(vector<vector<int>>& board, int col, int n) {
    if (col >= n) {
        return true;
    }

    for (int i = 0; i < n; i++) {
        if (isSafe(board, i, col, n)) {
            board[i][col] = 1;
            if (nQueens(board, col + 1, n)) {
                return true;
            }
            board[i][col] = 0;
        }
    }

    return false;
}

int main() {
    int n;
    cout << "Enter the size of the board: ";
    cin >> n;

    vector<vector<int>> board(n, vector<int>(n, 0));

    if (nQueens(board, 0, n)) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "Not possible" << endl;
    }

    return 0;
}
