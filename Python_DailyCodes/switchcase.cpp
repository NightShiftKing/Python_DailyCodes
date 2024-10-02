#include<iostream>
using namespace std;

int main(){
    
    char name = 'g';
    //cout << "enter a letter for a name" << endl;
    //cin >> name; 

    switch (name)
    {
    case 'a':
        cout << "hello" << endl;
        break;    
    case 'b':
        cout << "bye" << endl;
        break;
    }


    int room;
    cout << "enter a room number" << endl;
    cin >> room;
    char answer;  

    while(true){

    
    switch (room)
    {
    case 1 :
    cout << "you are in room one. can go east" << endl; 
    cin >> answer;
    if(answer == 'e')
        room = 2;
        break;
    case 2 :
    cout << "you are in room two. can go west and south" << endl; 
        break;
    case 3 :
    cout << "you are in room three. can go north and east" << endl; 
        break;
    case 4 :
    cout << "you are in room four. can go west and south" << endl; 
        break;

    default:
        cout << "you are in room idk" << endl; 
        break;
    }

    }


}