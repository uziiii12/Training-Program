class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x=0;
        for (String opp:operations){
            if (opp.contains("+")){
                x++ ;
            }else{
                x--;
            }
        }return x;
    }
}