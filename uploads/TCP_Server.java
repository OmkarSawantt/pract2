import java.io.*;
import java.net.*;
public class TCP_Server {
public static void main(String[] args) {
try {
int port =5555 ;
ServerSocket ss=new ServerSocket (port);
System.out.println("Waiting for connection");
Socket s= ss.accept();
System.out.println("Connection is done...");

BufferedReader br = new BufferedReader(new InputStreamReader(s.getInputStream()));
int num = Integer.parseInt(br.readLine());
System.out.println("Request From client =" + num);
int f = 1;
for(int i=1;i<=num;i++)
{
f= f * i;
}
PrintWriter pw = new PrintWriter(new OutputStreamWriter(s.getOutputStream()));
pw.println(f);
pw.flush();
}
catch (Exception e)
{
System.out.println("Error : " + e);
}
}}
