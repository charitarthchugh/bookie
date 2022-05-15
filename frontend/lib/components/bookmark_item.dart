import 'package:flutter/material.dart';
import 'package:flutter_nord_theme/flutter_nord_theme.dart';
import 'package:google_fonts/google_fonts.dart';

class BookmarkItem extends StatelessWidget {
  const BookmarkItem(
      {Key? key,
      required this.name,
      required this.description,
      required this.folder,
      required this.link,
      required this.favicon})
      : super(key: key);
  final String name;
  final String description;
  final String folder;
  final String link;
  final Image favicon;
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Row(
          children: [
            Padding(padding: const EdgeInsets.all(15.0), child: favicon),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(0, 0, 0, 5),
                  child: Text(
                    name,
                    style: GoogleFonts.getFont("Roboto",
                        textStyle: Theme.of(context).textTheme.bodyLarge,
                        fontSize: 19),
                  ),
                ),
                Text(
                  description,
                  style: GoogleFonts.getFont("Roboto",
                      textStyle: Theme.of(context).textTheme.bodyMedium,
                      fontWeight: FontWeight.normal),
                ),
                Padding(
                  padding: const EdgeInsets.only(top: 5),
                  child: Row(
                    children: [
                      Icon(
                        Icons.folder,
                        size: 16,
                        color: NordColors.snowStorm.darkest,
                      ),
                      Text(
                        folder,
                        style: GoogleFonts.getFont("Roboto",
                            textStyle: Theme.of(context).textTheme.bodySmall,
                            color: NordColors.snowStorm.darkest),
                      ),
                      Icon(
                        Icons.fiber_manual_record,
                        size: 10,
                        color: NordColors.polarNight.lighter,
                      ),
                      Text(
                        link,
                        style: GoogleFonts.getFont("Roboto",
                            textStyle: Theme.of(context).textTheme.bodySmall,
                            color: NordColors.snowStorm.darkest),
                      )
                    ],
                  ),
                )
              ],
            )
          ],
        ),
        Divider(
          color: NordColors.polarNight.darker,
          indent: 30,
          endIndent: 30,
        )
      ],
    );
  }
}
