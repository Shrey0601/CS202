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
int power(int a,int b) {int res=1;a%=INF; assert(b>=0); for(;b;b>>=1){if(b&1)res=res*a%INF;a=a*a%INF;}return res;}

void c_p_c()
{
  ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);

}

mii m1;

int dpll(vvi cnf,mii m){

    while(1){
        int flag=0;
        vi v;
        for(auto clause: cnf){
          if(clause.size()==1){
            v=clause;
            flag=1;
            break;
          }
        }
        
        if(flag==0){
            break;
        }
        
        int unilit = v[0];

        for(auto it: m){
            if(it.ff == -1*unilit){
                return false;
            }
        }
 
        m[unilit] = 1;

        auto it = cnf.begin();

        for(auto clause: cnf){
            for(auto lit: clause){
              if(lit==unilit){
                  cnf.erase(it);
              }
              else if(lit==(unilit*(-1))){
                  clause.erase(find(all(clause),-unilit));
                  *it=clause;
              }
            }
            it++;
        }
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

    if(dpll(cnfp,m)){
        return 1;
    }
    else if(dpll(cnfn,m)){
        return 1;
    }
    else{
        return 0;
    }
}


int32_t main(){
    vi v;
    v.pb(1);
    v.pb(2);
    vvi claus;
    claus.pb(v);
    v.clear();
    v.pb(-1);
    v.pb(-2);
    claus.pb(v);
    v.clear();
    v.pb(1);
    claus.pb(v);
    mii m;
    int z=dpll(claus,m);
    if(z){
        cout<<"SAT\n";
    }
    else{
        cout<<"UNSAT";
        return 0;
    }
    for(int i=1;i<=3;i++){
        if(m1.find(i)==m1.end())
            cout<<-i<<' ';
        else
            cout<<i<<' ';
    }
    return 0;
}
