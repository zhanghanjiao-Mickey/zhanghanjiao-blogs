# 常用数据结构

---

## List

---

### ArrayList: 数组实现

```java
List<Integer> num = new ArrayList<>();
List<Integer> num = new ArrayList<>(Arrays.asList(a, b, c));
// 添加删除（index）
num.add(index);
num.remove(index);
// 获取修改
num.get(index);
num.set(index, Integer);
// 获取对象下标
num.indexOf(Integer);
num.lastIndexOf(Integer);
// 判断是否有对象&空列表
num.contains(Integer);
num.isEmpty();
```

## Queue: 推荐使用LinkedList初始化

---

```java
Queue<Integer> queue = new LinkedList<>();
// 添加元素到队尾
queue.add(1);
queue.offer(1);
// 取队尾元素并删除
queue.poll();
queue.remove();
// 取队尾元素不删除
queue.peek();
```

## Deque: 推荐使用LinkedList初始化

---

Deque接口从Queue扩展, Queue的API也可以用

```java
Deque<Integer> deque = new LinkedList<>();
// 添加元素到队首/队尾
deque.addFirst(1);
deque.offerFirst(1);
deque.addLast(1);
deque.offerLast(1);
// 取队首/队尾元素并删除
deque.removeFirst();
deque.pollFirst();
deque.removeLast();
deque.pollLast();
// 取队首/队尾元素不删除
deque.peekFirst();
deque.getFirst();
deque.peekLast();
deque.getLast();
```

## LinkedList: 双向链表实现

---

可作为List, Deque, Queue

```java
LinkedList<Integer> num = new LinkedList<Integer>();
num.add(index);
num.remove(index);
num.isEmpty();
// 通过对链表头尾操作可同时当stack和queue
num.addFirst(Integer);
num.addLast(Integer);
num.getFirst();
num.getLast();
num.offer();
num.offerFirst(Integer);
num.offerLast(Integer); 
num.removeLast();
num.removeLast();
```

### 与int[]转换

```java
// 把List<Integer>转换成int[]
int[] newNum = num.stream().mapToInt(Integer::intValue).toArray();

// 把int[]转换为List<Integer>
public List<Integer> convert(int[] n){
    List<Integer> num = new ArrayList<Integer>(n.length);
    for (int i : n){
        num.add(i);
    }
    return num;
}
```

## PriorityQueue

---

用小顶堆实现，每次取出最小值，poll()复杂度为O(1)，add(Obj)复杂度为O(log(N))

```java
PriorityQueue<Integer> pq = new PriorityQueue<>(); 

// 改为大顶堆
PriorityQueue<Integer> pq = new PriorityQueue<>(new Comparator<Integer>(){
    @Override
    public int compare(Integer i1, Integer i2){
        return i2-i1;
    }
}); 
// 简化写法（匿名Lambda表达式）
Queue<Integer> pq = new PriorityQueue<>((n1, n2) -> n2 - n1); 

pq.add(Integer);
pq.offer(Integer);
pq.poll();
pq.remove();
```

## Map

---

基本单元为Entry, 包含一个键值对

### HashMap: 数组实现，无法覆写comparator实现排序，只能自动按照hashcode排序

```java
Map<Integer, Integer> map = new HashMap<>();
map.put(key, value);
map.getOrDefault(key, default);
map.get(key);
map.containsKey(key);
map.remove(key);
map.remove(key, value);
map.clear();
map.isEmpty();
map.keySet();
map.values();
map.size();
map.entrySet();
// 遍历
// 按键遍历
for (int key : map.keySet());
// 按值遍历
for (int value : map.values());
// 按Entry遍历
for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
    entry.getKey();
    entry.getValue();
}
```

### TreeMap: 默认按照Key进行升序排序（对String默认按字母排序）

```java
// 按照Key降序排序
Map<Integer, Integer> map = new TreeMap<>((o1, o2) -> o2 - o1);
// 按照Value升序排序：可以把map.values()转换为list排序再sort
Map<Integer, Integer> map = new HashMap<>();
List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
Collections.sort(list, (o1, o2) -> o1.getValue() - o2.getValue());
```

## Set

---

基于哈希表实现

```

java
Set<Integer> set = new HashSet<Integer>();
set.add();
set.remove();
set.contains();
// 需要排序使用TreeSet
Set set = new HashSet((o1, o2) -> o2 - o1);
```

--- 




# 基础

---

## 输入输出

---

``` Java
Scanner in=new Scann(System.in);
int n=in.nextInt();//读取单个字符；
String s=in.nextLine();//读取整行输入；
//优化：
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String n=inBufferedReader.readLine();
```

## StringBuilder

---

```Java
StringBuilder stringBuilder = new StringBuilder();
stringBuilder.setCharAt(0, 's');
```

## 类型转换

---

```Java
//Stinrg类型转换成int；其他同理
Integer.valueOf(string);
Integer.parseInt(string);
```

## list转换为int数组

---

```Java
List<int[]> list = new ArrayList<>();
list.toArray(new int[list.size()][2])
 List<Integer> temp =new ArrayList();
        temp.add(0, 12);
        temp.add(0, 122);
```

## ArrayList方法

---

``` Java
List<Integer> res=new ArrayList();
res.clear();//清空元素内容。
Collections.reverse(res) //将动态数组元素内容逆序。
```

## 最大值最小值

---

```Java
Long同理
max = Integer.MAX_VALUE;
min = Integer.MIN_VALUE;
```

## String

---

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

---

## HashMap

---

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

---

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

---

```Java
//一种简单做法是通过Arrays.sort()传入新的Compartor对象；来实现按照指定序列排序；比如我们想实现二维数组，按照第一列升序，第二列降序
  Arrays.sort(arr, new Comparator<int[]>()
         {
             public int compare(int[] a, int[] b) {
                 return a[0] == b[0] ?
                     b[1] - a[1] : a[0] - b[0];
             }
         });
```
``` Java
      Arrays.sort(arr,(int[]a, int[]b)->{
              return  b[0]==a[0]?a[1]-b[1]:a[0]-b[0];
          });

```

# 输出

---

``` Java
            System.out.println(String.format("%.6f",((s-1)/n)*100));//保留6位小数 四舍五入

```

# 其他

---

## 字符串加法

---

``` Java
  public static void main(String[] args){
        Main m=new Main();
        String a="110101";
        String b="1010110";
        String sum=m.add(a,b);
        System.out.println(sum);
    }
    public String add(String a,String b){
        int sum=Integer.valueOf(a,2)+Integer.valueOf(b,2);
        return Integer.toBinaryString(sum);
    }
```

## 向上取整，向下取整

---

java m/n向下取整 m+n-1/n向上取整

## 数组填充指定数字

---

Arrays.fill(nums,number)填充数组指定值

## 求最大公约数

---

``` Java
public static int gcd(int m, int n) {
    return n == 0 ? m : gcd(n, m % n);
}
```

## 使用javaStream求和

---

```Java
 int sumA = Arrays.stream(A).sum();
 int sumB = Arrays.stream(B).sum();
```

## 优先级队列构造

---

``` Java
  PriorityQueue<Integer> minQueue = new PriorityQueue<>(Comparator.naturalOrder());
  PriorityQueue<Integer> maxQueue = new PriorityQueue<>(Comparator.reverseOrder());
  按照第二个元素升序。
        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(
            new Comparator<int[]>(){
                public int compare(int[]a,int[]b){
                    return a[1]-b[1];
                }
            }
        );
       
```

## 随机数

---

``` Java
    int random= new Random().nextInt(n);生成0到 n之间的正数。[0,n];
```

## list转普通数组

---

```
    List<int[]> list = new ArrayList();
   ist.toArray(new int[list.size()][2]);   
```