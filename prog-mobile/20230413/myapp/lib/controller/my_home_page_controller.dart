import 'package:myapp/model/items_model.dart';
import 'package:flutter/material.dart';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> with TickerProviderStateMixin {
  late TabController _tabController;

  final List<Items> items = <Items>[
    Items(nome: 'Arroz'),
    Items(nome: 'Feijão'),
    Items(nome: 'Farinha')
  ];

  Widget retornarListViewCombuilder() {
    return ListView.builder(
        itemCount: items.length,
        itemBuilder: (BuildContext context, int index) {
          final item = items[index];
          return CheckboxListTile(
              title: Text(item.nome),
              key: Key(item.nome),
              value: item.check,
              onChanged: (value) {
                setState(() {
                  item.check = value!;
                });
              });
        });
  }

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: retornarListViewCombuilder(),
      appBar: AppBar(
          actions: const <Widget>[Icon(Icons.local_grocery_store)],
          title: const Text('Home')),
    );
  }
}
