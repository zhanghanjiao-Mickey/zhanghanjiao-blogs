import os

# 重新创建一个_sidebar.md文件
sidebar_path = '_sidebar.md'

# 再次检查“博客文档”文件夹
blog_docs_path = '博客文档'
if not os.path.exists(blog_docs_path):
    print(f"没有找到文件夹：{blog_docs_path}")
else:
    # 对博客文档文件夹中的内容进行排序
    entries = os.listdir(blog_docs_path)
    entries.sort(key=lambda entry: os.path.getctime(os.path.join(blog_docs_path, entry)))

    with open(sidebar_path, 'w', encoding='utf-8') as sidebar_file:
        # 遍历每一个条目
        for entry in entries:
            entry_path = os.path.join(blog_docs_path, entry)
            if os.path.isdir(entry_path):
                # 跳过名为“其他”的文件夹
                if entry == '其他':
                    continue
                
                # 写入文件夹名称
                sidebar_file.write(f"- {entry}\n")

                # 检查是否存在与文件夹同名的.md文件
                md_file_path = os.path.join(entry_path, f"{entry}.md")
                if os.path.exists(md_file_path):
                    relative_path = f"{blog_docs_path}/{entry}/{entry}.md"
                    sidebar_file.write(f"  - [{entry}]({relative_path})\n")
                
                # 写入该文件夹内所有的.md文件
                for file in os.listdir(entry_path):
                    if file.endswith('.md'):
                        file_name = os.path.splitext(file)[0]
                        relative_file_path = f"{blog_docs_path}/{entry}/{file}"
                        sidebar_file.write(f"  - [{file_name}]({relative_file_path})\n")

print("侧边栏文件已经生成。")
