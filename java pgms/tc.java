class node{
int value;
node left;
node right;
node(int value){
this.value=value;
left=null;right=null;
}
}
class tree
{
public static void main(String ar[]){
	node root;
root=new node(4);
root.left=new node(30);
System.out.println(root.left.value);
}
}