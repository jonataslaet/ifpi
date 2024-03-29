import 'package:flutter/material.dart';
import 'package:laetapp/controllers/google_maps_controller.dart';

class MapsView extends StatelessWidget {
  const MapsView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Mapa'),
      ),
      body: const Center(
        child: GoogleMapsController()
      ),
    );
  }
}
