import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'MyApp',
      initialRoute: '/',
      routes: {
        '/': (context) => const MyHome(),
        '/second': (context) => const SecondRoute()
      },
    );
  }
}

class MyHome extends StatefulWidget {
  const MyHome({super.key});

  @override
  State<MyHome> createState() => _MyHomeState();
}

class _MyHomeState extends State<MyHome> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Primeira tela"),
      ),
      body: Center(
        child: Column(children: [
          ElevatedButton(
              onPressed: () => Navigator.pushNamed(context, '/second'),
              child: const Text("Avançar Página")),
        ]),
      ),
    );
  }
}

class SecondRoute extends StatelessWidget {
  const SecondRoute({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Segunda tela"),
      ),
      body: Center(
        child: Column(children: [
          ElevatedButton(
              onPressed: () => Navigator.pop(context),
              child: const Text("Voltar")),
        ]),
      ),
    );
  }
}
