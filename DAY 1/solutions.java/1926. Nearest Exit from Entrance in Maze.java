import java.util.*;

class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {

        int rows = maze.length;
        int cols = maze[0].length;

        Queue<int[]> queue = new LinkedList<>();

        queue.offer(new int[]{
            entrance[0],
            entrance[1],
            0
        });

        maze[entrance[0]][entrance[1]] = '+';

        int[][] directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        while (!queue.isEmpty()) {

            int[] current = queue.poll();

            int r = current[0];
            int c = current[1];
            int steps = current[2];

            for (int[] direction : directions) {

                int nr = r + direction[0];
                int nc = c + direction[1];

                if (nr >= 0 && nr < rows &&
                    nc >= 0 && nc < cols &&
                    maze[nr][nc] == '.') {

                    if (nr == 0 || nr == rows - 1 ||
                        nc == 0 || nc == cols - 1) {

                        return steps + 1;
                    }

                    maze[nr][nc] = '+';

                    queue.offer(new int[]{
                        nr,
                        nc,
                        steps + 1
                    });
                }
            }
        }

        return -1;
    }
}