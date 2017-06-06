plugin for CudaText.
gives commands for HTML/CSS work (lexer name can be any).

1) commands to wrap selection in HTML tag: <b>, <i>, <u>.
  for ex, "text" ->  "<b>text</b>"
  
2) command, to do the same as Sublime Text does on hotkey Alt+Shift+W:
    on selection: wrap selection with <p></p> and place 2 selections to rename tag
    w/o selection: add <p></p> with 2 selections and 2 markers:
      1st TAB press goes into tag,
      2nd TAB press goes after tag

3) command, which converts selected value between "px" and "rem" units.
  it works only if selection is number + "px" or "rem", and changes selection
  between "px" and "rem" value. it leaves only 4 digits of float-number after dot.
  for ex, 10px -> 0.625rem -> 10.0px.
  idea: user "nmsalinas", site: www.nevermindhttp.com
    

author: Alexey (CudaText)
license: MIT
