import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Calculadora de IMC"),
          centerTitle: true,
          actions: [
            IconButton(onPressed: () {}, icon: const Icon(Icons.refresh))
          ],
        ),
        body: SingleChildScrollView(
          padding: const EdgeInsets.fromLTRB(20.0, 0.0, 20.0, 0.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Icon(
                Icons.person_outline,
                size: 120.0,
                color: Color.fromRGBO(76, 175, 80, 1),
              ),
              const SizedBox(height: 20.0),
              const TextField(
                  textAlign: TextAlign.center,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                      labelText: "Peso (kg)",
                      labelStyle:
                          TextStyle(color: Color.fromARGB(255, 175, 76, 78), fontSize: 25.0))),
              const SizedBox(height: 20.0),
              const TextField(
                  textAlign: TextAlign.center,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                      labelText: "Altura (cm)",
                      labelStyle:
                          TextStyle(color: Colors.green, fontSize: 25.0))),
              const SizedBox(height: 20.0),
              Container(
                height: 50.0,
                child: ElevatedButton(
                    onPressed: () {},
                    child: const Text(
                      'Calcular',
                      style: TextStyle(color: Colors.white, fontSize: 25.0),
                    )),
              ),
              const SizedBox(height: 20.0),
              const Text("Info",
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.green, fontSize: 25.0))
            ],
          ),
        ));
  }
}
