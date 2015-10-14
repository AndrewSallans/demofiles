from text.blob import TextBlob as tb

colors = {
	1: "892EE4",
	0.9: "#9B4EE9",
	0.8: "#A55FEB",
	0.7: "#AE70ED",
	0.6: "#AE70ED",
	0.5: "#C79BF2",
	0.4: "#CEA8F4",
	0.3: "#DBBFF7",
	0.2: "#E1CAF9",
	0.1: "#EDDFFB",
	0: "#F5EEFD",
	-0.1: "#FFF2F2",
	-0.2: "#FFECEC",
	-0.3: "#FFDFDF",
	-0.4: "#FFCECE",
	-0.5: "#FFBBBB",
	-0.6: "#FFA8A8",
	-0.7: "#FF9797",
	-0.8: "#FF8A8A",
	-0.9: "#FF7575",
	-1:	"#FF4848"
}

tb(pos).words
html = ""
for word in tb(pos).words:
    try:
        html += '<font color="{0}">{1}</font>'.format(colors[round(tb(word).polarity,1)], word)
    except: 
        html += '<font color="#F5EEFD">{0}</font>'.format(word)
    
print html

changes to file in github
