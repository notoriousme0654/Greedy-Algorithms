// 15. Job Sequencing Problem

class Solution{
    private :
    static bool  cmp(Job a, Job b){
        return (a.profit > b.profit);
    }
    
    public:
    vector<int> JobScheduling(Job arr[], int n) 
    {
        sort(arr, arr + n, cmp);
        bool temp[n]={false};
        int noOfJOb=0,maxProfit=0;
        vector<int> result;
        for(int i=0;i<n;i++){
            for(int j=min(n,arr[i].dead)-1;j>=0;j--){
                if(temp[j] == false){
                    noOfJOb++;
                    temp[j]=true;
                    maxProfit += arr[i].profit;
                    break;
                }
            }
        }
        return {noOfJOb, maxProfit};
    } 
};
