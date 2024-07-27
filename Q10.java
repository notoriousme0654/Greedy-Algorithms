//N meetings in one room

class Solution 
{
   
    public static int maxMeetings(int start[], int end[], int n)
    {
      PriorityQueue<Node> pq=new PriorityQueue<Node>((a,b)->a.end-b.end);
      for(int i=0;i<n;i++){
          pq.add(new Node(start[i],end[i]));
      }
      int count=1;
      int prev=pq.poll().end;
      while(pq.size()>0){
          Node curr=pq.poll();
      
          if(curr.start>prev){
              count++;
              prev=curr.end;
          }
          
      }
      return count;
    }
    static class Node{
        int start;
        int end;
        Node(int start,int end){
            this.start=start;
            this.end=end;
        }
    }
}
