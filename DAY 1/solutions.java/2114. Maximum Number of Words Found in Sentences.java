class Solution {
    public int mostWordsFound(String[] sentences) {
        int maxcount=0;
        for(String sentence:sentences){
            int words = sentence.split(" ").length;
            maxcount=Math.max(maxcount,words);       }
            return maxcount;
    }   
}