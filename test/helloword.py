import pandas as pd

# 定义表数据
data = {
    'parent_name': ['t1', 't1', 't2', 't2', 't3'],
    'son_name': ['t2', 't3', 't4', 't5', 't8']
}

df = pd.DataFrame(data)


# 构建层级关系
def build_hierarchy(df, root, level=1, parent_table='parent_table'):
    hierarchy = []
    visited = set()  # 用于记录已经访问过的节点，避免重复

    def dfs(node, level, parent):
        if node in visited:
            return
        visited.add(node)
        hierarchy.append([level, node, parent if parent != 'parent_table' else parent_table])

        # 获取当前节点的所有子节点
        children = df[df['parent_name'] == node]['son_name'].tolist()

        for child in children:
            dfs(child, level + 1, node)

    dfs(root, level, root)

    return hierarchy


# 初始化根节点
root_nodes = df['parent_name'].unique()

all_hierarchies = []

for root in root_nodes:
    hierarchy = build_hierarchy(df, root)
    all_hierarchies.extend(hierarchy)

# 创建DataFrame并输出
result_df = pd.DataFrame(all_hierarchies, columns=['level_no', 'table_name', 'parent_tab'])
print(result_df)