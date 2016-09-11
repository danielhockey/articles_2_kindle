import urllib.request
import re
import os.path
import epub_source_files
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

path_to_script = os.path.dirname(os.path.abspath(__file__))
print(path_to_script)
######

os.makedirs(path_to_script+str('/META-INF'), exist_ok=True)
os.makedirs(path_to_script+str('/OEBPS'), exist_ok=True)
os.makedirs(path_to_script+str('/OEBPS/Styles'), exist_ok=True)
os.makedirs(path_to_script+str('/OEBPS/Images'), exist_ok=True)
os.makedirs(path_to_script+str('/OEBPS/Text'), exist_ok=True)

######

def make_default_file(dir, file, content_for_file):
    with open(str(dir)+str(file), 'w') as file:
        file.write(content_for_file)
        file.close()

def parse_link(link):
    data = urllib.request.Request(link)
    data = urllib.request.urlopen(data)
    return data.read()

def remove_ugly_text(title):
    mapping = [('&quot;', '"'),("&amp;",''),('mdash;','--'),('nbsp;',''), ('\\',''),('&rsquo;','\'')]
    for k,v in mapping:
        title = title.replace(k,v)
    return title

def remove_ugly_text2(title):
    mapping = [('&quot;', '"'),("&amp;",''),('&mdash;','--'),('nbsp;',''),('&rsquo;','\''),('&ldquo;',''),
               ('&rdquo;',''),('&',' ')]
    for k,v in mapping:
        title = title.replace(k,v)
    return title

def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

######

data = parse_link('http://www.scientificamerican.com/section/lateststories/?page=1')
links = re.findall(r'article/(.*?)/"', str(data)) # Finds links to articles
links = set(list(map(lambda x: 'http://www.scientificamerican.com/article/'+str(x), links))) # Fixes url address

playorder = 2 # toc.ncx

###### Clean up later ..

make_default_file(path_to_script, '/mimetype', 'application/epub+zip')
make_default_file(path_to_script+str('/META-INF/'), 'container.xml', epub_source_files.container_xml)
make_default_file(path_to_script+str('/OEBPS/'), 'content.opf', epub_source_files.content_opf_default)
make_default_file(path_to_script+str('/OEBPS/'), 'toc.ncx', epub_source_files.toc_ncx_default)
make_default_file(path_to_script+str('/OEBPS/Styles/'), 'stylesheet.css', epub_source_files.stylesheet)
make_default_file(path_to_script+str('/OEBPS/Text/'), 'title.xhtml', epub_source_files.title_default)
make_default_file(path_to_script+str('/OEBPS/Text/'), 'toc.xhtml', epub_source_files.toc_xhtml_default)
make_default_file(path_to_script+str('/OEBPS/Text/'), 'toc.xhtml', epub_source_files.toc_xhtml_default)
make_default_file(path_to_script+str('/OEBPS/Text/'), 'copyright.xhtml', epub_source_files.copyright)
make_default_file(path_to_script+str('/OEBPS/Text/'), 'cover.xhtml', '')
make_default_file(path_to_script+str('/OEBPS/Text/'), 'backcover.xhtml', '')

######

for link in links:

    article_page = parse_link(str(link))

    header_1 = (re.findall(r'"og:title" content="(.*?)" ', str(article_page)))[0]
    header_1 = remove_ugly_text(header_1)

    header_2 = (re.findall(r'"og:description" content="(.*?)" ', str(article_page)))[0]
    header_2 = remove_ugly_text(header_2)

    article = re.findall(r'="article-block article-text">(.*?)</p></div>', str(article_page))[0]
    article = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b|</a>|<link(.*?)/>|<a href="(.*?)>|(\\r)|(\\n)|(\\\\n)|(\\\\r)', '', str(article), flags=re.MULTILINE)
    article = remove_ugly_text2(article)

    full_path_location_chapter = os.path.join(path_to_script+str('/OEBPS/Text'), str(header_1)+'.xhtml')
    with open(full_path_location_chapter, 'w+') as file:
        file.write(epub_source_files.chapter_content.format(header_1,header_2,article))

    ###### CONTENT.OPF

    full_path_location_opf = os.path.join(path_to_script+str('/OEBPS'), 'content.opf')

    manifest_string = '''<item href="Text/{0}.xhtml" id="{1}" media-type="application/xhtml+xml"/>\n\t\t<MANIFEST>'''.format(str(header_1),str(header_1))
    spine_string = '''<itemref idref="{0}"/>\n\t\t<SPINE>'''.format(str(header_1))
    guide_string = '''<reference href="Text/{0}.xhtml" title="{0}" type="toc"/>\n\t\t<GUIDE>'''.format(str(header_1))
    inplace_change(full_path_location_opf, '<MANIFEST>', manifest_string)
    inplace_change(full_path_location_opf, '<SPINE>', spine_string)
    inplace_change(full_path_location_opf, '<GUIDE>', guide_string)

    ###### TOC.XHTML

    full_path_location_tocxhtml = os.path.join(path_to_script+str('/OEBPS/Text'), 'toc.xhtml')
    toc_string_replace = '''<a href="../Text/{0}.xhtml">{0}</a>\n\n<br/>\n\n<TOC>'''.format(str(header_1))
    inplace_change(full_path_location_tocxhtml, '<TOC>', toc_string_replace)

    ###### TOC.ncx

    full_path_location_tocncx = os.path.join(path_to_script+str('/OEBPS'), 'toc.ncx')
    tocnxc_string_replace = epub_source_files.toc_ncx_content.format(str(header_1), str(playorder))
    inplace_change(full_path_location_tocncx, '<NAVSTART>', tocnxc_string_replace)

    print(str(playorder-1) + ': ' + header_1)
    playorder += 1

###### Remove extensions in files and zip + rename

inplace_change(full_path_location_opf, '<MANIFEST>', '')
inplace_change(full_path_location_opf, '<SPINE>', '')
inplace_change(full_path_location_opf, '<GUIDE>', '')
inplace_change(full_path_location_tocxhtml, '<TOC>', '')
inplace_change(full_path_location_tocncx, '<NAVSTART>', '')

os.system("zip -r test.zip mimetype OEBPS META-INF | mv test.zip test.epub")
os.system('ebook-convert test.zip test.mobi')

#######
#######
#######

fromaddr = "FROM_EMAIL_ADDRESS"
toaddr = "TO_EMAIL_ADDRESS@kindle.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = ""

body = ""

msg.attach(MIMEText(body, 'plain'))

filename = "test.mobi"
attachment = open(path_to_script+str(' a/test.mobi'), "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
