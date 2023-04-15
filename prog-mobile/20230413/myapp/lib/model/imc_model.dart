import 'package:flutter/material.dart';

class Imc extends StatefulWidget {
  Imc({super.key, required this.title});

  final String title;

  @override
  State<Imc> createState() => _ImcState();
}

class _ImcState extends State<Imc> {
  final TextEditingController _textEditControllerAltura =
      TextEditingController();
  final TextEditingController _textEditControllerPeso = TextEditingController();

  double imc = 0.0;

  String resultado = '';
  String info = '';

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Calculadora de IMC"),
          centerTitle: true,
          actions: [
            IconButton(
                onPressed: () {
                  setState(() {
                    imc = 0.0;
                    resultado = '';
                    _textEditControllerAltura.text = '';
                    _textEditControllerPeso.text = '';
                    info = '';
                  });
                },
                icon: const Icon(Icons.refresh))
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
              TextField(
                  textAlign: TextAlign.center,
                  keyboardType: TextInputType.number,
                  controller: _textEditControllerPeso,
                  decoration: const InputDecoration(
                      labelText: "Peso (kg)",
                      labelStyle:
                          TextStyle(color: Colors.green, fontSize: 25.0))),
              const SizedBox(height: 20.0),
              TextField(
                  textAlign: TextAlign.center,
                  keyboardType: TextInputType.number,
                  controller: _textEditControllerAltura,
                  decoration: const InputDecoration(
                      labelText: "Altura (cm)",
                      labelStyle:
                          TextStyle(color: Colors.green, fontSize: 25.0))),
              const SizedBox(height: 20.0),
              Container(
                height: 50.0,
                child: ElevatedButton(
                    onPressed: () {
                      setState(() {
                        double altura =
                            double.parse(_textEditControllerAltura.text) / 100;
                        double peso =
                            double.parse(_textEditControllerPeso.text);
                        if (altura == 0) {
                          resultado =
                              'Não existe divisão por zero! Por favor, insira um valor na altura';
                        } else {
                          imc = peso / (altura * altura);
                          resultado =
                              'Seu imc é igual a ' + imc.toStringAsFixed(2);
                          if (imc < 18.5) {
                            info = ' -- Abaixo do peso --';
                          } else if (imc <= 24.9) {
                            info = ' -- Peso normal --';
                          } else if (imc <= 29.90) {
                            info = ' -- Excesso de peso --';
                          } else if (imc <= 34.90) {
                            info = ' -- Obesidade Classe I --';
                          } else if (imc <= 39.90) {
                            info = ' -- Obesidade Classe II --';
                          } else {
                            info = ' -- Obesidade Classe III --';
                          }
                        }
                      });
                    },
                    child: const Text(
                      'Calcular',
                      style: TextStyle(color: Colors.white, fontSize: 25.0),
                    )),
              ),
              const SizedBox(height: 20.0),
              Text(resultado,
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.green, fontSize: 25.0)),
              Text(info,
                  textAlign: TextAlign.center,
                  style: TextStyle(color: Colors.green, fontSize: 25.0))
            ],
          ),
        ));
  }
}
