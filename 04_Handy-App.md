Handy-App
========
Bevor man eine Handy-App schreibt, muss man sich für einen der zu vielen Wege entscheiden. Das liegt auch daran, dass es sehr viele Programmiersprachen gibt, die unterschiedliche Vor- und Nachteile haben. Daher ein Kommentar vorweg: Eine Programmiersprache zu lernen lohnt sich auf jeden Fall, egal welche. Gute Tutorials, mit denen man sich das Programmieren beibringen kann, gibt's auf [codecademy.com](https://www.codecademy.com/) und [w3schools](http://www.w3schools.com/).

Nun zu meiner Einschätzung: Ich denke, dass in naher Zukunft Browser-Apps zunehmen werden, da Browser sich als Schnittstelle zwischen Internet und Handy dazu anbieten: über den Browser kann mit den Geräten des Handys gesprochen werden. Das ist m.E. aber auch der kritische Punkt, wieso das Rennen vielleicht doch besser von nativen Apps gewonnen werden sollte: unsere Browserabhängigkeit und die hier fehlende Differenzierung beim Rechtemanagement (Mozillas Firefox hat bzgl. Datenschutz in letzter Zeit manches Vertrauen verspielt und Chrome ist von Google).

## Fachdidaktische Überlegungen

**Ansatz Nr. 1** Aus fachdidaktischer Sicht ist die Entscheidung für die Programmierung einer WebApp extrem konsequent, da die Schüler ausgehend vom Coden mit Markdown, HTML und CSS perfekt zu JavaScript motiviert werden können und mit [AppLab](https://code.org/educate/applab) eine nette Brücke zu JavaScript existiert. Das war mein bisheriger Ansatz und ich finde diese Linie nach wie vor überzeugend. JavaScript wird wohl auch in nächster Zeit der Standard in der Webprogrammierung bleiben; bleiben wird allerdings auch die Wahrnehmung von JavaScript als große Hürde. Der Organisationsaufwand für diesen Weg ist sehr gering.

**Ansatz Nr. 2** Im nächsten Durchgang will ich mit dem RaspberryPi anfangen, da ich die Idee schick finde, die damit erlernte Programmiersprache Python dann zur Entwicklung einer App zu verwenden. Zum Einen kommt es Schülern entgegen, nur eine Programmiersprache lernen zu müssen, zum Anderen kommt es ihnen auch entgegen, dass es nicht JavaScript oder Java ist. Außerdem scheint vielen Schülern (und mir, s.o.) das Programmieren einer nativen App attraktiver als das einer WebApp. Zu Markdown, HTML und CSS kommen die Schüler dann automatisch, wenn sie ihr Projekt dokumentieren oder ihre App im Internet präsentieren wollen. Ein Nachteil dieses Ansatzes ist, dass das Programmieren von nativen Apps mit Python (Kivy) realo kein Standard ist. Schülern, die später beruflich in die Richtung App-Entwicklung gehen wollen, wird das Umsteigen auf andere Programmiersprachen dann aber durch diese Einheit dennoch erleichtert. Der Vorteil von Kivy ist die Plattformunabhängigkeit. Ein kleiner Problempunkt von Kivy könnte das Kompilieren sein, ich habe bisher nur Buildozer ausprobiert und der ist nur für ein Projekt kostenlos. Organisatorisch ist dieser Weg aufgrund der RPis und einiger Programme, die erst im Netzwerk (oder auf den RPis) zum Laufen gebracht werden müssen, zumindest im ersten Durchgang aufwendig.

**Ansatz Nr. 3** Ein dritter fachdidaktischer Weg könnte m.E. beim Arduino beginnen. Die Brücke zur App-Entwicklung ist Processing, da damit sowohl der Arduinos programmiert als auch super einfach Apps entwickelt werden können. Die Vor- und Nachteile sind ähnlich wie beim zweiten Ansatz. Gegenüber dem zweiten Ansatz ist das Programmieren einer Handy-App mit Processing einfacher, allerdings ist Python dagegen eine Standard-Programmiersprache.

## Native App

### Klicken
Zum Einstieg kann das Programmieren nach dem Baukasten-Prinzip auf [code.org](https://studio.code.org/s/20-hour) geübt werden.

Mit diesen Programmen kann man native Apps durch Klicki-Bunti "programmieren" (habe nicht alle ausprobiert)
* [AppInventor](http://appinventor.mit.edu/explore/) ([RWTH](http://schuelerlabor.informatik.rwth-aachen.de/sites/default/files/dokumente/Einrichten%20des%20MIT%20AppInventor.pdf))
* [AppYourself](http://appyourself.net/de)
* [iBuildApp](http://ibuildapp.com/)
* [appTITAN](http://www.apptitan.de/de/)


### Programmieren
* [Kivy](https://de.wikipedia.org/wiki/Kivy). Mittels Python können plattformübergreifende Apps geschrieben werden. Beispiel: [Banana Grader](https://github.com/DorKeinath/BananaGrader/).
* [Processing](https://de.wikipedia.org/wiki/Processing). All-in-one Paket für alle Plattformen, mit dem man mit den geringsten Start- und Kompilierungsproblemen eine App auch z.B. für ein Android-Handy oder ein iPhone programmieren kann.
	* Geile deutsche Anleitung auf [creativecoding.org](http://www.creativecoding.org/)
	* Weitere deutsche Anleitungen sind im Wikipedia-Artikel verlinkt.
	* Das Forum nutzen, denn da gibt's viele Code-Schnipsel.

Weitere Möglichkeiten, die ich noch nicht ausprobiert habe:
* [Meteor](https://www.meteor.com/). Plattformunabhängige JavaScript-Apps.
* [Ionic](https://github.com/driftyco/ionic)
* [B4X](https://www.b4x.com)
* [AndroidStudio](https://developer.android.com/sdk/index.html)
	* [Newsreader](https://www.androidpit.de/android-entwickler-studio-erste-app#)
	* [Java ist auch eine Insel](http://www.amazon.de/Java-auch-eine-Insel-Programmieren/dp/3898427471)



## Web-App
Der Hauptbegriff lautet hier JavaScript. Entweder man lernt JavaScript oder eine zu JavaScript kompilierende vereinfachte Skriptsprache.

### Klicken
* [App Lab](https://code.org/educate/applab) *[Hinweise für Lehrer](https://code.org/educate)*

### Programmieren
* [JavaScript Tutorial auf w3schools](http://www.w3schools.com/js/default.asp)
* **JavaScript** [Tutorials von Mozilla](https://developer.mozilla.org/en-US/docs/Web/Tutorials).

Fachdidaktisch ist es glaub am sinnvollsten, original JavaScript zu verwenden (wennschon-dennschon), vielleicht ist aber auch etwas davon sinnvoll (habe ich nicht ausprobiert):
* [LimeJS](https://github.com/digitalfruit/limejs)
* [CoffeeScript](http://coffeescript.org/). [GitBook-Anleitung](https://weakish.gitbooks.io/cs4cats/content/coffeescript-for-cats.html)
* Mozillas Konzept der **[Open Web Apps](https://developer.mozilla.org/en-US/Apps/Fundamentals/Quickstart/Build/Intro_to_open_web_apps)**
* Framework, das nach JavaScript und andere Dateien kompilieren kann.
	* [libGDX](https://github.com/libgdx/libgdx)
	* [JustWeEngine](https://github.com/lfkdsk/JustWeEngine)
	* [playn](https://github.comQDF/playn/playn)
* Kompilieren einer WebApp zur nativen App mit PhoneGap oder [Apparatio](http://apparat.io/). [Artikel](http://softwareas.com/is-this-what-the-app-of-2015-looks-like-html5-coffeescript-less-webstore-phonegap-apparatio/)
