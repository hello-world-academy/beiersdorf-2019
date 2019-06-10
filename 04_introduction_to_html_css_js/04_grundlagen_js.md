# Grundlagen JS

[JavaScript (JS)](https://de.wikipedia.org/wiki/JavaScript) ist ein Programmiersprache, die Webseiten Dynamik, Interaktivität und Responsivität hinzufügt.

JavaScript ist sehr vielfältig. Entwickler können auf eine Vielzahl von Tools und Erweiterungen zurückgreifen und somit die Kernfunktionalität von JS deutlich erweitern.

Es ist grundsätzlich möglich, JS-Code direkt in das HTML Dokument zu schreiben. Aber auch hier, ähnlich wie für das Einfügen von CSS, empfiehlt es sich, lediglich eine Referenz auf einen JS-Datei im HTML zu hinterlegen (kurz vor dem _tag_ `</body>`). 

`<script src="pfad-zu-der-datei/name-js-script.js"></script>`

***

## Übung 6

> __Änderung des Dokumententitels mit Hilfe von JS Code zu `'Hello World Academy'`__
> * Öffnen Sie das HTML Dokument `04_introduction_to_html_css_js/html/04-js-uebung.html` mit einem Texteditor Ihrer Wahl.
> * Öffnen Sie das HTML Dokument `04_introduction_to_html_css_js/html/04-js-uebung.html` mit einem Browser Ihrer Wahl.
> * Öffnen Sie das JS-Script `04_introduction_to_html_css_js/html//scripts/header_changer.js` mit einem Texteditor Ihrer Wahl.
> Fügen Sie die folgende zwei Zeilen JS-Code in die Datei `header_changer.js` ein und speichern Sie diese.
>```
>var myHeading = document.querySelector('h1');
>myHeading.textContent = 'Hello World Academy';
>```
> * Fügen Sie `<script src="/scripts/header_changer.js"></script>` dem HTML Dokument `04_introduction_to_html_css_js/html/04-js-uebung.html` hinzu und speichern Sie die Änderungen.
> * Aktualisieren Sie die den Browser.

### Was ist passiert?

* Die Überschrift wurde mit Hilfe von JS in `Hello World Academy` geändert.
* Die Funktion `querySelector()` referenzierte die Überschrift und speicherte diese in eine  Variable (`myHeading`)
* Danach wurde diese Variable (ein JS-Objekt) mit dem neuen Titel überschrieben (`textContent` Eigenschaft).
* Gehen Sie auf den Browser und lassen Sie sich den _Quellcode anzeigen_ (rechte Maustaste). Sie werden sehen, dass das HTML Dokument unverändert ist und der JS-Code die Änderung dynamisch durchführte.   

***

## Übung 7

> __Öffnen Sie die JS-Datei `04_introduction_to_html_css_js/html/scripts/image_switcher.js` und versuchen Sie zu verstehen was das JS-Skript macht__
> * Öffnen Sie das HTML Dokument `04_introduction_to_html_css_js/html/05-js-uebung.html` mit einem Texteditor Ihrer Wahl.
> * Öffnen Sie das HTML Dokument `04_introduction_to_html_css_js/html/05-js-uebung.html` mit einem Browser Ihrer Wahl.
> Klicken Sie auf den _Beiersdorf_ Schriftzug. 
> Was ist passiert?
***