import java.util.Collection;
import java.util.LinkedList;

/**
 * @author Zeke Miller
 */
public class Node {

    // fields

    private int data;
    private Collection< Node > children;
    private int cost;


    // constructors

    public Node( int data ) {
        children = new LinkedList<>();
        this.data = data;
        cost = -1;
    }


    // accessors

    public Collection< Node > getChildren() {
        return children;
    }

    public int getCost() {
        return cost;
    }

    public int getData() {
        return data;
    }

    // mutators

    public void addChild( Node child ) {
        children.add( child );
    }

    public void setCost( int cost ) {
        this.cost = cost;
    }


}
