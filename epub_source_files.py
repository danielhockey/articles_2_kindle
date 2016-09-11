chapter_content = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?><html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Chapter 1</title>

<meta content="http://www.w3.org/1999/xhtml; charset=utf-8" http-equiv="Content-Type"/>
<link href="../Styles/stylesheet.css" rel="stylesheet" type="text/css"/>
</head>

<body class="mainbody">
  <div class="paragraphtext">

	<h1>
		{0}
	</h1>
	<h2>{1}</h2>
	<br/><br/>
	{2}</p>

  </div>
</body>
</html>'''

toc_ncx_content = '''		<navPoint class="chapter" id="{0}" playOrder="{1}">
			<navLabel>
				<text>{0}</text>
			</navLabel>
			<content src="Text/{0}.xhtml"/>
		</navPoint>\n\n<NAVSTART>'''

content_opf_default = '''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="uuid_id" version="2.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:opf="http://www.idpf.org/2007/opf" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <dc:title>Scientific American</dc:title>
        <dc:language>en</dc:language>
        <dc:identifier id="uuid_id" opf:scheme="uuid">isbn-000-0-000-00000-0</dc:identifier>
        <dc:creator>Daniel Hockey</dc:creator>
        <dc:publisher>D.H.</dc:publisher>
        <dc:date>2013-08-17</dc:date>
        <meta name="cover" content="my-cover-image"/>
    </metadata>
    <manifest>
        <item href="Text/bookcover.xhtml" id="bookcover" media-type="application/xhtml+xml"/>
        <item href="Text/title.xhtml" id="title" media-type="application/xhtml+xml"/>
        <item href="Text/copyright.xhtml" id="copyright" media-type="application/xhtml+xml"/>
        <item href="Text/toc.xhtml" id="toc" media-type="application/xhtml+xml"/>
        <item href="Styles/stylesheet.css" id="cascadingstylesheet" media-type="text/css"/>
        <item href="toc.ncx" id="tableofcontents" media-type="application/x-dtbncx+xml"/>
		<MANIFEST>
    </manifest>
    <spine toc="tableofcontents">
        <itemref idref="bookcover" linear="no"/>
        <itemref idref="title"/>
        <itemref idref="copyright"/>
		<SPINE>
    </spine>
    <guide>
        <reference href="Text/bookcover.xhtml" title="Cover Image" type="cover"/>
        <reference href="Text/toc.xhtml" title="Table Of Contents" type="toc"/>
		<GUIDE>
    </guide>
</package>'''

toc_ncx_default = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?><ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en">
	<head>
		<meta content="isbn-000-0-000-00000-0" name="dtb:uid"/>
		<meta content="2" name="dtb:depth"/>
		<meta content="0" name="dtb:totalPageCount"/>
		<meta content="0" name="dtb:maxPageNumber"/>
	</head>
	<docTitle>
		<text>Scientific American</text>
	</docTitle>
	<navMap>
		<navPoint class="chapter" id="title" playOrder="1">
			<navLabel>
				<text>Title Page</text>
			</navLabel>
			<content src="Text/title.xhtml"/>
		</navPoint>

<NAVSTART>

	</navMap>
</ncx>'''

stylesheet = '''@namespace h "http://www.w3.org/1999/xhtml";
.mainbody {
    display: block;
    font-size: 1em;
    margin-bottom: 5pt;
    margin-left: 5pt;
    margin-right: 5pt;
    margin-top: 5pt;
    padding-left: 0;
    padding-right: 0;
    text-align: justify;
    }
.paragraphtext {
    display: block;
    }
.leftaligntext {
    display: block;
    text-align: left;
    }
.centeraligntext {
    display: block;
    text-align: center;
    }
h1 {
    display: block;
    text-align: center;
    font-weight: bold;
    font-size: 125%;
    }
.photovariables {
	margin-right: 5px;
	float: left;
    }
.bookblock {
	position: relative;
	margin-bottom: 80px;
    }
p {
	margin: 0px;
	padding: 0px;
	text-indent: 2em;
	} '''

title_default = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?><html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Scientific American</title>

<meta content="http://www.w3.org/1999/xhtml; charset=utf-8" http-equiv="Content-Type"/>
<link href="../Styles/stylesheet.css" rel="stylesheet" type="text/css"/>
</head>

<body class="mainbody">
  <div class="centeraligntext">

	<h1>
	Scientific American
	</h1>


	by D.H.


  </div>
</body>
</html>'''

toc_xhtml_default = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?><html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Table of Contents</title>

<meta content="http://www.w3.org/1999/xhtml; charset=utf-8" http-equiv="Content-Type"/>
<link href="../Styles/stylesheet.css" rel="stylesheet" type="text/css"/>
</head>

<body class="mainbody">
  <div class="paragraphtext">

	<h1>
		Table Of Contents
	</h1>
	<br/><br/>


<div class="centeraligntext">

<h2>Scientific American/h2>
<h3>by John Doe</h3>

</div>

<br/><br/>


<a href="../Text/title.xhtml">Scientific American</a>

<br/>

<TOC>

  </div>
</body>
</html>'''

copyright = '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?><html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Copyright</title>

<meta content="http://www.w3.org/1999/xhtml; charset=utf-8" http-equiv="Content-Type"/>
<link href="../Styles/stylesheet.css" rel="stylesheet" type="text/css"/>
</head>

<body class="mainbody">
  <div class="leftaligntext">

	<h1>
		Copyright &#169; 2013 D.H. All Rights Reserved.
	</h1>

	<br/><br/>

	Note all the information below is optional. Only the H1 tag above is required.

	<br /><br />

All rights reserved under the Digital Millennium Copyright Act, the Universal Copyright Convention and the Berne Convention For The Protection Of Literary And Artistic Works. The author of this book, John Doe, secures all rights to this book, including the right to reproduce this book in whole or in part, in any form whatsoever, and extends such privileges to absolutely no other parties, individuals or companies. Not including eBook exemptions of the Digital Millennium Copyright Act, no part of this book may be reproduced or transmitted in any form, in whole or in part, by any electronic, mechanical, or other means including, but not limited to, all existing and yet to be invented information duplicating, storage or retrieval systems, without specific permission in writing from the author, except by a reviewer who may quote brief passages.


  </div>
</body>
</html>'''

container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
   </rootfiles>
</container>'''