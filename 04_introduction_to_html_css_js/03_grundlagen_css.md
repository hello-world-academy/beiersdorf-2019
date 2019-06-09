# Grundlagen CSS

Wie HTML ist auch Cascading Style Sheets (CSS) keine Programmiersprache aber eine _Stylesheet_ Sprache. Mit ihr kann man einzelne Elemente eines HTML Dokumentes formatieren. Um alle Absatzelemente (`<p>`) in einem HTML Dokument in roter Textfarbe darzustellen schreibt man in CSS Folgendes:

```
p {
  color: red;
}
```

In der Regel erstelle man eine eigene CSS Datei (z.B. `style.css`) und referenziert diese innerhalb des `<head>` _tags_ im HTML Dokument.

`<link href="styles/style.css" rel="stylesheet" type="text/css">`


## Anatomie von CSS 

Die Formatierung durch CSS basiert auf Regeln. Der Name des zu formatierenden HTML Elementes (_Selector_) steht immer am Anfang der Regel (z.B. `p`).
Eine Regel wie `color: red;` führt dazu das selektierte Element in der Farbe Rot dargestellt wird. Die korrekte Syntax ist herbei sehr wichtig:

* Jede Regel wird durch die geschwungenen Klammern umschlossen `{}`.
* Der Doppelpunkt `:` trennt die Eigenschaft (z.B. `color`) vom Wert (z.B. `red`).
* Das Semikolon (`;`) trennt die Deklarationen von einander.

```
p {
  color: red;
  width: 500px;
  border: 1px solid black;
}
```

Es bestehen verschiedene Möglichkeiten einzelne Elemente oder Gruppen von Elementen anzusprechen:

```
p, li, h1 {
  color: red;
}
```

Darüber hinaus kann man einzelne Elemente auch unterschiedlich ansprechen:

* _Name_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `p`
* _ID_ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `#my-id`
* Klasse &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`.my-class`
* Attribute &nbsp;&nbsp;&nbsp; `img[src]`
* Status &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `a:hover`

Darüber hinaus gibt es noch viele weitere Möglichkeiten mit CSS einzelne Elemente anzusprechen ([siehe hier](https://www.w3schools.com/cssref/css_selectors.asp)). 

### _Denken in Blöcken_

Bei der Definition der CSS Regeln geht es sehr of darum Boxen zu formatieren (Größe, Farbe, Position, etc). Es kann helfen Elemente eines HTML Dokumets als Boxen zu denken die neben- und übereinander existieren können (_box model_). Mit diesem Modell vor Augen sind Eigenschaften wie `padding`, `border` und `margin` besser zu verstehen. 

<img src='_img/box-model.png' width='100%'>

****
## Übung 3

> __Öffnen Sie die CSS Datei `04_introduction_to_html_css_js/html/styles/style.css` mit einem Texteditor Ihrer Wahl und versuchen die Formatierungsregeln nachzuvollziehen.__

***
## Übung 4

> __Öffnen Sie das HTML Dokument `04_introduction_to_html_css_js/html/03-css-uebung.html` mit einem Texteditor Ihrer Wahl.__
> Es gilt in der Datei zwei kleine Änderungen zwischen den _tags_ `<head>` zu beachten.  
>  1. `<link href="http://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet" type="text/css">`. Hier verweisen wir auf eine Internetquelle, die uns die Schriftart _Open Sans_ zur Verfügung stellt.
> 2. `<link href="styles/style.css" rel="stylesheet" type="text/css">` Hier verweisen wir auf die lokale `.css` Datei, die unsere spezifischen Formatregeln beinhaltet.
> * Abschließend öffnen Sie bitte die Datei `04_introduction_to_html_css_js/html/03-css-uebung.html` mit Ihrem Webbrowser (i.d.R. durch einen Doppelklick) und versuchen Sie die visuellen Veränderungen den jeweiligen Regeln zuzuordnen.
 
***
