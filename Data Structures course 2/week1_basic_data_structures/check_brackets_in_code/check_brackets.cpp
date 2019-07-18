#include <iostream>
#include <stack>
#include <string>
using namespace std;

struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text; //initialise string
    getline(std::cin, text);

    std::stack <Bracket> opening_brackets_stack;
    int answer;
    for (int position = 0; position < text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            // Process opening bracket, write your code here
            opening_brackets_stack.push(next);
            // if (opening_brackets_stack.pop() == next){
            //     continue
                
            // }else{return }
        }

        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
            if (opening_brackets_stack.empty()){
                answer = 0;
                break;
            }
            if (opening_brackets_stack.top() == next){
                opening_brackets_stack.pop();
                }
                else{
                answer = position ;}
        }
    }

    // Printing answer, write your code here
    if(answer){
        cout<<answer<<endl;
    }
    else{
        cout<<'Success'<<endl;}
    return 0;
}
