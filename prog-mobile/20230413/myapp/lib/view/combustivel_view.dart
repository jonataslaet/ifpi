import 'package:flutter/material.dart';
import 'package:myapp/combustivel_controller.dart';

class CombustivelView extends StatelessWidget {
  const CombustivelView({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.green,
      ),
      home: const CombustivelController(),
    );
  }
}