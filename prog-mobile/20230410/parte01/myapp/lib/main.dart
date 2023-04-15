import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
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
    return DefaultTabController(
        initialIndex: 2,
        length: 3,
        child: Scaffold(
          body: const TabBarView(children: [
            Center(child: Text("It's cloudy here")),
            Center(child: Text("It's rainy here")),
            Center(child: Text("It's sunny here"))
          ]),
          appBar: AppBar(
            title: const Text('TabBar Widget'),
            bottom: const TabBar(tabs: [
                Tab(icon: Icon(Icons.cloud_outlined)),
                Tab(icon: Icon(Icons.beach_access_sharp)),
                Tab(icon: Icon(Icons.brightness_5_sharp))
          ]))
        ));
  }
}

