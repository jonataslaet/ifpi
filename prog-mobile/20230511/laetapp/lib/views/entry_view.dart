import 'package:flutter/material.dart';

class EntryView extends StatelessWidget {
  const EntryView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
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
                image: const DecorationImage(image: NetworkImage("https://vali.qconcursos.com/odin/users/avatars/284b96fb-94f8-4d2d-9d61-b598eccd151cavatar-qgq7qi.png"))
              ),
            ),

            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/auth');
              },
              child: const Text('Autenticação'),
            ),
            ElevatedButton(
              onPressed: () {
                Navigator.pushNamed(context, '/maps');
              },
              child: const Text('Mapa'),
            )
            // TextButton(onPressed: () {}, child: const MapView())
          ],
        ),
      ),
    );
  }
}
