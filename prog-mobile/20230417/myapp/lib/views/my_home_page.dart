import 'package:flutter/material.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import 'dart:async';

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  Future<Database> _openBanco() async {
    try{
      print('Executando a função openBanco()');
      var databasePath = await getDatabasesPath();
      String path = join(databasePath, 'banco.db');

      Database db = await (openDatabase(path, version: 1,
          onCreate: (db, versaoRecente) async {
        String sql =
            "CREATE TABLE contatos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR)";
        await db.execute(sql);
      }));
      print('Banco:  ${db.isOpen.toString()}');
      return db;
    }
    catch(ex){
      print('Erro desconhecido. Tente novamente mais tarde.');
      throw Exception();
    }
  }

  void _salvar() async {
    Database db = await _openBanco();
    Map<String, dynamic> dadosContato = {'nome': 'Jonatas Laet'};
    int idContato = await db.insert('contatos', dadosContato);
    print('Id: $idContato');
  }

  @override
  Widget build(BuildContext context) {
    _openBanco();
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        title: Text(widget.title),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'You have pushed the button this many times:',
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headlineMedium,
            ),
          ],
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
