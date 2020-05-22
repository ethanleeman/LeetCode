class Solution {
    public void rotate(int[][] matrix) {
        for(int i = 0; i < (matrix[0].length+1)/2; i++) {
            for(int j = 0; j < (matrix[0].length)/2; j++) {
                int mem = matrix[i][j];
                matrix[i][j] = matrix[matrix[0].length-j-1][i];
                matrix[matrix[0].length-j-1][i] = matrix[matrix[0].length-i-1][matrix[0].length-j-1];
                matrix[matrix[0].length-i-1][matrix[0].length-j-1] = matrix[j][matrix[0].length-i-1];
                matrix[j][matrix[0].length-i-1] = mem;
            }
        }
    }
}
