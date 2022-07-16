import os
import glob
import htmlmin
import minify_html

dir_path = "htmls/*.html"
file_list = glob.glob(dir_path)

for f in file_list:
    with open(f, 'r', encoding="utf-8") as fl:
        html_txt = fl.read()
    
    fbase = os.path.basename( f )
    print(fbase)
    html_min1 = htmlmin.minify( html_txt, remove_comments=True, remove_empty_space=True)
    html_min2 = minify_html.minify( html_txt, minify_css=True, minify_js=True )
    
    with open( os.path.join("htmlmin", fbase), 'w', encoding='utf-8-sig') as fl:
        fl.write( html_min1 )
        
    with open( os.path.join("minify_html", fbase), 'w', encoding='utf-8-sig') as fl:
        fl.write( html_min2 )
    