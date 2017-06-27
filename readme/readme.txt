Plugin for CudaText.
Gives commands for HTML/CSS work (lexer name can be any).

--------------------------  
* commands to preview current HTML text in web browser.
  2 commands (new tab/ new window) for current browser and per each major browser 
  (Firefox/Chrome/Safari/Opera/Windows-default).
  
  for selection, only selection is previewed, and a temp-file is created (_cudatext_preview.html),
  in the same folder as original file (so temp file can see relative HTML links).

--------------------------  
* commands to wrap selection in HTML tag.
  commands for about 25 tags.
  e.g. "text" -->  "<b>text</b>"

--------------------------  
* command, to do the same as Sublime Text does on hotkey Alt+Shift+W:

  on selection: wrap selection with <p></p> and place 2 selections to rename tag
  w/o selection: add <p></p> with 2 selections and 2 markers:
    1st TAB press goes into tag,
    2nd TAB press goes after tag

--------------------------  
* command, which converts selected value between "px" and "rem" units.
  it works only if selection is number + "px" or "rem", and changes selection
  between "px" and "rem" value. it leaves only 4 digits of float-number after dot.
  for ex, 10px -> 0.625rem -> 10.0px.
  idea: user "nmsalinas", site: www.nevermindhttp.com

--------------------------  
* function of plugin "HTML Image Tag".
  Command to choose image file (jpeg, png, gif), and inserts image info into code. 

  For CSS lexer (and several CSS based lexers: scss, sass, stylus) it inserts such text:

    background: url("path/file.png");
    width: 70px;
    height: 70px;

  For other lexers (assumed it's HTML) it inserts HTML <img> tag:

    <img src="path/file.png" width="70" height="70" alt="untitled" />

  It replaces full path of image to short path "fn.png" or "subfolder/fn.png"
  if image file is in the editor file's subfolder.

--------------------------  
* function of plugin "HTML Lines To List". 
  commands "Convert lines to list", convert several selected lines to:
  - ordered list <ol> ... </ol>    
  - unordered list <ul> ... </ul>
  - table <table>, arrange cells by lines    
  - table <table>, arrange cells by columns
      
--------------------------
* function of plugin "HTML Validator".
  Items to check current document via online checkers: HTML4/HTML5.
  Automatic format detection often fails, so you have to manually choose it.
  It shows results in Validate panel (in the bottom panel), you can double-click result 
  lines to go to error.

--------------------------
* function of plugin "Increment".
  2 commands to increase/decrease number under caret. 
  Numbers in CSS/HTML supported: 100px, 1.200em. 
  Float numbers supported (dot must be used).
  Multi-carets supported: all numbers for all carets affected.

--------------------------
* event for HTML lexers (any lexer name with "HTML" word):
  Enter key press between opening/closing tag, makes smart indent:

    <tag>|</tag>
    converts to
    <tag>
      |
    </tag>
  
    <a href="#GlossTop">|Top</a>
    converts to
    <a href="#GlossTop">
      |Top
    </a>
  

Author: Alexey T. (CudaText)
License: MIT
