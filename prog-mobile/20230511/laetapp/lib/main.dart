import 'package:laetapp/views/authentication_view.dart';
import 'package:laetapp/views/entry_view.dart';
import 'package:flutter/material.dart';
import 'package:laetapp/views/maps_view.dart';

void main() {
  runApp(const LaetApp());
}

class LaetApp extends StatelessWidget {
  const LaetApp({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: MaterialApp(
        title: 'Presentation Page',
        initialRoute: '/',
        routes: {
          '/': (context) => const EntryView(),
          '/auth': (context) => const AuthenticationView(),
          '/maps': (context) => const MapsView()
        },
      ),
    );
  }
}
