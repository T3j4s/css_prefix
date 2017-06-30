import re,sqlite3,sys

output_file="should_make_compatible.css"

def find_browser(l):
    if l.find("-webkit-")!=-1:
        return "-webkit-"
    elif l.find("-moz-")!=-1:
        return "-moz-"
    elif l.find("-ms-")!=-1:
        return "-ms-"
    elif l.find("-o-")!=-1:
        return "-o-"
    else:return ""


def function_styler(v):
	pass
    

def property_styler(l,conn, wf):
    l=l.strip()
    
    for stm in l.split(";"):
        brw=find_browser(stm)
        tm=re.match(brw+"(.+):(.+)",stm)
        out=""
        if tm:
            p, v= tm.groups()
            query="select cs,es,ies,fs,ss,os from p_table where property='"+p+"';"
            cursor=conn.execute(query)
            out+= p+":"+v+";\n"
            for r in cursor:
                webkit_there=False
                for c in r:
                    if c!="S" and c!="N":
                        if c=="-webkit-" and webkit_there==True:
                            pass
                        else:out+= c+p+":"+v+";\n"
                        if c=="-webkit-":webkit_there=True
        else :
            out+= stm
        
        wf.write(out+"\n")
def help():
    global output_file
    print sys.argv[0], "is a tool for managing/adding vendor prefixes to the css-selectors.\n"
    print "Usage : \t", sys.argv[0], " <file.css>\n"
    print "Generate output file :", output_file, "\n"

def main():
    global output_file
    conn=None
    read_f=None
    write_f=None
    if len(sys.argv)==1 or sys.argv[1]=="-h" or sys.argv[1]=="--help":
        help()
        exit(1)
    
    try:
        #connect to the CSS_data.db to get info regarding the vendor-prefixes
        conn=sqlite3.connect("CSS_data.db")
        #open the file for reading
        read_f=open(sys.argv[1], "r")
        #open the file to write to.
        write_f=open(output_file, "w")
    except:
        print "Not able to open the file."
        exit(-1)

    for l in read_f.readlines():
        property_styler(l, conn, write_f)

    read_f.close()
    write_f.close()
    conn.close()
    print "Done Generated file : ", output_file, "\n" 

main()
