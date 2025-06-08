# OSINTScope Google Dorks

## SYMBOLS

- `"` **Quotes** Search for exact phrases.  
- `-` **Minus sign** Exclude terms from the search.  
- `*` **Asterisk (wildcard)** Acts as a placeholder for any word(s).  
- `OR` **Logical OR** Search for one term or another (must be uppercase).  
- `()` **Parentheses** Group terms or operators to structure the query.  
- `..` **Range operator** Search within a numeric range (e.g., dates, numbers).  
- `@` **At symbol** Often used to search for email addresses or social handles.  
- `\` **Escape character** Use before special characters to search them literally.  

## COMMON  
- `site:` Restrict search to a specific site or domain  
- `intitle:` Search for words in the page title  
- `allintitle:` All words must be in the title  
- `inurl:` Search for words in the URL  
- `allinurl:` All words must appear in the URL  
- `intext:` Search within the page text  
- `allintext:` All words must appear in the text  
- `filetype:` Search for specific file types (e.g., pdf, doc)  
- `cache:` View Google's cached version of a page  
- `link:` Find pages linking to a URL  
- `related:` Find sites similar to a URL  
- `define:` Find definitions of a term  

## SENSITIVE DATA 
- `filetype:pdf confidential` Search PDFs containing the word "confidential"  
- `filetype:xls intext:username password` Excel files containing username and password  
- `ext:cfg` Configuration files  
- `ext:conf intext:password` Configuration files containing passwords  
- `ext:bak` Backup files  
- `ext:old` Old files backups  
- `ext:backup` Backup files  
- `intitle:"index of" "parent directory"` Search for open directory listings  
- `inurl:/view.shtml` Possible exposed directory or file viewer  
- `inurl:.git` Exposed git repositories  
- `inurl:.env DB_PASSWORD` Environment files containing database passwords  
- `inurl:wp-config.php` WordPress config files (often contain sensitive info)  
- `inurl:config.php "DB_PASSWORD"` PHP config files with database password  
- `filetype:env intext:DB_HOST` Environment files with DB host info  
- `inurl:.git/config` Git configuration files  
- `inurl:credentials.json` Credentials files  
- `filetype:xml intext:password` XML files containing passwords  

## ACCESS PORTALS  
- `intitle:"login"` Login pages  
- `intitle:"admin login"` Admin login pages  
- `inurl:admin` URLs containing "admin"  
- `intitle:"admin panel"` Admin control panels  
- `inurl:wp-admin` WordPress admin area  
- `inurl:joomla/administrator` Joomla admin pages  
- `inurl:phpmyadmin intitle:"phpMyAdmin"` phpMyAdmin login pages  
- `inurl:adminlogin` Admin login URLs  
- `inurl:login.asp` Login pages with ASP  
- `inurl:auth` Authentication pages  
- `inurl:cpanel` cPanel login portals  
- `inurl:dashboard` Dashboard pages  
- `intitle:"sign in"` Sign in pages  
- `inurl:/user/login` User login URLs  

## ACCESSIBLE DIRECTORIES, FILE  
- `intitle:"index of" inurl:ftp` Open FTP directories  
- `intitle:"index of" backup` Backup folders indexed  
- `intitle:"index of" db.sql` Indexed database dump files  
- `inurl:backup.zip` Backup ZIP files  
- `inurl:db_backup` Database backup folders  
- `filetype:sql "insert into"` SQL files containing insert statements  
- `intitle:"Index of /apache/logs"` Apache logs directory  
- `filetype:log password` Log files mentioning passwords  
- `intitle:"index of" passwd` Indexed passwd files  
- `intitle:"index of" .git` Git folders indexed  
- `intitle:"index of" .ssh` SSH directories indexed  
- `intitle:"index of" .bash_history` Bash history files  
- `intitle:"index of" config` Config files indexed  

## NETWORKS, DEVICES EXPOSED  
- `intitle:"webcamXP 5"` WebcamXP software devices  
- `inurl:8080 intitle:"Router"` Routers on port 8080  
- `intitle:"DVR login"` Digital Video Recorder login pages  
- `intitle:"HP LaserJet" inurl:hp/device/this.LCDispatcher` HP LaserJet devices  
- `inurl:"/setup.cgi?next_file=netgear.cfg"` Netgear router config files  
- `intitle:"IP Camera"` IP cameras  
- `intitle:"webcam 7"` Webcam software 7 devices  
- `intitle:"Axis 2400"` Axis cameras  
- `intitle:"Live View / - AXIS"` Live view of AXIS cameras  
- `inurl:/view/index.shtml` Camera views or device panels  
- `inurl:8080 intitle:"Netgear router"` Netgear routers on port 8080  

## FOOTPRINTING  
- `site:example.com -www` Search a domain excluding www  
- `filetype:pdf site:example.com` PDFs on a domain  
- `site:example.com "@example.com"` Emails on the domain  
- `inurl:/config` Pages with config in URL  
- `intext:"You have an error in your SQL syntax"` Pages showing SQL errors  
- `site:gov` Government sites  
- `site:edu` Educational sites  
- `site:example.com filetype:doc` DOC files on a domain  
- `site:example.com inurl:login` Login pages on a domain  
- `site:example.com ext:xml` XML files on a domain  
- `intext:"powered by phpBB" site:example.com` phpBB powered sites  

## DEBUG, ERROR MESSAGES  
- `intext:"Warning: mysql_fetch"` MySQL warnings  
- `intext:"You have an error in your SQL syntax"` SQL syntax errors  
- `intext:"PHP Parse error"` PHP parsing errors  
- `intext:"Notice: Undefined variable"` PHP notices  
- `intext:"Fatal error"` Fatal errors  
