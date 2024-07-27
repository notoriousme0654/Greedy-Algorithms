//Shop in a Candy store

class Solution{
    static ArrayList<Integer> candyStore(int candies[],int N,int K){
        // code here
        
        ArrayList<Integer> res=new ArrayList<>();
        if(K==0){
            int x=0;
            for(int i:candies){
                x+=i;
            }
            res.add(x);
            res.add(x);
            return res;
        }
        PriorityQueue<Integer> p=new PriorityQueue<>();
        for(int i:candies){
            p.add(i);
        }
        ArrayList<Integer> inc=new ArrayList<>();
        while(p.size()>0){
            inc.add(p.poll());
        }
        int i=0;
        int j=inc.size()-1;
        int min=0;
        while(i<=j){
            min+=inc.get(i);
            j-=K;
            i++;
            }
        res.add(min);
        
        Collections.reverse(inc);
        int l=0;
        int m=inc.size()-1;
        int max=0;
        while(l<=m){
            max+=inc.get(l);
            m-=K;
            l++;
            }
        res.add(max);
        return res;
        
    }
}
