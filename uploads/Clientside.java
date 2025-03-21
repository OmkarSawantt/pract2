import java.io.*;
import java.net.*;
public class Clientside {
public static void main(String[] args) {
try {
int port = 5555;
InetAddress addr = InetAddress.getLocalHost();
Socket s = new Socket(addr,port);
System.out.println("Connection is done ...");
BufferedReader br1 = new BufferedReader(new InputStreamReader(System.in));

PrintWriter pw = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
pw.flush();
}
catch (Exception e)
{
System.out.println("Error : " + e);
}
}
}
