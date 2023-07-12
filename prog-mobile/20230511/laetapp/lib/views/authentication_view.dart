import 'package:flutter/material.dart';
import 'package:laetapp/controllers/authentication_controller.dart';

class AuthenticationView extends StatelessWidget {
  const AuthenticationView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Autenticação'),
      ),
      body: Center(
        child: Column(
          children: [
            Container(
              width: 150,
              height: 150,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: Colors.blue,
                border: Border.all(),
                image: const DecorationImage(image: NetworkImage("https://picsum.photos/250?image=9"))
              ),
            ),
            const AuthenticationController()
          ],
        ),
      ),
    );
  }
}