# -*- coding: utf-8 -*-

import FbxCommon

def print_node(node, depth=0):
    indent = " " * depth * 2
    print("{}Node: {}".format(indent, node.GetName()))
    
    # トランスフォームを取得
    translation = node.LclTranslation.Get()
    rotation = node.LclRotation.Get()
    scale = node.LclScaling.Get()

    print("{}Translation: {}, {}, {}".format(indent, translation[0], translation[1], translation[2]))
    print("{}Rotation: {}, {}, {}".format(indent, rotation[0], rotation[1], rotation[2]))
    print("{}Scale: {}, {}, {}".format(indent, scale[0], scale[1], scale[2]))

    # ノードからメッシュを取得
    mesh = node.GetNodeAttribute()
    if mesh and mesh.GetAttributeType() == FbxCommon.FbxNodeAttribute.eMesh:
        print("{}Mesh found".format(indent))
        control_points = mesh.GetControlPoints()
        for i in range(mesh.GetControlPointsCount()):
            print("{}Vertex: {}, {}, {}".format(indent, control_points[i][0], control_points[i][1], control_points[i][2]))

    # 子ノードを再帰的に処理
    for i in range(node.GetChildCount()):
        print_node(node.GetChild(i), depth + 1)

# ファイルを読み込むためのマネージャーとシーンを作成します
manager, scene = FbxCommon.InitializeSdkObjects()

# FBXファイルをロードします
result = FbxCommon.LoadScene(manager, scene, 'default.fbx')
if not result:
    print('An error occurred while loading the scene...')

# シーンのルートノードを取得します
root_node = scene.GetRootNode()

# ノードの構造を表示します
print_node(root_node)