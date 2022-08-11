import 'package:flutter/material.dart';
import 'package:flutter_simple_treeview/flutter_simple_treeview.dart';
import 'package:bookief/components/logo.dart';

class BookieDrawer extends StatelessWidget {
  const BookieDrawer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Column(
        children: const [
          Center(child: DrawerHeader(child: Logo())),
          FolderView()
        ],
      ),
    );
  }
}

class FolderView extends StatefulWidget {
  const FolderView({Key? key}) : super(key: key);

  @override
  State<FolderView> createState() => _FolderViewState();
}

class _FolderViewState extends State<FolderView> {
  final TreeController _treeController = TreeController();
  List<TreeNode> toTreeNodes(List<String> foldersString) {
    Map<String, dynamic> toNestedFolderMap(List<String> folders) {
      var mapRoot = <String, dynamic>{};
      for (var path in folders) {
        var currentMap = mapRoot;
        for (var key in path.split('/')) {
          currentMap = currentMap[key] ??= <String, dynamic>{};
        }
      }
      return mapRoot;
    }

    List<TreeNode> createTreeNodes(dynamic parsedPaths) {
      if (parsedPaths is Map<String, dynamic> && parsedPaths != {}) {
        return parsedPaths.keys
            .map((k) => TreeNode(
                content: Text('$k'), children: createTreeNodes(parsedPaths[k])))
            .toList();
      }
      // if (parsedPaths is List<dynamic>) {
      //   return parsedPaths
      //       .asMap()
      //       .map((i, element) => MapEntry(
      //           i,
      //           TreeNode(
      //               content: Text('[$i]:'), children: toTreeNodes(element))))
      //       .values
      //       .toList();
      // }
      return [TreeNode(content: Text(parsedPaths.toString()))];
    }

    return createTreeNodes(toNestedFolderMap(foldersString));
  }

  var mapPaths = [
    "animal/cat/persian",
    "animal/cat/british_shorthair",
    "animal/dog/pug",
    "animal/dog/pitbull",
    "vehicle/car/mercedes",
    "vehicle/car/bmw",
  ];
  Widget buildTree() {
    try {
      return TreeView(
        nodes: toTreeNodes(mapPaths),
        treeController: _treeController,
      );
    } on FormatException catch (e) {
      return Text(e.message);
    }
  }

  @override
  Widget build(BuildContext context) {
    return buildTree();
  }
}
