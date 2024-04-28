源码阅读顺序参考：http://shanks.link/blog/2021/08/23/redis%E6%BA%90%E7%A0%81%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB%E9%A1%BA%E5%BA%8F/

2024/4/28：开始数据结构部分

| 文件                                                         | 内容                        |
| :----------------------------------------------------------- | :-------------------------- |
| sds.h 和 sds.c                                               | Redis 的动态字符串实现。    |
| adlist.h 和 adlist.c                                         | Redis 的双端链表实现。      |
| dict.h 和 dict.c                                             | Redis 的字典实现。          |
| redis.h 中的 zskiplist 结构和 zskiplistNode 结构， 以及 t_zset.c 中所有以 zsl 开头的函数， 比如 zslCreate 、 zslInsert 、 zslDeleteNode ，等等。 | Redis 的跳跃表实现。        |
| hyperloglog.c 中的 hllhdr 结构， 以及所有以 hll 开头的函数。 | Redis 的 HyperLogLog 实现。 |