#include<iostream>
using namespace std;
int main(){
    int m, n;
    cin >> m >> n;
    int* col = new int [m];
    for(int i = 0; i < m; i++){
        col[i] = 0;
    }
    int count(int* col, int m, int n, int i);
    int sum = count(col, m, n, 0);
    cout << sum << endl;
    return 0;
}
int count(int* col, int m, int n, int i){
    if(i >= m){
        return 0;
    }
    if(i != 0 && col[i-1] <= col[i]){
        return 0;
    }
    if(col[i] == n){
        return 0;
    }
    col[i]++;
    // cout << "当前第一行情况为：" << col[0] << ",";
    // cout << "当前第二行情况为：" << col[1] << endl;
    if(col[m-1] == n){
        col[i]--;
        // cout << "到达回溯" << endl;
        // cout << "当前第一行情况为：" << col[0] << ",";
        // cout << "当前第二行情况为：" << col[1] << endl;
        return 1;
    }
    int sum = 0;
    for(int j = 0; j < m; j++){
        sum += count(col, m, n, j);
    }
    col[i]--;
    // cout << "回溯" << endl;
    // cout << "当前第一行情况为：" << col[0] << ",";
    // cout << "当前第二行情况为：" << col[1] << endl;
    return sum;
}