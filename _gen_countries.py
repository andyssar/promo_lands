import os

NUM_WORDS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six'}

COUNTRIES = [
    dict(name='Armenia', slug='armenia', flag='am', demonym='Armenian',
         ip='6,500+', ip_short='6.5K+',
         cities=['Yerevan', 'Gyumri', 'Vanadzor', 'Vagharshapat', 'Abovyan', 'Kapan', 'Hrazdan', 'Armavir']),
    dict(name='Azerbaijan', slug='azerbaijan', flag='az', demonym='Azerbaijani',
         ip='9,000+', ip_short='9K+',
         cities=['Baku', 'Ganja', 'Sumqayit', 'Mingachevir', 'Nakhchivan', 'Shirvan', 'Lankaran', 'Sheki']),
    dict(name='Bahrain', slug='bahrain', flag='bh', demonym='Bahraini',
         ip='4,200+', ip_short='4.2K+',
         cities=['Manama', 'Riffa', 'Muharraq', 'Hamad Town', "A'ali", 'Isa Town', 'Sitra', 'Budaiya']),
    dict(name='Bangladesh', slug='bangladesh', flag='bd', demonym='Bangladeshi',
         ip='45,000+', ip_short='45K+',
         cities=['Dhaka', 'Chittagong', 'Khulna', 'Rajshahi', 'Sylhet', 'Barisal', 'Comilla', 'Rangpur', 'Mymensingh', 'Narayanganj']),
    dict(name='Bhutan', slug='bhutan', flag='bt', demonym='Bhutanese',
         ip='1,800+', ip_short='1.8K+',
         cities=['Thimphu', 'Phuntsholing', 'Punakha', 'Paro', 'Gelephu', 'Samdrup Jongkhar', 'Wangdue Phodrang']),
    dict(name='Brunei Darussalam', slug='brunei-darussalam', flag='bn', demonym='Bruneian',
         ip='2,200+', ip_short='2.2K+',
         cities=['Bandar Seri Begawan', 'Kuala Belait', 'Seria', 'Tutong', 'Bangar']),
    dict(name='Cambodia', slug='cambodia', flag='kh', demonym='Cambodian',
         ip='15,000+', ip_short='15K+',
         cities=['Phnom Penh', 'Siem Reap', 'Battambang', 'Sihanoukville', 'Kampong Cham', 'Poipet', 'Kampot']),
    dict(name='China', slug='china', flag='cn', demonym='Chinese',
         ip='850,000+', ip_short='850K+',
         cities=['Beijing', 'Shanghai', 'Guangzhou', 'Shenzhen', 'Chengdu', 'Hangzhou', 'Wuhan', "Xi'an", 'Nanjing', 'Chongqing']),
    dict(name='Cyprus', slug='cyprus', flag='cy', demonym='Cypriot',
         ip='5,000+', ip_short='5K+',
         cities=['Nicosia', 'Limassol', 'Larnaca', 'Paphos', 'Famagusta', 'Kyrenia']),
    dict(name='East Timor', slug='east-timor', flag='tl', demonym='Timorese',
         ip='1,200+', ip_short='1.2K+',
         cities=['Dili', 'Baucau', 'Maliana', 'Suai', 'Same', 'Pante Macassar']),
    dict(name='Georgia', slug='georgia', flag='ge', demonym='Georgian',
         ip='8,000+', ip_short='8K+',
         cities=['Tbilisi', 'Batumi', 'Kutaisi', 'Rustavi', 'Zugdidi', 'Gori', 'Poti']),
]

AFGHANISTAN = dict(name='Afghanistan', slug='afghanistan', flag='af', demonym='Afghan',
                    ip='12,000+', ip_short='12K+',
                    cities=['Kabul', 'Kandahar', 'Herat', 'Mazar-i-Sharif', 'Kunduz',
                            'Jalalabad', 'Lashkar Gah', 'Taloqan', 'Pul-e-Khumri', 'Khost'])

ALL_COUNTRIES = [AFGHANISTAN] + COUNTRIES

BASE = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(BASE, 'afghanistan', 'index.html')


def load_template():
    with open(TEMPLATE_PATH, encoding='utf-8') as f:
        return f.read()


def other_locations_for(slug):
    order = [c['slug'] for c in ALL_COUNTRIES]
    idx = order.index(slug)
    picks = []
    i = idx
    while len(picks) < 5:
        i = (i + 1) % len(order)
        if order[i] != slug:
            picks.append(order[i])
    return [c for c in ALL_COUNTRIES if c['slug'] in picks and c['slug'] != slug][:0] or \
           [next(c for c in ALL_COUNTRIES if c['slug'] == s) for s in picks]


def build_page(country):
    c = load_template()

    name = country['name']
    slug = country['slug']
    flag = country['flag']
    demonym = country['demonym']
    ip = country['ip']
    ip_short = country['ip_short']
    cities = country['cities']
    n_cities = len(cities)

    c1 = cities[0]
    c2 = cities[1] if n_cities > 1 else cities[0]
    c3 = cities[2] if n_cities > 2 else c1
    c4 = cities[3] if n_cities > 3 else c1

    # ---- 1. Title / meta / OG (most specific strings first) ----
    c = c.replace(
        'Afghanistan Residential Proxies, 12K+ Afghan IPs | 2extract',
        f'{name} Residential Proxies, {ip_short} {demonym} IPs | 2extract'
    )
    c = c.replace(
        'Residential proxies in Afghanistan with city-level targeting across Kabul, Kandahar, Herat and more. Ethically sourced IPs, PAYG pricing, no traffic-limited plans.',
        f'Residential proxies in {name} with city-level targeting across {c1}, {c2}, {c3} and more. Ethically sourced IPs, PAYG pricing, no traffic-limited plans.'
    )
    c = c.replace(
        'afghanistan proxy, afghanistan residential proxy, kabul proxy, afghan ip addresses, afghanistan web scraping',
        f'{slug.replace("-", " ")} proxy, {slug.replace("-", " ")} residential proxy, {c1.lower()} proxy, {demonym.lower()} ip addresses, {slug.replace("-", " ")} web scraping'
    )
    c = c.replace(
        'Afghanistan Residential Proxies | 2extract',
        f'{name} Residential Proxies | 2extract'
    )
    c = c.replace(
        'Residential proxies in Afghanistan with city-level targeting across Kabul, Kandahar, Herat and more. Ethically sourced IPs, PAYG pricing.',
        f'Residential proxies in {name} with city-level targeting across {c1}, {c2}, {c3} and more. Ethically sourced IPs, PAYG pricing.'
    )
    c = c.replace('https://2extract.com/og/afghanistan.png', f'https://2extract.com/og/{slug}.png')
    c = c.replace('https://2extract.com/afghanistan"', f'https://2extract.com/{slug}"')

    # ---- 2. data-routing-cities exact list ----
    c = c.replace(
        'data-routing-cities="Kabul,Kandahar,Herat,Mazar-i-Sharif,Kunduz,Jalalabad,Lashkar Gah,Taloqan,Pul-e-Khumri,Khost"',
        f'data-routing-cities="{",".join(cities)}"'
    )

    # ---- 3. FAQ target-cities sentence ----
    if n_cities > 1:
        city_list_str = ', '.join(cities[:-1]) + f' or {cities[-1]}'
    else:
        city_list_str = cities[0]
    c = c.replace(
        'Yes &mdash; set a city in your proxy username to target Kabul, Kandahar, Herat, Mazar-i-Sharif, Kunduz, Jalalabad, Lashkar Gah, Taloqan, Pul-e-Khumri or Khost directly.',
        f'Yes &mdash; set a city in your proxy username to target {city_list_str} directly.'
    )

    # ---- 4. "Why" city-level precision sentence ----
    extra = n_cities - 4
    if extra >= 1:
        more_word = NUM_WORDS.get(extra, str(extra))
        center_word = 'major center' if extra == 1 else 'major centers'
        precision_sentence = f'Target {c1}, {c2}, {c3}, {c4} and {more_word} more {center_word} individually'
    else:
        precision_sentence = f'Target {c1}, {c2} and {c3} individually'
    c = c.replace(
        'Target Kabul, Kandahar, Herat, Mazar-i-Sharif and six more major centers individually',
        precision_sentence
    )

    # ---- 5. Hero description 4-city mention ----
    c = c.replace(
        'City-level targeting across Kabul, Kandahar, Herat and Mazar-i-Sharif for market research',
        f'City-level targeting across {c1}, {c2}, {c3} and {c4} for market research'
    )

    # ---- 6. City coverage grid ----
    old_grid = '\n'.join(
        f'<div class="rounded-xl border border-border bg-card px-4 py-4 text-center font-medium text-foreground">{city}</div>'
        for city in AFGHANISTAN['cities']
    )
    new_grid = '\n'.join(
        f'<div class="rounded-xl border border-border bg-card px-4 py-4 text-center font-medium text-foreground">{city}</div>'
        for city in cities
    )
    assert old_grid in c, f'[{slug}] city grid block not found'
    c = c.replace(old_grid, new_grid)

    # ---- 7. "Kabul or Herat" example in Genuine local traffic card ----
    c = c.replace('browsing from Kabul or Herat', f'browsing from {c1} or {c3}')

    # ---- 8. Stat boxes: IPs count + cities covered count ----
    c = c.replace(
        '<div class="text-lg font-bold text-foreground">12K+</div><div class="text-xs text-muted-foreground">Afghan IPs</div>',
        f'<div class="text-lg font-bold text-foreground">{ip_short}</div><div class="text-xs text-muted-foreground">{demonym} IPs</div>'
    )
    c = c.replace(
        '<div class="text-lg font-bold text-foreground">10</div><div class="text-xs text-muted-foreground">Cities covered</div>',
        f'<div class="text-lg font-bold text-foreground">{n_cities}</div><div class="text-xs text-muted-foreground">Cities covered</div>'
    )

    # ---- 9. "12,000+" written out (FAQ answer + final CTA) ----
    c = c.replace('12,000+ residential IPs across Afghanistan', f'{ip} residential IPs across {name}')
    c = c.replace('Instant access to 12,000+ Afghan residential IPs', f'Instant access to {ip} {demonym} residential IPs')

    # ---- 10. Routing card uppercase country label ----
    c = c.replace(
        '<span class="text-xs font-semibold text-muted-foreground uppercase tracking-wide">Afghanistan</span>',
        f'<span class="text-xs font-semibold text-muted-foreground uppercase tracking-wide">{name.upper()}</span>'
    )

    # ---- 11. Default routing city text (before JS kicks in) ----
    c = c.replace('id="routing-city">Kabul<', f'id="routing-city">{c1}<')

    # ---- 12. Flag alt + badge text ----
    c = c.replace('alt="Afghanistan flag"', f'alt="{name} flag"')
    c = c.replace('>Afghanistan proxies<', f'>{name} proxies<')

    # ---- 13. Generic "Afghanistan" catch-all (headings, eyebrows, etc.) ----
    c = c.replace('Afghanistan', name)

    # ---- 14. Generic "Afghan" catch-all (demonym adjective usages) ----
    c = c.replace('Afghan', demonym)

    # ---- 15. Flag asset path ----
    c = c.replace('assets/flags/af.svg', f'assets/flags/{flag}.svg')

    # ---- 16. Other-locations teaser: replace the 5 sample country links ----
    others = other_locations_for(slug)
    old_teaser = '\n'.join([
        '<a href="../index.html" class="rounded-xl border border-border bg-card px-4 py-4 flex items-center gap-2 loc-hover-border transition-colors"><img src="../assets/flags/in.svg" class="size-5 rounded-full" alt="">India</a>',
        '<a href="../index.html" class="rounded-xl border border-border bg-card px-4 py-4 flex items-center gap-2 loc-hover-border transition-colors"><img src="../assets/flags/cn.svg" class="size-5 rounded-full" alt="">China</a>',
        '<a href="../index.html" class="rounded-xl border border-border bg-card px-4 py-4 flex items-center gap-2 loc-hover-border transition-colors"><img src="../assets/flags/tr.svg" class="size-5 rounded-full" alt="">Turkey</a>',
        '<a href="../index.html" class="rounded-xl border border-border bg-card px-4 py-4 flex items-center gap-2 loc-hover-border transition-colors"><img src="../assets/flags/id.svg" class="size-5 rounded-full" alt="">Indonesia</a>',
        '<a href="../index.html" class="rounded-xl border border-border bg-card px-4 py-4 flex items-center gap-2 loc-hover-border transition-colors"><img src="../assets/flags/pk.svg" class="size-5 rounded-full" alt="">Pakistan</a>',
    ])
    new_teaser = '\n'.join(
        f'<a href="../{o["slug"]}/index.html" class="rounded-xl border border-border bg-card px-4 py-4 flex items-center gap-2 loc-hover-border transition-colors"><img src="../assets/flags/{o["flag"]}.svg" class="size-5 rounded-full" alt="">{o["name"]}</a>'
        for o in others
    )
    assert old_teaser in c, f'[{slug}] other-locations teaser block not found'
    c = c.replace(old_teaser, new_teaser)

    return c


def main():
    for country in COUNTRIES:
        page = build_page(country)
        out_dir = os.path.join(BASE, country['slug'])
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, 'index.html')
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(page)
        remaining_afghan = page.count('Afghan')
        remaining_kabul = page.count('Kabul')
        print(f"{country['slug']:20s} written ({len(page)} chars) residual-Afghan={remaining_afghan} residual-Kabul={remaining_kabul}")


if __name__ == '__main__':
    main()
