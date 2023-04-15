import 'package:flutter/material.dart';

class ListViewPage extends StatefulWidget {
  ListViewPage({super.key});

  @override
  State<ListViewPage> createState() => _ListViewPageState();
}

class _ListViewPageState extends State<ListViewPage> {
  final List<String> entries = <String>['E', 'F', 'G'];

  final List<int> colorCodes = <int>[600, 500, 100];

  Widget retornaListViewEstatico() {
    return ListView(
      padding: const EdgeInsets.all(0),
      children: [
        Container(
            height: 50,
            color: Colors.amber[500],
            child: const Center(
              child: Text('Entry A'),
            )),
        Container(
            height: 50,
            color: Colors.amber[300],
            child: const Center(child: Text('Entry B'))),
        Container(
            height: 50,
            color: Colors.amber[200],
            child: const Center(child: Text('Entry c'))),
      ],
    );
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
        padding: const EdgeInsets.all(0),
        itemCount: entries.length,
        itemBuilder: (BuildContext context, int index) {
          return Container(
              height: 50,
              color: Colors.amber[colorCodes[index]],
              child: Center(child: Text('Entry ${entries[index]}')));
        });
  }
}
