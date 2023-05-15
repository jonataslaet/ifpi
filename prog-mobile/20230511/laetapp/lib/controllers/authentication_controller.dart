import 'package:flutter/material.dart';

class AuthenticationController extends StatefulWidget {
  const AuthenticationController({super.key});

  @override
  State<AuthenticationController> createState() =>
      _AuthenticationControllerState();
}

class _AuthenticationControllerState extends State<AuthenticationController> {
  final TextEditingController _valorLoginController = TextEditingController();
  final TextEditingController _valorSenhaController = TextEditingController();

  String status = 'Não autenticado';

  void autenticar() {
    setState(() {
      if (_valorLoginController.text == 'admin' &&
          _valorSenhaController.text == 'admin') {
        status = 'Autenticado';
      } else {
        status = 'Não autenticado';
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 300,
      child: Scaffold(
        body: Column(
          children: [
            const Text('Login'),
            TextField(
              keyboardType: TextInputType.text,
              controller: _valorLoginController,
            ),
            const Text('Senha'),
            TextField(
              keyboardType: TextInputType.number,
              controller: _valorSenhaController,
            ),
            TextButton(onPressed: autenticar, child: const Text('Autenticar')),
            Text('Status: $status')
          ],
        ),
      ),
    );
  }
}
