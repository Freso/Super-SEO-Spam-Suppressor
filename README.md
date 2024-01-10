# Super SEO Spam Suppressor

Super SEO Spam Suppressor (SSSS[^SSSS]) is a domains blocklist of sites abusing SEO tactics to spam web searches with advertisement, empty content (monetized with ads), malware (looking like ads) and generative AI garbage. It is best used with uBlacklist.

[^SSSS]: It's a Gridman reference. I'm spelling it out because it's also the name of a skin disease: don't go looking for SSSS on image search.

> Our website is now optimized to supply content to Google, not build an audience of its own.  
> [Mia Sato, "The Perfect Webpage", *The Verge*.](https://www.theverge.com/c/23998379/google-search-seo-algorithm-webpage-optimization)

As of now, present day, time of writing year 2023, Google is now a barely useable, terminally enshittified mess, merely a husk of the wonderful discovery tool it was yesterday.
Do you want to learn about *thing*?
[How about **buying** *thing* and **consuming** *thing* instead?](https://www.wired.com/story/google-antitrust-lawsuit-search-results/)
Its drive to commercialize our every online interaction also has consequences on other, much more user friendly search engines such as DuckDuckGo, whose indexers crawl through [shit optimized for Google's terrible algorithm](https://www.theverge.com/c/23998379/google-search-seo-algorithm-webpage-optimization).
Moreover, generative models are now branded as "AIs" and they suck.
This list is, as any good adblocking tool is, an attempt to escape this neverending capitalist coercition and attention theft.
All of the tech giants play this game so consider also using a social media blocklist.

This blocklist is left in the [public domain (Do What The Fuck You Want To Public License)](https://github.com/NotaInutilis/Super-SEO-Spam-Suppressor/blob/main/LICENSE).

## Browser extensions

### uBlacklist syntax

[Blocklist in uBlacklist format](https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/ublacklist.txt) to use with [uBlacklist](https://github.com/iorate/ublacklist). It removes blocked sites from search engine results.

[Click here to subscribe.](https://iorate.github.io/ublacklist/subscribe?name=Super%20SEO%20Spam%20Suppressor&url=https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/ublacklist.txt)  (This automatic subscription link is only compatible with Chrome, you have to add it by yourself on other browsers!)

### AdBlock Plus syntax

[Blocklist in AdBlock format](https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/adblock.txt) to use with an adblocker ([uBlock Origin](https://ublockorigin.com), [Adguard](https://adguard.com)…) or Adguard Home. It uses a [strict blocking rule](https://github.com/gorhill/uBlock/wiki/Strict-blocking) to block access to those sites on your browser.

[Click here to subscribe.](https://subscribe.adblockplus.org/?location=https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/adblock.txt&title=Super%20SEO%20Spam%20Suppressor)

## DNS blockers

### Hosts format

[Blocklist in Hosts format](https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/hosts.txt) to use in a [hosts](https://en.wikipedia.org/wiki/Hosts_(file)) file or [Pi-hole](https://pi-hole.net/).

[IPV6 version](https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/hosts.txt.ipv6).

**Known issue:** [Firefox's DNS over HTTPS option bypasses the computer's hosts file ruleset.](https://bugzilla.mozilla.org/show_bug.cgi?id=1453207)

### Dnsmasq format

[Blocklist in Dnsmasq format](https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/dnsmasq.txt) to use with the [Dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html) DNS server software.

## Fediverse formats

### Mastodon

[Blocklist in Mastodon format](https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/mastodon.csv) to use with [Mastodon](https://joinmastodon.org/) and other federated services. It will defederate from blocked instances.

### Fediblockhole

[Blocklist in FediBlockHole format](https://raw.githubusercontent.com/NotaInutilis/Super-SEO-Spam-Suppressor/main/fediblockhole.csv) to use with the [FediBlockHole](https://github.com/eigenmagic/fediblockhole) tool for Mastodon. It will defederate from blocked instances.

## How to contribute

Clone this repository and add one domain per line in `.txt` files stored in the `sources` folder. Blocked sites are organized using subfolders and `.txt` files within the `sources` folder. Use comments (`#`) and markdown files (`.md`) to add more information and references.

> For the `https://www.example.com` website, add `example.com` on a new line of the `sources/default.txt` file.

You can paste the full URL: the update script will clean it and make it a domain. As the hosts format does not automatically block subdomains (e.g. `subdomain.example.com`), they have to be explicitely added to the list to maintain compatibility.

It is possible to add TLDs (e.g. `com`, without the dot) to the list, they will be blocked by Dnsmasq, adblockers and uBlacklist. Domains related to Fediverse instances (Mastodon, Peertube, etc.) should be put in `.txt` files with `fediverse` in their names (e.g. `Bad Fediverse is bad.txt`) so that they are included in the Fediverse blocklists.

Then, when you push your changes to the `sources` folder, GitHub actions automatically generate new versions of the blocklists. Should you want to generate them yourself, you can run the `scripts/update.sh` script (prerequisites : bash, python).

Finally, make a pull request: it will be reviewed and approve it within a few days.

### Importing an external list

External lists can be imported by adding them to the `import/importlist.txt` as a new line in the following format: `list name.txt|url`. They are automatically downloaded twice a day, cleaned (some formats only), copied to the `sources/_imported/`folder and thus added to the list generation database. The domain list in the `import/allowlist.txt` file serves as an exception ruleset for imported lists.

### How to contribute (easy mode)

If you have no idea how Git works, you can still contribute! Just [open an issue](https://github.com/NotaInutilis/Super-SEO-Spam-Suppressor/issues) with the URLs you would like to add to the list (or remove, false positives happen!), grouping them by language and categories if possible. We'll check and add them shortly.

### Report malicious websites

The next best thing to do after adding a malicious website (malware, phishing, scam) to this list is to to report it so it actually doesn't show up in searches, or even gets taken offline by its host or registrar!
Here's a video guide on how to do it: [How Anyone Can DESTROY A Scam Website in Minutes 😤 (Scammers Will HATE This)](https://www.youtube.com/watch?v=0fIUiv9-UFk).

Sites to report malicious URLs:
- Search engines:
    - [Google SafeBrowsing](https://safebrowsing.google.com/safebrowsing/report_phish/)
    - [Microsoft](https://www.microsoft.com/wdsi/support/report-unsafe-site)
- Cybersecurity providers:
    - [Fortiguard](https://www.fortiguard.com/webfilter)
    - [BrightCloud](https://www.brightcloud.com/tools/url-ip-lookup.php)
    - [CRDF](https://threatcenter.crdf.fr/submit_url.html)
    - [Netcraft](https://report.netcraft.com/report)
    - [Palo Alto Networks](https://urlfiltering.paloaltonetworks.com/)
    - [ESET](https://phishing.eset.com/report)
    - [Trend Micro](https://global.sitesafety.trendmicro.com/index.php)
    - [Forcepoint](https://csi.forcepoint.com/)
    - [Spam404](https://www.spam404.com/report.html)
    - [Cisco Talos](https://talosintelligence.com/reputation_center)
    - [URLhaus](https://urlhaus.abuse.ch/browse/)
- Antivirus publishers:
    - [BitDefender](https://www.bitdefender.com/consumer/support/answer/29358/)
    - [McAfee](https://sitelookup.mcafee.com/)
    - [Symantec](https://sitereview.symantec.com/#/)
    - [Kaspersky](https://opentip.kaspersky.com/)
    - [Avira](https://www.avira.com/en/analysis/submit-url)
    - [Avast](https://www.avast.com/report-malicious-file.php)
- Phishing databases:
    - [Phishing Initiative](https://phishing-initiative.eu/contrib/)
    - [PhishTank](https://www.phishtank.com/add_web_phish.php)
    - [OpenPhish](https://openphish.com/) via [e-mail](mailto:report@openphish.com)

## Aggregated lists

This blocklist borrows from the following projects:
- the blocklist generation code and readme that I co-wrote for rimu's [No-QAnon](https://github.com/rimu/no-qanon) ([anti-fascist licence](https://github.com/rimu/no-qanon/blob/master/LICENSE.txt)).
- the [full blocklist](https://github.com/quenhus/uBlock-Origin-dev-filter/blob/main/dist/other_format/domains/all.txt) from quenhus' [uBlock-Origin-dev-filter](https://github.com/quenhus/uBlock-Origin-dev-filter) ([The Unlicense, public domain](https://github.com/quenhus/uBlock-Origin-dev-filter/blob/main/LICENSE)).
- the [full blocklist](https://github.com/no-cmyk/Search-Engine-Spam-Blocklist/blob/master/blocklist.txt) from no-cmyk's [Search Engine Spam Blocklist](https://github.com/no-cmyk/Search-Engine-Spam-Blocklist) (no licence).
- the [full blocklist](https://github.com/franga2000/aliexpress-fake-sites/blob/main/domains.txt) from franga2000's [AliExpress fake site blocker](https://github.com/franga2000/aliexpress-fake-sites) (no licence).
- the [full blocklist](https://github.com/levitation-opensource/aliexpress-fake-sites/blob/main/domains.txt) from levitation's fork of the [AliExpress fake site blocker](https://github.com/levitation-opensource/aliexpress-fake-sites) (no licence).
- the [full blocklist](https://dl.red.flag.domains/red.flag.domains.txt) from [Red Flag Domains](https://red.flag.domains/) ([Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)).
- the [full blocklist](https://github.com/insomnimus/seo-garbage/blob/main/list.txt) from insomnimus' [seo-garbage](https://github.com/insomnimus/seo-garbage) ([Apache License](https://github.com/insomnimus/seo-garbage/blob/main/LICENSE)).
- the [antipup domains](https://github.com/iam-py-test/my_filters_001/blob/main/Alternative%20list%20formats/antipup_domains.txt), [antitypo domains](https://github.com/iam-py-test/my_filters_001/blob/main/Alternative%20list%20formats/antitypo_domains.txt) and [clickbait domains](https://github.com/iam-py-test/my_filters_001/blob/main/Alternative%20list%20formats/clickbait_domains.txt) blocklist from iam-py-test's [my_filters_001](https://github.com/iam-py-test/my_filters_001) ([CC0 1.0 Universal](https://github.com/iam-py-test/my_filters_001/blob/main/LICENSE)).

## Other useful lists

[Jmdugan Blocklists](https://github.com/jmdugan/blocklists/tree/master/corporations): consider blocking social media and big tech corporations.
