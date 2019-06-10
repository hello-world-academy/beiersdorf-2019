# Grundlagen HTML

HTML (Hypertext Markup Language) ist keine Programmiersprache im eigentlichen Sinne. Es handelt sich vielmehr um eine Auszeichnungssprache (_markup language_), welche die Struktur einer Webseite beschreibt. Der Grundbaustein von HTML ist das sogenannte _Element_. Es erlaubt, Inhalte zu strukturieren und mit Attributen zu versehen.   

## Elemente

Ein Element kann u.a. Text, Daten, Bilder etc. beinhalten. Typischerweise beginnt ein Element mit einem (eröffnenden) `<...>` (_tag_), enthält Attribute, umschließt Text und endet mit einem (schließenden) `</...>`.

Hier ein Beispiel für ein `p` (_paragraph_) Element: 

`<p>class="abcd">Hello world!</p>`, 

- `<p>` eröffnender _tag_,
- `class="abcd"` ein Attribut und der dazugehörige Wert,
- `'Hello world!'` Text und der
- `</p>` schließender _tag_

Es gibt auch Elemente, die keinen Inhalt haben (_empty elements_):

`<img src="meinpfad/bild.png">`

Dieses Element enthält ein Attribut aber keinen schließenden _tag_ (`</img>`) und auch keinen Inhalt.

### Texte

#### Überschriften
Überschriftelemente ermöglichen es, einzelne Textpassagen als Überschriften unterschiedlicher Größe darzustellen. HTML enthält 6 vordefinierte Größen (`<h1>`–`<h6>`).

```
<h1>Überschrift 1. Ordnung</h1>
<h2>Überschrift 2. Ordnung</h2>
<h3>Überschrift 3. Ordnung</h3>
<h4>Überschrift 4. Ordnung</h4>
<h5>Überschrift 5. Ordnung</h5>
<h6>Überschrift 6. Ordnung</h6>
```

#### Absätze 
Das `<p>` Element kennzeichnet einen Absatz.

```
<p>Ich bin ein Absatz</p>
```

### Bilder

Das `<img>` Element fügt Bilddateien in das Dokument ein. Das `src` (_source_) Attribut verweist auf den Pfad zur Bilddatei (auf eine lokale Datei oder auch eine _url_).

`<img src="images/mein_Bild.png">`


## Die Anatomie eines HMTL Dokuments

```
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Coding Workshop</title>
  </head>
  <body>
    <img src="image/Beiersdorf.png">
  </body>
</html>
```

* `<!DOCTYPE html>` Der Dokumententyp. Ein historisches Artefakt, dass Anfang der 90er einem (best-practice) Standart entsprach. 
* `<html></html>` Das `<html>` Element. Das Element umfasst den gesamten Inhalt (_root element_).
* `<head></head>` Das `<head>` Element. Diese Element entspricht einem Container, in dem alles Relevante zu finden ist, dass nicht Teil des auf der Webseite angezeigten Inhaltes ist.
* `<meta charset="utf-8">` Das Element beschreibt die verwendete Zeichenkodierung.
* `<title></title>`  Das `<title>` Element. Es beschreibt den Titel der Webseite, die vom Browser im Reiter angezeigt wird und auch als Bezeichung der Seite beim Ablegen als Favorit verwendet wird.
* `<body></body>` Das `<body>` Element. Dieses Element beinhalt alle Inhalte der Webseite die dem Nutzer angezeigt werden (Text, Bilder, Videos, Spiele, etc).

***
## Übung 1

> __Erstellen Sie ein HTML Dokument mit folgenden Inhalten:__
> * Legen Sie den Titel des Browserreiters als `Coding Workshop` fest.
> * Erstellen Sie eine Dokumentenüberschrift `Grundlagen von Coding für Non-Coder`.
> * Erstellen Sie einen Paragraphen und dokumentieren Sie das heutige Datum `Datum 13.06.2019` 
> * Fügen Sie ein Bild hinzu. Dieses finden Sie unter dem Pfad `images/BDF_Logo.png`
> * Nutzen Sie bitte hierfür die Vorlage `04_introduction_to_html_css_js/html//01-html-uebung.html`. Öffnen Sie diese Datei mit einem Texteditor Ihrer Wahl und ergänzen Sie die fehlenden Zeilen. Gleichzeitig können Sie diese Datei mit einem Browser Ihrer Wahl öffnen, um Ihre Fortschritte sehen zu können.  


***

## Übung 2
> __Öffnen Sie das HTML Dokument `04_introduction_to_html_css_js/html/02-html-uebung.html` mit einem Texteditor Ihrer Wahl und versuchen Sie die Änderungen zur vorhergehende Version innerlich nachzuvollziehen.__
> * Das Element `<ul></ul>` steht fur eine ungeordnete Liste (_unordered list_)
> * Das Element `<li></li>` steht für einen Listeneintrag (_list_)
> * Das Element `<a></a>` steht für einen Link (_anchor_)
> * Erst nachdem Sie eine Vorstellung über das Aussehen der Webseite haben, öffnen Sie die Datei mit Ihrem Webbrowser (i.d.R. durch einen Doppelklick).
