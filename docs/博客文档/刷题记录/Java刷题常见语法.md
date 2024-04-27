# 基础
## 输入输出
``` Java
Scanner in=new Scann(System.in);
int n=in.nextInt();//读取单个字符；
String s=in.nextLine();//读取整行输入；
//优化：
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String n=inBufferedReader.readLine();
```
## StringBuilder
```Java
StringBuilder stringBuilder = new StringBuilder();
stringBuilder.setCharAt(0, 's');
```
## 类型转换
```Java
//Stinrg类型转换成int；其他同理
Integer.valueOf(string);
Integer.parseInt(string);
```
## list转换为int数组
```Java
List<int[]> list = new ArrayList<>();
list.toArray(new int[list.size()][2])
 List<Integer> temp =new ArrayList();
        temp.add(0, 12);
        temp.add(0, 122);
```
## ArrayList方法
``` Java
List<Integer> res=new ArrayList();
res.clear();//清空元素内容。
Collections.reverse(res) //将动态数组元素内容逆序。
```
## 最大值最小值
```Java
Long同理
max = Integer.MAX_VALUE;
min = Integer.MIN_VALUE;
```
## String
```Java
String s="xxxx";
char[]ch=s.toCharArray(); 
s.substring(i,j);//截取下标从i到j-1;
s.length();
数组的话是 num.length;
char s1= s.charAt(i)  
s.charAt(i) ;//第i个字符。
String[]ss=s.split("regex");
 
 String path = "//aaaa/b";
 String[] paths = path.split("/+"); //匹配多个/ 使用split分开会生成多余的空格。

```

# 集合
## HashMap
``` Java
//HashMap
Map<String,String> map = new HashMap<>();
map.put("key","value");
map.getOrDefault("key","default");//if(map.containsKey("key")) return "value" else return "default"
map.get("key"); 
map.containsKey("key");//是否包含指定key；
map.putIfAbsent("key","value"); //存在当前key,就用当前key对应的value;否则使用参数中的value；
//集合遍历
//推荐
for(Map.Entry<String,String> entry : map.entrySet()){
    entry.getKey();
    entry.getValue();
} 
 // 推荐
map.forEach((k, v) -> System.out.println(k + " : " + (v + 10))); 
// for
Map<Integer, Integer> map = new HashMap<Integer, Integer>();
for (Integer key : map.keySet()) {
    Integer value = map.get(key);
    System.out.println("Key = " + key + ", Value = " + value);
  }
// 使用Iterator迭代器
        Iterator hmIterator = map.entrySet().iterator(); 

  while (hmIterator.hasNext()) { 
            Map.Entry mapElement = (Map.Entry)hmIterator.next(); 
            int marks = ((int)mapElement.getValue() + 10); 
            System.out.println(mapElement.getKey() + " : " + marks); 
        } 

map.getOrDefault(k,defaultValue); 没有k值，设置为默认值。有k值，获取k值。简化操作。否则。我们需要 用if else去实现。
```
## 队列&栈
``` Java
Queue<Integer> q = new LinkedList<>(); 
 q.peek();
 q.poll();
 q.size();
 q.poll()当没有队列元素；出队会返回null;
    //优先级遍历
PriorityQueue pQueue = new PriorityQueue(); 
Iterator itr = pQueue.iterator(); 
while (itr.hasNext()) 
    System.out.println(itr.next()); 



Deque stack= new LinkedList(); //使用这个替代之前的Stack
stack.push();
stack.pop();
stack.peek();
stack.size();
```
## 按照指定位置排序
