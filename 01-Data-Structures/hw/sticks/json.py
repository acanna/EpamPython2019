from collections import Counter, defaultdict
from statistics import mean

from numpy import inf


def parse(s):
    if s.startswith(': '):
        s = s[2:]
    if s.endswith(', '):
        s = s[:-2]
    return s


def to_int(s):
    if s == 'null':
        return -1
    else:
        return int(s)


def max_min_stat_country(country_stats):
    max_mean_stat = -inf
    min_mean_stat = inf
    max_countries = []
    min_countries = []
    for country in country_stats:
        if country_stats[country]:
            mean_stat = round(mean(country_stats[country]))
            if mean_stat == max_mean_stat:
                max_countries.append(country)
            elif mean_stat > max_mean_stat:
                max_countries = [country]
                max_mean_stat = mean_stat
            if mean_stat == min_mean_stat:
                min_countries.append(country)
            elif mean_stat < min_mean_stat:
                min_countries = [country]
                min_mean_stat = mean_stat

    max_countries = '", "'.join(max_countries)
    min_countries = '", "'.join(min_countries)
    return max_countries, min_countries


wines = []
sorts = [
    'Gew\\u00fcrztraminer',
    'Riesling',
    'Merlot',
    'Madera',
    'Tempranillo',
    'Red Blend'
]

stats = dict.fromkeys(sorts)
for key in stats:
    # for each sort list of price, region, country, score values
    stats[key] = [[], Counter(), Counter(), []]

with open('winedata_1.json') as f:
    for wine in f.read()[2:-1].split('{'):
        wine = wine[:wine.index('}')]
        wines.append(wine)

with open('winedata_2.json') as f:
    for wine in f.read()[2:-1].split('{'):
        wine = wine[:wine.index('}')]
        wines.append(wine)

wines = list(dict.fromkeys(wines))

parsed_wines = [None] * len(wines)

highest_score = 0
lowest_score = 100
country_prices = defaultdict(list)
country_points = defaultdict(list)
tasters = Counter()
for i, wine in enumerate(wines):
    wines[i] = (i, wine)
    w = [s for s in
         [parse(t) for t in wine.replace('\\"', '').split('"')]
         if s]
    parsed_wines[i] = w

    # score statistic
    if w[1] != 'null':
        score = int(w[1])
        highest_score = max(highest_score, score)
        lowest_score = min(lowest_score, score)

    # most active commentator by taster_twitter_handle
    if w[9] != 'null':
        tasters[w[9]] += 1

    # country mean price
    if w[23] != 'null' and w[11] != 'null':
        country_prices[w[23]].append(int(w[11]))
    # country scores/points
    if w[23] != 'null' and w[1] != 'null':
        country_points[w[23]].append(int(w[1]))

    if w[15] in sorts:
        # price
        if w[11] != 'null':
            stats[w[15]][0].append(int(w[11]))
        # region
        if w[17] != 'null':
            stats[w[15]][1][w[17]] += 1
        if w[19] != 'null':
            stats[w[15]][1][w[19]] += 1
        # country
        if w[23] != 'null':
            stats[w[15]][2][w[23]] += 1
        # points
        if w[1] != 'null':
            stats[w[15]][3].append(int(w[1]))

wines.sort(key=lambda x: parsed_wines[x[0]][15])
wines.sort(key=lambda x: to_int(parsed_wines[x[0]][11]), reverse=True)

with open('winedata_full.json', 'w') as f:
    f.write('[')
    for i in range(len(wines) - 1):
        f.write(f'{{{wines[i][1]}}}, ')
    f.write(f'{{{wines[len(wines) - 1]}}}]')

with open('stats.json', 'w') as f:
    f.write('{"statistics": {')

    f.write('"wine": {')
    wine_stats = []
    for wine in sorts:
        cur_stats = ['null'] * 6
        if stats[wine][0]:
            cur_stats[0] = round(mean(stats[wine][0]))
            cur_stats[1] = min(stats[wine][0])
            cur_stats[2] = max(stats[wine][0])
        if stats[wine][1]:
            cur_stats[3] = f'"{stats[wine][1].most_common(1)[0][0]}"'
        if stats[wine][2]:
            cur_stats[4] = f'"{stats[wine][2].most_common(1)[0][0]}"'
        if stats[wine][3]:
            cur_stats[5] = round(mean(stats[wine][3]))
        wine_stat = ', '.join([
            f'"average_price": {cur_stats[0]}',
            f'"min_price": {cur_stats[1]}',
            f'"max_price": {cur_stats[2]}',
            f'"most_common_region": {cur_stats[3]}',
            f'"most_common_country": {cur_stats[4]}',
            f'"average_score": {cur_stats[5]}'
        ])
        wine_stats.append(f'"{wine}": {{{wine_stat}}}')

    f.write(', '.join(wine_stats))
    f.write('}, ')  # wine
    most_expensive_wines = []
    max_price = parsed_wines[wines[0][0]][11]
    for i, wine in wines:
        if parsed_wines[i][11] == max_price:
            most_expensive_wines.append(f'{{{wine}}}')
        else:
            break
    most_expensive_wines = ', '.join(most_expensive_wines)
    f.write(f'"most_expensive_wine": [{most_expensive_wines}], ')
    cheapest_wines = []
    min_price = None
    for i, wine in reversed(wines):
        if min_price:
            if parsed_wines[i][11] == min_price:
                cheapest_wines.append(f'{{{wine}}}')
            else:
                break
        elif parsed_wines[i][11] != 'null':
            min_price = parsed_wines[i][11]
            cheapest_wines.append(f'{{{wine}}}')
    cheapest_wines = ', '.join(cheapest_wines)
    f.write(f'"cheapest_wine": [{cheapest_wines}], ')

    f.write(f'"highest_score": {highest_score}, ')
    f.write(f'"lowest_score": {lowest_score}, ')

    max_price_country, min_price_country = max_min_stat_country(country_prices)
    f.write(f'"most_expensive_coutry": ["{max_price_country}"], ')
    f.write(f'"cheapest_coutry": ["{min_price_country}"], ')

    max_score_country, min_score_country = max_min_stat_country(country_points)
    f.write(f'"most_rated_country": ["{max_score_country}"], ')
    f.write(f'"underrated_country": ["{min_score_country}"], ')

    max_taster_count = tasters.most_common(1)[0][1]
    max_tasters = []
    for taster in tasters:
        if tasters[taster] == max_taster_count:
            max_tasters.append(taster)
    max_tasters = '", "'.join(max_tasters)
    f.write(f'"most_active_commentator": ["{max_tasters}"]')

    f.write('}}')  # statistics
