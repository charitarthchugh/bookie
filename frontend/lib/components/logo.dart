import 'package:flutter/material.dart';
import 'package:flutter_nord_theme/flutter_nord_theme.dart';
import 'package:google_fonts/google_fonts.dart';

class Logo extends StatelessWidget {
  const Logo({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextButton(
      onPressed: () {
        showAboutDialog(
          context: context,
          applicationName: "",
          applicationIcon: Text("bookie",
              style: GoogleFonts.getFont('Pacifico',
                  textStyle: Theme.of(context).textTheme.titleLarge,
                  fontSize: 54,
                  color: NordColors.aurora.purple)),
        );
      },
      child: Text("bookie",
          style: GoogleFonts.getFont('Pacifico',
              textStyle: Theme.of(context).textTheme.titleLarge,
              fontSize: 54,
              color: NordColors.aurora.purple)),
    );
  }
}
