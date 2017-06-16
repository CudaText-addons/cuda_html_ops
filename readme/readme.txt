Plugin for CudaText.
Gives commands for HTML/CSS work (lexer name can be any).

--------------------------  
* commands (new tab/window) to open current HTML text in current web browser. 
  it is the function of plugin HTML Preview. 
  for selection: only selection is used, and a temp-file is created, in the same folder as original
  (_cudatext_preview.html).

--------------------------  
* commands to wrap selection in HTML style tag: <b>, <i>, <u>.
  for ex, "text" -->  "<b>text</b>"

--------------------------  
* command, to do the same as Sublime Text does on hotkey Alt+Shift+W:

  with selection: wrap selection with <p></p> and place 2 selections to rename tag
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
* function of plugin "Image Tag".
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
    

Author: Alexey T. (CudaText)
License: MIT
