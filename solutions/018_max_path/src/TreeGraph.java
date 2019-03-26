import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

import java.lang.Math;

public class TreeGraph {

    private Map< Location, Node > map;
    private int rows;

    public TreeGraph( String filename ) {

        map = new HashMap<>();

        Scanner in;
        try {
            in = new Scanner( new File( filename ) );
        }
        catch ( FileNotFoundException fnf ) {
            fnf.printStackTrace();
            return;
        }

        String line;
        String[] arr;
        int i;
        for ( i = 0 ; in.hasNextLine() ; i++ ) {
            line = in.nextLine();
            // System.out.println(line);
            arr = line.split( " " );
            if ( arr.length != i + 1 ) {
                System.exit( 1 );
            }
            for ( int ind = 0 ; ind < arr.length ; ind++ ) {
                map.put( new Location( i, ind ), new Node( Integer.parseInt(
                        arr[ ind ] ) ) );
            }
        }
        rows = i;

        for ( int row = 0 ; row < rows - 1 ; row++ ) {
            for ( int col = 0 ; col <= row ; col++ ) {
                Node node = map.get( new Location( row, col ) );
                Node child1 = map.get( new Location( row + 1, col ) );
                Node child2 = map.get( new Location( row + 1, col + 1 ) );
                node.addChild( child1 );
                node.addChild( child2 );
            }
        }
    }


    public Node getNode( Location loc ) {
        return map.get( loc );
    }


    public int findLongestPath( Node start ) {
        start.setCost( start.getData() );
        return findLongestRec( start, start.getCost() );

    }

    private int findLongestRec( Node curr, int max ) {
        Collection< Node > children = curr.getChildren();
        int newMax = max;
        for ( Node child : children ) {
            child.setCost( Math.max( curr.getCost() + child.getData(), child
                    .getCost() ) );
            if ( child.getCost() > curr.getCost() + child.getData() ) {
                continue;
            }
            newMax = Math.max( child.getCost(), findLongestRec( child, newMax ) );
        }
        return newMax;
    }

    public static void main(String[] args) {

        TreeGraph treeGraph = new TreeGraph( args[0] );
        int max = treeGraph.findLongestPath( treeGraph.map.get(
                new Location( 0, 0 ) ) );
        System.out.println( max );
    }
}
