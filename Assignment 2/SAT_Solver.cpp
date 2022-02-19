#include<bits/stdc++.h>
using namespace std;
       
#define ff              first
#define ss              second
#define int             long long
#define float           double
#define pb              push_back
#define mp              make_pair
#define pii             pair<int,int>
#define vi              vector<int>
#define vvi             vector<vector<int>>
#define mii             map<int,int>
#define pqb             priority_queue<int>
#define pqs             priority_queue<int,vi,greater<int> >
#define setbits(x)      __builtin_popcountll(x)
#define zrobits(x)      __builtin_ctzll(x)
#define mod             1000000007
#define inf             1e18
#define ps(x,y)         fixed<<setprecision(y)<<x
#define mk(arr,n,type)  type *arr=new type[n];

#define w(x)            int x; cin>>x; while(x--)
mt19937                 rng(chrono::steady_clock::now().time_since_epoch().count());
#define pi 3.1415926536;
#define fi(i,n)         for(int i=0;i<n;++i)
#define fe(i,n)         for(int i=n-1;i>=0;--i)
#define ld              long double
#define all(c)            c.begin(), c.end()
#define max_val(c)      * max_element(all(c));
#define max_index(c)       max_element(all(c))-c.begin();
#define min_val(c)      * min_element(all(c))  
#define min_index(c)       min_element(all(c))-c.begin();
#define mod            1000000007

const ld PI = acos(-1);
const ld EPS = 1e-9;
const int INF = 1e18;
const int MAX_LEN =  100000;
int power(int a,int b) {int res=1;a%=INF; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%INF;a=a*a%INF;}return res;}

void c_p_c()
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

}


mii m1;

vi singleton(vvi cnf){
    for(auto clause :cnf){
        if(clause.size()==1)
            return clause;
    }
    vi v;
    v.pb(0);
    return v;
}
int sat_solver(vvi cnf,mii m){
    vi s=singleton(cnf);
    while(s[0]!=0){

        int unilit=s[0];

        m[unilit] = 1;

        for(auto it: m){
            if(it.ff == -1*unilit){
                return 0;
            }
        }

        auto it=cnf.begin();
        for(auto i:cnf){
            if(find(all(i),unilit)!= i.end()){
                cnf.erase(it);
            }
            else if(find(all(i),-unilit)!= i.end()){
                i.erase(find(all(i),-unilit));
                *it=i;
            }
            it++;
        }  
        s=singleton(cnf);     
    }

    for(auto clause :cnf){
        if(!clause.size())
            return 0;
    }

    if(!cnf.size()){
        m1 = m;
        return 1;
    }

    vector<vector<int>> cnfp=cnf,cnfn=cnf;      

    vi v,v1;

    v.pb(*((*cnf.begin()).begin()));
    cnfp.pb(v);

    v1.pb(-1*(*((*cnf.begin()).begin())));
    cnfn.pb(v1);

    if(sat_solver(cnfp,m)){
        return 1;
    }
    else if(sat_solver(cnfn,m)){
        return 1;
    }
    else{
        return 0;
    }
}


int32_t main(){
    int clauses, literals, removed;
    vvi claus;
    freopen("tests/TestCase_5_unsat.cnf", "r", stdin);
    char y[MAX_LEN];
    while(1){
        scanf("%[^\n]%*c", y);
        while(y[0]=='c'){
            scanf("%[^\n]%*c", y);
            continue;
        }
        if(y[0]=='p'){
            istringstream stream(y);
            vector<string>y1((istream_iterator<string>(stream)),istream_iterator<string>());
            clauses=stoi(y1[3]);
            literals=stoi(y1[2]);
        }
        claus.resize(clauses);
        for(int i =0;i< clauses;i++){
            scanf("%[^\n]%*c", y);
            if(y[0]=='c'){
               i--;
               continue;
            }
            else{
                istringstream stream(y);
                vector<string>y2((istream_iterator<string>(stream)),istream_iterator<string>());
                int n = y2.size();
                for(int j=0;j<n;j++){
                    int prop = stoi(y2[j]);
                    if(prop!=0){
                        claus[i].push_back(prop);   
                    }
                }    
            }     
        }
        break;
    }
    for(int i=0;i<clauses;i++){
        sort(claus[i].begin(),claus[i].end());
    }
    int init_clauses = clauses;
    vvi init_claus = claus;
    clauses=claus.size();
    mii m;
    int z=sat_solver(claus,m);
    if(z){
        cout<<"SAT\n";
    }
    else{
        cout<<"UNSAT";
        return 0;
    }
    for(int i=1;i<=literals;i++){
        if(m1.find(i)==m1.end())
            cout<<-i<<' ';
        else
            cout<<i<<' ';
    }
    return 0;
}