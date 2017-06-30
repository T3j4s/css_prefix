# css-prefix
A Python-based command line tool which automatically add's vendor prefixes to a .css file.
>Supported python version :2.7.*
## Description 
***css-prefix*** takes an option .css file_name as an input an add's vendor-prefixes to all of its selectors and outputs this changes into the newly genrated file "should_make_compatible.css"

>supported vendor-prefixes [-webkit-, -moz-, -ms- or -o-]
#### Example
A test.css file which need's vendor-prefixes
```sh
div {
	column-count: 3;
	background: red;width:300px;
	
	-webkit-animation: 2s infinite;
	background: linear-gradient(red,yellow,blue);
}
```
Passing the 'test.css' file as argument/option to the tool
```sh
$ python css-prefix.py test.css
Done Generated file :  should_make_compatible.css
```

Cheaking the genrated file 
```sh
$ cat should_make_compatible.css
div {
column-count: 3;
-webkit-column-count: 3;
-moz-column-count: 3;


background: red;

width:300px;



animation: 2s infinite;
-webkit-animation: 2s infinite;
-moz-animation: 2s infinite;


background: linear-gradient(red,yellow,blue);


}
```
***done***
