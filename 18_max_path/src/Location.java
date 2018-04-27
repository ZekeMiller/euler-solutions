/**
 * @author Zeke Miller
 */
public class Location {

    private int row;
    private int col;

    public Location( int row, int col ) {
        this.row = row;
        this.col = col;
    }

    public int getRow() {
        return row;
    }

    public int getCol() {
        return col;
    }

    @Override
    public boolean equals( Object o ) {
        return o instanceof Location && ((Location)o).row == this.row && (
                (Location)o).col == this.col;
    }

    @Override
    public int hashCode() {
        return Integer.hashCode( row ) * Integer.hashCode( col );
    }
}
