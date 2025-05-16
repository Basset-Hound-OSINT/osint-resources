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
