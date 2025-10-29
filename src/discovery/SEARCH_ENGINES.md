> add yaml so that each can be incorporated as normal
> but also make a custom html block that acts like discovery oasis
> select which search engines to use then open new tabs with the search queries already populated

- [Google](http://google.com)
  - input text
  - window.open('http://google.com/search?q=' + Search01, 'Search01window');

- [Google Date](http://google.com)
  - input text
  - window.open('http://google.com/search?q=' + Search02 + '&tbs=cdr:1,cd_min:1/1/0,sbd:1', 'Search02window');

- [Google News](http://www.google.com)
  - input text
  - window.open('http://www.google.com/search?tbm=nws&q=' + Search03, 'Search03window');

- [Google FTP](https://www.google.com)
  - input text
  - window.open('https://www.google.com/search?q=inurl%3Aftp%20-inurl%3A(http|https)%20' + Search05, 'Search05window');

- [Google Index](https://www.google.com)
  - input text
  - window.open('https://www.google.com/search?q=intitle%3Aindex.of+' + Search06, 'Search06window');

- [Google Scholar](http://scholar.google.com)
  - input text
  - window.open('http://scholar.google.com/scholar?&q=' + Search07, 'Search07window');

- [Google Patents](https://patents.google.com)
  - input text
  - window.open('https://patents.google.com/?q=' + Search08, 'Search08window');

- [Bing](http://bing.com)
  - input text
  - window.open('http://bing.com/search?q="' + Search09 + '"', 'Search09window');

- [Bing News](http://bing.com)
  - input text
  - window.open('http://bing.com/news/search?q="' + Search10 + '"', 'Search10window');

- [Yahoo](http://search.yahoo.com)
  - input text
  - window.open('http://search.yahoo.com/search?p=' + Search11, 'Search11window');

- [Yandex](http://www.yandex.com)
  - input text
  - window.open('http://www.yandex.com/yandsearch?text=' + Search12, 'Search12window');

- [Baidu](http://baidu.com)
  - input text
  - window.open('http://baidu.com/s?wd=' + Search13, 'Search13window');

- [Searx](https://baresearch.org)


```YAML
tool_info:
    name: Searx Instance
    type: web
    usage_url: baresearch.org
    info_url: https://github.com/searxng/searxng
tool_cmd:
    login: false
    js: function doSearch14(Search14)
{window.open('https://baresearch.org/?q=' + Search14, 'Search14window');}
    target_info: fullname, phonenumber, firstname, lastname
    target_info_opt: dob, address
    # autopopulate use of given info type in a profile, if multiple of a type, like a phonnumber, then drop down menu listing all phonenumbers
    # comma deliminated info types, if multiple then generate more fields on rendering site, and each field has a dropdown if multiple
   # optional targeted info does not require its field to be populated to run the tool/search
```

- [DuckDuckGo](https://duckduckgo.com)
  - input text
  - window.open('https://duckduckgo.com/?q=' + Search16, 'Search16window');

- [StartPage](https://startpage.com)
  - input text
  - window.open('https://startpage.com/do/search?q=' + Search17, 'Search17window');

- [Qwant](https://www.qwant.com)
  - input text
  - window.open('https://www.qwant.com/?q=' + Search18, 'Search18window');

- [Brave](https://search.brave.com)
  - input text
  - window.open('https://search.brave.com/search?q=' + Search19, 'Search19window');

- [Wayback](https://web.archive.org)
  - input text
  - window.open('https://web.archive.org/web/*/' + Search20, 'Search20window');

- [Ahmia](https://ahmia.fi)
  - input text
  - window.open('https://ahmia.fi/search/?q=' + Search21, 'Search21window');

- [Onion - Tor.link](https://tor.link)
  - input text
  - window.open('https://tor.link/?q=' + Search37, 'Search37window');

- [Onion - Torch](http://torch4st4l57l2u2vr5wqwvwyueucvnrao4xajqr2klmcmicrv7ccaad.onion)
  - input text
  - window.open('http://torch4st4l57l2u2vr5wqwvwyueucvnrao4xajqr2klmcmicrv7ccaad.onion/search?query=' + Search23 + '&action=search', 'Search23window');

- [Onion - Tor66](http://www.tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion)
  - input text
  - window.open('http://www.tor66sewebgixwhcqfnp5inzp5x5uohhdy3kvtnyfxc2e5mxiuh34iid.onion/search?q=' + Search24, 'Search24window');

- [Onion - Haystack](http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion)
  - input text
  - window.open('http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q=' + Search25, 'Search25window');

- [Onion - Ahmia](http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion)
  - input text
  - window.open('http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q=' + Search26, 'Search26window');

- [Onion - SearchDemon](http://srcdemonm74icqjvejew6fprssuolyoc2usjdwflevbdpqoetw4x3ead.onion)
  - input text
  - window.open('http://srcdemonm74icqjvejew6fprssuolyoc2usjdwflevbdpqoetw4x3ead.onion/search?q=' + Search27, 'Search27window');

- [Onion - Excavator](http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion)
  - input text
  - window.open('http://2fd6cemt4gmccflhm6imvdfvli3nf7zn6rfrwpsy7uhxrgbypvwf5fad.onion/search/' + Search28, 'Search28window');

- [Onion - GDark](http://zb2jtkhnbvhkya3d46twv3g7lkobi4s62tjffqmafjibixk6pmq75did.onion)
  - input text
  - window.open('http://zb2jtkhnbvhkya3d46twv3g7lkobi4s62tjffqmafjibixk6pmq75did.onion/gdark/search.php?query=' + Search29 + '&search=1', 'Search29window');

- [Onion - Hidden Reviews](http://u5lyidiw4lpkonoctpqzxgyk6xop7w7w3oho4dzzsi272rwnjhyx7ayd.onion)
  - input text
  - window.open('http://u5lyidiw4lpkonoctpqzxgyk6xop7w7w3oho4dzzsi272rwnjhyx7ayd.onion/?s=' + Search30, 'Search30window');

- [Onion - OnionLand](http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion)
  - input text
  - window.open('http://3bbad7fauom4d6sgppalyqddsqbf5u5p56b5k5uk2zxsy3d6ey2jobad.onion/search?q=' + Search31, 'Search31window');

- [Onion - Phobos](http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion)
  - input text
  - window.open('http://phobosxilamwcg75xt22id7aywkzol6q6rfl2flipcqoc4e4ahima5id.onion/search?query=' + Search32, 'Search32window');

- [Onion - Submarine](http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion)
  - input text
  - window.open('http://no6m4wzdexe3auiupv2zwif7rm6qwxcyhslkcnzisxgeiw6pvjsgafad.onion/search.php?term=' + Search33, 'Search33window');

- [Onion - DeepSearch](http://searchgf7gdtauh7bhnbyed4ivxqmuoat3nm6zfrg3ymkq6mtnpye3ad.onion)
  - input text
  - window.open('http://searchgf7gdtauh7bhnbyed4ivxqmuoat3nm6zfrg3ymkq6mtnpye3ad.onion/search?q=' + Search34, 'Search34window');

- [Onion - OnionCenter](http://5qqrlc7hw3tsgokkqifb33p3mrlpnleka2bjg7n46vih2synghb6ycid.onion)
  - input text
  - window.open('http://5qqrlc7hw3tsgokkqifb33p3mrlpnleka2bjg7n46vih2synghb6ycid.onion/index.php?a=search&q=' + Search35, 'Search35window');

- [Onion - FreshOnion](http://freshonifyfe4rmuh6qwpsexfhdrww7wnt5qmkoertwxmcuvm4woo4ad.onion)
  - input text
  - window.open('http://freshonifyfe4rmuh6qwpsexfhdrww7wnt5qmkoertwxmcuvm4woo4ad.onion/?query=' + Search36, 'Search36window');



## SEARCH ENGINES

- [Google Advanced Search](https://www.google.com/advanced_search)
- [MetaGer: Privacy Protected Search](https://metager3.de/en)
- [Search Engines Index](https://www.searchenginesindex.com)
- [carrot2](https://search.carrot2.org/#/search/web)
- [Startpage](https://startpage.com)
- [Crossref](https://search.crossref.org)
- [Yahoo Search](https://search.yahoo.com)
- [Ecosia](https://www.ecosia.org)
- [Dogpile](https://www.dogpile.com)
- [Zoo Search](https://www.metacrawler.com)
- [App Store and iTunes search engine](https://fnd.io)
- [Ask](https://www.search.ask.com)
- [ZorexEye](https://zorexeye.com)
- [keys.openpgp.org](https://keys.openpgp.org)
- [MIT PGP Key Server](https://pgp.mit.edu)
- [Ipfs-search.com](https://ipfs-search.com/#/search)
- [Debate.cards](https://debate.cards)
- [Argumentsearch.com](https://argumentsearch.com)
- [Meganzsearch.com](https://www.meganzsearch.com)
- [Engine.presearch.org](https://engine.presearch.org)
- [Blockscan.com](https://blockscan.com)
- [Publc.com](https://publc.com)
- [CachedViews.com](https://cachedviews.com)
- [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)
- [Google & Bing](https://one-plus.github.io/GoogleBing)
- [Libgen.rs](https://libgen.rs)
- [Stacksearch](https://stacksear.ch)
- [SearchTempest](https://www.searchtempest.com)
- [2lingual](https://2lingual.com)
- [Milled](https://milled.com/search)
- [btdig](https://btdig.com)
- [Monster Crawler Search](https://monstercrawler.com)
- [Arabo.com](https://arabo.com)
- [WordPress.com](https://en.search.wordpress.com)
- [Octosearch.dootech.com](https://octosearch.dootech.com)
- [Search craigslist](https://searchcraigslist.org)
- [Public Buckets](https://osint.sh/buckets)
- [Search Atlas](https://searchatlas.org)
- [Dorki](https://dorki.io)
- [Hackxy](https://hackxy.io)

### Universal search tools

- [S](https://github.com/zquestz/s)
- [searchall.net](https://searchall.net)
- [Query-server](https://query-server.herokuapp.com)
- [Search Engines Scraper](https://github.com/tasos-py/Search-Engines-Scraper)
- [Trufflepiggy (Context Search)](https://chrome.google.com/webstore/detail/trufflepiggy-context-sear/chffnhocnckigoapjdienmaphjnljpmo)
- [Search Patterns](https://chrome.google.com/webstore/detail/search-patterns/hjlahhonnlceifaecpjejlhhgjkipnbj/related?hl=zh-CN&gl=001)
- [Searcher](https://github.com/davemolk/searcher)
- [Startpage Parser](https://github.com/knassar702/startpage-parser)
- [BigSearch](https://github.com/garywill/BigSearch)


### Filesharing Search Engines

- [Filesearching](https://filesearching.com)
- [Snowfl.com](https://snowfl.com)
- [Torrents.me](https://torrends.to)
- [Open Directory Finder](https://ewasion.github.io/opendirectory-finder/#)
- [Mamont's open FTP indexer](https://www.mmnt.net)
- [Orion Media Indexer](https://orionoid.com)
- [Sunxdcc](https://sunxdcc.com)
- [Xdcc.eu](https://www.xdcc.eu)
- [DDL Search](https://ddlsearch.free.fr)
- [Sharedigger](https://www.sharedigger.com)
- [Xtorx](https://www.xtorx.com)
- [Torrent Seeker](https://torrentseeker.com)
- [FreeWare web FTP file search](https://www.freewareweb.com/ftpsearch.shtml)
- [Search 22](https://search-22.com/ftp-search-tools)
- [Heystack](https://heystacks.com)
- [DuckDuckGo !bangs](https://chrome.google.com/webstore/detail/duckduckgo-bangs/hdjfebkndhmegijlghjcdghdbealibeb/related)
- [DDGR](https://github.com/jarun/ddgr)
- [Google Search Scraper](https://apify.com/apify/google-search-scraper)
- [Googler](https://github.com/jarun/googler)
- [goosh.org](https://goosh.org)
- [Web Search Navigator](https://github.com/infokiller/web-search-navigator)
- [Overload Search](https://chrome.google.com/webstore/detail/overload-search-advanced/knihkdaajdhpjgeiadaefmjmpbnlojbg/related)
- [Google Autocomplete Scraper](https://tools.digitalmethods.net/beta/scrapeGoogle/autocomplete.php)
- [SDorker](https://github.com/TheSpeedX/SDorker)
- [XGS](https://github.com/XAMFRA/XGS)
- [http://onion.cab](https://onion.cab)
- [http://onion.city](https://onion.city)
- [https://onion.cab](http://onion.cab](https://onion.cab](http://onion.cab)
- [https://onion.city](http://onion.city](https://onion.city](http://onion.city)
- [Google Email Extractor](https://chrome.google.com/webstore/detail/google-email-extractor/aabpdmlmkpedpigeignclfmodjhplllj/related)
- [SEQE.me](https://seqe.me)
- [Bright Local Search Result Checker](https://www.brightlocal.com/local-search-results-checker)
- [Auto Searcher](https://chrome.google.com/webstore/detail/auto-searcher/hhggekcjcdgenbgejmkhineppclnkbkn/related)
- [I search from](https://isearchfrom.com)
- [Anon Scraper](https://github.com/370rokas/anonscraper)
- [Search Commands](https://chrome.google.com/webstore/detail/search-commands/ggjakfijchdkbmmhbfemjciidhnipgoe/related)
- [Boolean Builder theBalazs](https://docs.google.com/spreadsheets/d/1v27Oybrv9H5sn3MMD76clLp2B4mwhA7OtUkfQzlNu8w/edit#gid=940516593)
- [Yagooglesearch](https://github.com/opsdisk/yagooglesearch)
- [Google Word Sniper](https://googlewordsniper.eu)

### IOT (ip search engines)

- [TheLordEye](https://github.com/rlyonheart/thelordseye)
- [Quick Cache and Archive search](https://quickcacheandarchivesearch.onrender.com)
- [Trove](https://trove.nla.gov.au/search/category/websites)
- [Vandal](https://chrome.google.com/webstore/detail/vandal/knoccgahmcfhngbjhdbcodajdioedgdo/related)
- [https://archive.org](http://archive.org](https://archive.org](http://archive.org)
- [TheOldNet.com](https://theoldnet.com)
- [Carbon Dating The Web](https://carbondate.cs.odu.edu)
- [Archive.md](https://archive.md)
- [Webarchive.loc.gov](https://webarchive.loc.gov)
- [Swap.stanford.edu](https://swap.stanford.edu)
- [Wayback.archive-it.org](https://wayback.archive-it.org)
- [Vefsafn.is](https://vefsafn.is)
- [web.archive.bibalex.org](https://web.archive.bibalex.org)
- [Archive.vn](https://archive.vn)
- [UKWA](https://www.webarchive.org.uk)



### General Search Engines

- [Google](https://www.google.com/)
- [Bing](https://www.bing.com/)
- [Yahoo!](http://www.yahoo.com/)
- [Yandex](https://yandex.com/)
- [Ask](https://www.ask.com/)
- [Baidu](https://www.baidu.com/)
- [SearXNG](https://searx.be/?q=)
- [EXALead](http://www.exalead.com/search/web/)
- [DuckDuckGo](https://duckduckgo.com/)
- [Swisscows](https://swisscows.com/en)
- [Naver](https://www.naver.com/)
- [AOL](https://search.aol.com)
- [Brave](https://search.brave.com/)
- [Yep](https://yep.com/)
- [Gibiru](https://gibiru.com/)
- [Kagi](https://kagi.com/)
- [Stract](https://stract.com/)


### Files

- [Pastebin](https://pastebin.com/) - Website where you can store text online for a set period of time
- [Mega](https://mega.nz/) - Secure and private cloud storage for everyone. Store and share files, chat, meet, back up, sync, and more
- [4Shared](https://www.4s.io/) - Search, Store and Share easily. Upload, discover and share files without a hitch
- [files.fm](https://files.fm/discover) - Explore content shared by community
- [edisk.cz](https://www.edisk.cz/) - Online storage for backing up, sharing and searching for photos, videos, music and other files
- [doodstream](https://doodstream.com.tr/search-engine/) - DoodStream Search Engine
- [UVRX Search](http://www.uvrx.com/) - Most comprehensive online file storage search engine
- [filesearch.link](https://filesearch.link/) - You can search archives, programs, videos, music, books and more
- [RapidGators Search](https://rapidgators.net/file-search/) - Search for files stored on the rapidgator cloud


# Meta Search

- [100SearchEngines](https://www.100searchengines.com)
- [Bing vs. Google](https://bvsg.org)
- [https://bvsg.org](https://bvsg.org)
- [DADgogo](https://dadgogo.com)
- [https://dadgogo.com](https://dadgogo.com)
- [Etools](https://www.etools.ch)
- [https://www.etools.ch](https://www.etools.ch)
- [WebCrawler](https://www.webcrawler.com)
- [https://www.webcrawler.com](https://www.webcrawler.com)

# Code Search

- [Chromium Code Search](https://source.chromium.org/chromium)
- [Code Finder](https://codefinder.dev)
- [https://codefinder.dev](https://codefinder.dev)
- [codefinder org](https://codefinder.org)
- [https://codefinder.org](https://codefinder.org)
- [Android Code Search](https://cs.android.com)
- [CodeSeek](https://www.codeseek.co)
- [Debian Code Search](https://codesearch.debian.net)
- [https://codesearch.debian.net](https://codesearch.debian.net)
- [Scala](https://www.programcreek.com/scala)
- [SearchCode](https://searchcode.com)
- [SourceCodeOnline](https://www.sourcecodeonline.com)
- [https://www.sourcecodeonline.com](https://www.sourcecodeonline.com)
- [Woboq](https://code.woboq.org)
- [publicwww](https://publicwww.com)
- [https://publicwww.com](https://publicwww.com)
- [DevsecOps Secure Code](https://devsecopsguides.com/docs/rules)
- [awesomeopensource](https://awesomeopensource.com)
- [https://awesomeopensource.com](https://awesomeopensource.com)
- [nerdydata](https://www.nerdydata.com/reports/new)
- [Github code search](https://github.com/search?type=code)
- [sourcegraph](https://sourcegraph.com/search)
- [cybdetective code search](https://cybdetective.com/codesearch.html)
- [postman](https://www.postman.com/explore/collections)
- [swaggerhub](https://app.swaggerhub.com/search)
- [ecosyste](https://ecosyste.ms)
- [https://ecosyste.ms](https://ecosyste.ms)
- [wpdirectory](https://wpdirectory.net)
- [https://wpdirectory.net](https://wpdirectory.net)
- [launchpad](https://launchpad.net)
- [https://launchpad.net](https://launchpad.net)
- [snipplr](https://snipplr.com/all)



# Other Search Engines

- [criminalip](https://www.criminalip.io)
- [https://www.criminalip.io](https://www.criminalip.io)
- [us.searchboth.net](https://us.searchboth.net)
- [https://us.searchboth.net](https://us.searchboth.net)
- [Archive.org](https://www.arhive.org)
- [https://www.arhive.org](https://www.arhive.org)
- [Yandex](https://yandex.com)
- [Pastebin](https://www.pastebin.com)
- [https://www.pastebin.com](https://www.pastebin.com)
- [Topix.com](https://www.topix.com)
- [https://www.topix.com](https://www.topix.com)
- [Shodan](https://www.shodan.io)
- [https://www.shodan.io](https://www.shodan.io)
- [Piratebays](https://thepiratebays.com)
- [https://thepiratebays.com](https://thepiratebays.com)
- [Onesearch](https://www.onesearch.com)
- [https://www.onesearch.com](https://www.onesearch.com)
- [Searchencrypt](https://www.searchencrypt.com/home)
- [Duckgo](https://duckduckgo.com)
- [https://duckduckgo.com](https://duckduckgo.com)
- [Waymore](https://forum.seccodeid.com/d/waymore-find-way-more-from-the-wayback-machine)
- [StartPage](https://www.startpage.com)
- [https://www.startpage.com](https://www.startpage.com)
- [Searx](https://searx.space)
- [https://searx.space](https://searx.space)
- [CommonCrawl](https://commoncrawl.org/latest-crawl)
- [Similar Sites](https://www.similarsites.com)
- [https://www.similarsites.com](https://www.similarsites.com)
- [Zap Meta](https://www.zapmeta.com)
- [https://www.zapmeta.com](https://www.zapmeta.com)
- [Carrot Search](https://search.carrot2.org/#/search/web)
- [Goo Search](https://www.goo.ne.jp)
- [https://www.goo.ne.jp](https://www.goo.ne.jp)
- [swisscows](https://swisscows.com/en)
- [odp](https://www.odp.org/homepage.php)
- [https://www.odp.org/homepage.php](https://www.odp.org/homepage.php)
- [Yiipy Search](https://www.yippysearchengine.com)
- [https://www.yippysearchengine.com](https://www.yippysearchengine.com)
- [webarchiveviewer](https://cybdetective.com/webarchiveviewer)
- [https://cybdetective.com/webarchiveviewer](https://cybdetective.com/webarchiveviewer)
- [duckduckgo Bangs](https://duckduckgo.com/bangs)
- [mediasova](https://search.mediasova.com/en/index)
- [mojeek](https://www.mojeek.com)
- [https://www.mojeek.com](https://www.mojeek.com)
- [boardreader](https://boardreader.com)
- [https://boardreader.com](https://boardreader.com)
- [Geoint CSE search](https://cse.google.com/cse?cx=015328649639895072395:sbv3zyxzmji#gsc.tab=0&gsc.sort=)
- [lolarchiver](https://osint.lolarchiver.com/#)
- [wbmii](https://webmii.com)
- [https://webmii.com](https://webmii.com)
- [Wiki Leaks](https://wikileaks.org)
- [https://wikileaks.org](https://wikileaks.org)
- [bellingcat wayback-google-analytics](https://github.com/bellingcat/wayback-google-analytics)
- [yamli Arabic search](https://www.yamli.com)
- [https://www.yamli.com](https://www.yamli.com)
- [ASK](https://www.ask.com)
- [https://www.ask.com](https://www.ask.com)
- [Baidu](https://www.baidu.com)
- [https://www.baidu.com](https://www.baidu.com)
- [Infospace](https://www.infospace.com)
- [https://www.infospace.com](https://www.infospace.com)
- [gibiru](https://gibiru.com)
- [https://gibiru.com](https://gibiru.com)
- [kagi](https://kagi.com)
- [https://kagi.com](https://kagi.com)
- [brave](https://search.brave.com)
- [https://search.brave.com](https://search.brave.com)
- [stract](https://stract.com)
- [https://stract.com](https://stract.com)
- [Google Safe Browsing](https://developers.google.com/safe-browsing/reference?hl=id)
- [qwant](https://www.qwant.com)
