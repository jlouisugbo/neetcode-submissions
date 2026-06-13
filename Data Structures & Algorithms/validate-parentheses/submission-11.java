class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        if(s.length() == 1) return false;
        for (int i = 0; i < s.length(); i++){
            char b = s.charAt(i);
            if (b == '(' || b == '{' || b == '['){
                stack.push(b);
                continue;
            }
            if(stack.isEmpty()) return false;
            switch(b){
            case ')':
                if(stack.peek() =='('){
                    stack.pop(); 
                    break;
                } else {
                    return false;
                }
            case '}':
                if(stack.peek() =='{'){
                    stack.pop(); 
                    break;
                } else {
                    return false;
                }
            case ']':
                if(stack.peek() =='['){
                    stack.pop(); 
                    break;
                } else {
                    return false;
                }
            }
        }
        return stack.isEmpty();
        /*
        System.out.println(stack);
        for (int i = 0; i < s.length(); i++){
            char x = s.charAt(i);
            if (stack.contains(x)) continue;
            switch(stack.peek()){
                case '(':
                    if(x ==')') stack.pop(); break;
                case '{':
                    if(x =='}') stack.pop(); break;
                case '[':
                    if(x ==']') stack.pop(); break;
            } 
        }

        return stack.isEmpty();
        /*first add every opening bracket to a stack
        you dont need to return a stack so just keep iterating through
        if the next element in the string is the closing bracket
        just pop that element from the top of the stack
        then after you pop from the top of the stack, check the next eleent
        then return stack.isEmpty;*/
    }
}
