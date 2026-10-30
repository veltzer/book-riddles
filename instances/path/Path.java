import java.util.Vector;
import java.util.Random;


public class Path {
	
	static Random rnd=new Random();
	static boolean debug=false;
	
	static Vector<Integer> createPath(int min,int max,int from,int to,int steps,float zero_factor) {
		assert steps>=abs(to-from);
		assert steps>0;
		Vector<Integer> v=new Vector<Integer>();
		int sign=sign(to-from);
		int climb=abs(to-from);
		// fill out the climbing code
		for(int i=0;i<climb;i++) {
			v.add(Integer.valueOf(sign));
		}
		int left=steps-climb;
		float zero=(float)left*zero_factor;
		// fill out zeroes according to the zero factor
		int izero=(int)zero;
		for(int i=0;i<izero;i++) {
			v.add(Integer.valueOf(0));
		}
		left-=izero;
		// make sure that we have an even number left
		if(left%2==1) {
			v.add(Integer.valueOf(0));
			left--;
		}
		// fill out the junk +1/-1 fillout
		for(int i=0;i<left;i+=2) {
			v.add(Integer.valueOf(+1));
			v.add(Integer.valueOf(-1));
		}
		// scramble the vector
		scramble(v);
		// make sure that we do not pass the limits
		int current=from;
		for(int i=0;i<v.size();i++) {
			int newpos=current+v.get(i);
			if(newpos>=max) {
				int pos=find(v,-1,i);
				swap(v,i,pos);
				newpos=current+v.get(i);
			}
			if(newpos<min) {
				int pos=find(v,+1,i);
				swap(v,i,pos);
				newpos=current+v.get(i);
			}
			current=newpos;
		}
		if(debug) {
			System.out.println("debug v is");
			System.out.println(v.toString());
		}
		
		Vector<Integer> path=new Vector<Integer>();
		path.add(Integer.valueOf(from));
		int curr=from;
		for(int i=0;i<v.size();i++) {
			curr+=v.get(i);
			path.add(Integer.valueOf(curr));
			if(debug) {
				System.out.println("adding "+v.get(i));
				System.out.println("curr is "+curr);
			}
		}
		return(path);
	}
	
	private static int find(Vector<Integer> v,int what,int pos) {
		for(int i=pos;i<v.size();i++) {
			if(v.get(i)==what) return(i);
		}
		assert false;
		return(-1);
	}
	
	private static void scramble(Vector<Integer> v) {
		for(int i=0;i<100;i++) {
			int a,b;	
			do {
				a=rnd.nextInt(v.size());
				b=rnd.nextInt(v.size());
			} while(a==b);
			swap(v,a,b);
		}
	}
	
	private static void swap(Vector<Integer> v,int a,int b) {
		assert a>=0;
		assert b>=0;
		assert a<v.size();
		assert b<v.size();
		Integer tmp=v.get(a);
		v.set(a,v.get(b));
		v.set(b,tmp);
	}

	private static int sign(int i) {
		if(i<0) return -1;
		else return 1;
	}
	
	private static int abs(int i) {
		if(i<0) return -i;
		else return i;
	}
	

	static Vector<Point> createPath2d(Point min,Point max,Point from,Point to,int steps,float zero_factor) {
		Vector<Integer> pathx=createPath(min.getX(),max.getX(),from.getX(),to.getX(),steps,zero_factor);
		Vector<Integer> pathy=createPath(min.getY(),max.getY(),from.getY(),to.getY(),steps,zero_factor);
		Vector<Point> ret=new Vector<Point>();
		for(int i=0;i<steps+1;i++) {
			Point p=new Point(pathx.get(i),pathy.get(i));
			ret.add(p);
		}
		return(ret);
	}
	

	public static void main(String[] args) {
		Vector<Integer> path1d=createPath(0,10,3,7,40,0.2f);
		System.out.println("1d path is");
		System.out.println(path1d.toString());
		
		Point min=new Point(0,0);
		Point max=new Point(7,7);
		Point from=new Point(0,6);
		Point to=new Point(6,0);
		
		Vector<Point> path2d=createPath2d(min,max,from,to,10,0.2f);
		System.out.println("2d path is");
		System.out.println(path2d.toString());

	}

}
