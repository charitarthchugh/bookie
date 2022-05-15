import 'package:flutter/material.dart';
import 'package:frontend/components/logo.dart';
import 'package:frontend/components/tmp/maintmp.dart';

class BookieDrawer extends StatelessWidget {
  const BookieDrawer({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: Column(
        children: [
          const Center(child: DrawerHeader(child: Logo())),
        ],
      ),
    );
  }
}
