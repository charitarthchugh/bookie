import "package:flutter/material.dart";
import 'package:flutter_nord_theme/flutter_nord_theme.dart';
import 'package:google_fonts/google_fonts.dart';

class NewBookmark extends StatelessWidget {
  const NewBookmark({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return ElevatedButton(
      style: ElevatedButton.styleFrom(
          primary: NordColors.polarNight.lightest,
          maximumSize: const Size(115, 42),
          shape:
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(90))),
      onPressed: (() {}),
      child: Center(
        child: Row(
          children: [
            Icon(
              Icons.add,
              color: NordColors.snowStorm.lightest,
            ),
            Padding(
              padding: const EdgeInsets.only(left: 8.0),
              child: Text(
                "New",
                style: GoogleFonts.getFont("Poppins",
                    textStyle: Theme.of(context).textTheme.titleMedium,
                    color: NordColors.snowStorm.lightest),
              ),
            )
          ],
        ),
      ),
    );
  }
}
