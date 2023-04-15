import 'package:flutter/material.dart';

class CombustivelController extends StatefulWidget {
  const CombustivelController({super.key});

  @override
  State<CombustivelController> createState() => _CombustivelControllerState();
}

class _CombustivelControllerState extends State<CombustivelController> {
  final TextEditingController _valorGasolinaController =
      new TextEditingController();
  final TextEditingController _valorAlcoolController =
      new TextEditingController();

  double resultado = 0.0;

  void calcular() {
    setState(() {
      double valorGas = double.parse(_valorGasolinaController.text);
      double valorAlcool = double.parse(_valorAlcoolController.text);
      resultado = valorGas + valorAlcool;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Column(
        children: [
          Icon(Icons.gas_meter),
          Text('Gasolina'),
          TextField(
            keyboardType: TextInputType.number,
            controller: _valorGasolinaController,
          ),
          Text('Alcool'),
          TextField(
            keyboardType: TextInputType.number,
            controller: _valorAlcoolController,
          ),
          TextButton(onPressed: calcular, child: const Text('CALCULAR')),
          Text('Resposta: $resultado')
        ],
      ),
    );
  }
}
