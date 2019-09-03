import java.util.Scanner;

class BiNode {
    private String data = "";
    private BiNode lchild;
    private BiNode rchild;
    
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public BiNode getLchild() {
        return lchild;
    }

    public void setLchild(BiNode lchild) {
        this.lchild = lchild;
    }

    public BiNode getRchild() {
        return rchild;
    }

    public void setRchild(BiNode rchild) {
        this.rchild = rchild;
    }

    public BiNode(String data, BiNode lchild, BiNode rchild) {
        this.data = data;
        this.lchild = lchild;
        this.rchild = rchild;
    }

    public BiNode() {
    }

    
}
public class BinaryTree {
    private BiNode root;

    /**
     * first order traverse the tree
     * @param biTree An empty biTree
     * 
     */
    public static void createBiTree(BiNode biNode) {
        // read a tree node
        Scanner sc = new Scanner(System.in);
        String data = sc.nextLine();
        // System.out.println(data);
        
        if(data.equals("#")) {
            biNode = null;
        } else {
            // biNode is empty need to instantiate one
            biNode.setData(data);
            BiNode lnode = new BiNode();
            biNode.setLchild(lnode);
            createBiTree(biNode.getLchild());
            BiNode rnode = new BiNode();
            biNode.setRchild(rnode);
            createBiTree(biNode.getRchild());
        }
        // no need to close
        // sc.close();

    }

    /**
     * In order traverse the whole tree
     * @param biTree 
     */
    public void inOrderTraverse(BiNode biNode) {
        if (biNode != null) {
            inOrderTraverse(biNode.getLchild());
            System.out.print(biNode.getData());
            inOrderTraverse(biNode.getRchild());
        }
    }

    // main entrance
    public static void main(String[] args) {
        BinaryTree biTree = new BinaryTree();
        BiNode root = new BiNode();
        biTree.setRoot(root);
        BinaryTree.createBiTree(biTree.getRoot());
        // in order outputa
        System.out.println("in order traverse:");
        biTree.inOrderTraverse(biTree.getRoot());
    }

    public BiNode getRoot() {
        return root;
    }

    public void setRoot(BiNode root) {
        this.root = root;
    }

    public BinaryTree() {

    }

    public BinaryTree(BiNode root) {
        this.root = root;
    }
}