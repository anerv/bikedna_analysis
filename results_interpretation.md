# Results & interpretation

## Feature matching & Density differences

- no clear pattern in diff and length of matched features - some tendency to have more matched features where diff is small
- clear tendency that the higher the differences are (negative values) the more unmatched osm features there are
- opposite pattern for reference data - and a little less clear cut
- outliers with high unmatched values around 0 edge dens diff -> clear indication of why FM matters
- outliers with a lot of unmatched ref despite more OSM data (minus dens, high umatched) - also shows diff features
- outliers with high pos diff and high pos unmatched ref - OSM is missing

***

## Differences aggregated on the municipal level

TLDR: There are some trends - but also exceptions. We cannot say that OSM is *always* more extensive or with how much OSM will be more complete/extensive, but:

### Completeness/infrastructure length

- For all aspects compared, there are 96 municipalities where OSM is larger and 2 where GeoDK is larger.
- The differences between the two dataset all between 1.5 - 94% (2.8 - 697 km) (Assens is a clear outlier with much more bike infra in GeoDK)
- Average difference is around 130.6km/58%

### Structure

#### Components

- 91 municipalities have more components in OSM, 7 in GeoDanmark
- 37 have more components per km in OSM, 58 have more comp/km in GeoDanmark
- The range for OSM is smaller than GeoDanmark (0.07 - 1.48 vs. 0.1 - 4.46)
- It is a few outliers that produces the wide value range for GeoDK (Albertslund, Ishøj, and especially Vallensbæk)

#### Topology errors

**GeoDanmark has more errors per km than OSM:**

- The OSM data has 91 overshoots in 37 municipalities and 157 undershoots in 50 municipalities.
- The GeoDanmark data has 99 overshoots in 43 municipalities and 339 undershoots in 65 municipalities.
- The OSM data has 0.04 overshoots and 0.07 undershoots per 10 km.
- The GeoDanmark data has 0.11 overshoots and 0.38 undershoots per 10 km.
- The discrepancy between the number of over and undershoots in the two data sets in many places suggest that it is errors.

**Topology errors are unevenly distributed, and despite GeoDanmark generally having more errors per km, there are also municipalities where OSM has more errors:**

- There are 28 municipalities with more overshoots in OSM than in GeoDanmark.
- There are 31 municipalities with more overshoots GeoDanmark than in OSM.
- There are 26 municipalities with more undershoots in OSM than in GeoDanmark.
- There are 46 municipalities with more undershoots GeoDanmark than in OSM.

## GeoDanmark - municipal analysis

- There are a few municipalities with very different patterns than the majority (Aarhus)
- Many of the correlations between network size, number of components, errors etc. make sense - *but* there patterns are not very consistent, many outliers or municipalities that do not fit the tendency.

- Generally, the longer the network, the fewer components per km --> can both be a question of *network* and of *data* quality
- Componets per km cannot be explained by municipality size/network density - at least only partially. Aarhus has more components per km than expected and Cph. fewer.
- Geographically smaller municipalities tend to have more components per km, but this is mostly explained by their shorter network size, and a few outliers
- Due to how GeoDanmark maps bike infra, it is hard to check for network gaps, but: clear outliers to the trend with more gaps with longer network: Cph and Odense have fewer than expected, Aarhus has more
- Same holds for topology errors for Cph and Aarhus (less vs. more than expected from network size)

## OSM - municipal analysis

- Clear pattern between length and component gaps
- No clear pattern between length or size and components per km
- Clear pattern between length and number of components (but some outliers - Cph fewer than expected)
- Correlation between size and number of components - but some outliers (Aarhus again more components than expected from size - but matches with length!)
- Some weak correlation between length and errrors - but also many without errors regardless of length! Aarhus again has many errors - but corresponds with length

*****

### Correlations

- *Are there any correlations between differences across different dimensions?*

More topology errors in GeoDK data - despite less infra (but small values/differences)

OSM has more infrastructure in almost all muni - except Assens and Langeland (later is small difference)

OSM has more **nodes** in most municipalities - size of differences between >300 and a few pct. (Largest differences for muni where OSM has more network but GeoDK more nodes).

OSM has more **dangling nodes** in all but one muni.

**Network is longest** in OSM in all munis except Assens (large diff) and Langeland.

Same for **network density** - also shows that the diff for Assens is noteworthy given the size of the muni.

More **overshoots** in GeoDK in total, but small diff
More than double the number of **undershoots** in GeoDK than OSM

The discrepancy between **over and undershoots** in many places between the two datasets suggest that it is errors.

Big differences between **over/under** - some muni have way more in GeoDK and vice versa.

Many more **components** on OSM in most munis - except Gentofte, Hvidovre, Vallensbæk

Generally more **components per km** with GeoDK in most munis - but also many with more comps per km in OSM.

For **comp per km**, those with more per comp per km in OSM are only slightly more - while many of those with more in ref have significantly more.

A few munis with way more **comp/components per km** in GeoDK than OSM (Vallensbæk)

### Violin plots

#### Differences

Differences for **nodes**, **dangling nodes**, **node count** are more of less identical - most differences are negative/more OSM but relatively low

Differences for **infra_dens** are mostly close to zero (*relatively*) - but more on the negative/more in OSM side - but a few with much more data in OSM than ref.

**Over** and **under** are mostly symmetrical around zero with most differences being low - but slightly more positive/more in GeoDK for both

Most munis have more **components** in OSM than GeoDK, but few exceptions. Most have a diff around 0 - -100 but some outliers with many more components in OSM.

**Comp per km** is mostly symmetrical around zero, but an outlier tail with munis with many more comps per km in GeoDK than OSM.

#### Both violins

**Node/dangling node** Similar. OSM much bigger distribution than ref.

**Infra_km** again, OSM much bigger value range. More with many km.

**Infra_dens** OSM somewhat bigger value range - OSM fever with low dens and more with medium and high dens.

**Infra_pop** OSM bigger value range - GeoDK has more with low values/low infra per pop, OSM has more with high/much infra per pop.
Interpretation? Can be either way. (looking at data points show that small islands, Læsø og Samsø, which have much more infra in OSM)

**Overshoots** very similar.
**Undershoots** much bigger range in GeodK

**Component count** OSM much bigger range - fewer with low values, more with high values. GeoDK many more with low values.

**Comp per km** OSM much smaller value range, GeoDK much larger. Fairly similar except for some outliers for GeoDK with a lot of components per km (Albertslund, Ishøj, Vallensbæk).

## Correlation between differences

positive correlation between pct differences in dangling nodes and pct differences in components
this is even more clear when looking at standardized values

Correlation between differences pct std for infra km and component count

Otherwise no clear correlation between differences.

## Topology errors - Both

No strong patterns in location of errors

If I wanted to quantify errors in GeoDK - first cluster errors of gaps?
Looking at the number of errors based on density give some results - but does not appear to be significant.

## GeoDanmark

**Correlation between components per km and infra length/area/dens**

Longer network --> fewer components per km - but clear exceptions to this pattern.
Geographically smaller components also have more comp per km - but this is mostly explained by their shorter networks. Also driven by some outliers (Ishøj)? If three most extreme outliers in terms of many components per km, almost no correlation between size and comp per km.

**Correlation between infra length and comp gaps**

Longer network --> more gaps (obviously)
BUT - also outliers.

Notedly - Copenhagen and Odense have few gaps per km of bicycle infra and Aarhus has many.

**Correlation between infra length and topo errors**

Some correlation between length and errors - but also many municipalities, across a wide range of infra lengths, which have none.

Looking only at those munis with gaps, CPH again has few compared to length and Aarhus again has many.

**Correlation between infra length and no components**

Similar pattern as comp gaps - positive correlation but both high and low outliers.
Again Cph low and Aarhus high.

Looking at muni size as a third variable here, it does not seem to be good explanaition - small munis seem to be low both in infra length and number of comps, but there are muni with large areas and roughly same number of comps, but very different lengths of infra.
Also middle munis with medium networks and quite different number of comps.

**Correlation between muni size and no components**

Positive relationship but muddy.
Aarhus agian outlier in terms of number of comps - partly explained by size of network, but not completely?
Viborg and Ringkjøbing-Skjern outliers in terms of low number of comps and size. For RS maybe partly explained by small-ish network - not the case for Viborg (also somewhat outlier in other plots).

**Correlation between infra dens and no components**

Infra density cannot really explain number of components.

Some munis follow expected pattern:
Copenhagen and suburbs to the north stand out with high dens and few components (expected).

Aarhus has low density and many components - expected/what one would predict, *but* many other low density munis have way fewer components.

For some, this might however be because they both are small in terms of area and size.

## OSM

**Correlation between components per km and infra length/area/dens**
Fewer components per km than GeoDK.
No clear pattern between length and comp per km.
Same for comp per km and size.
Some tendency that munis with high density have fewer components per km - but high variability among low density municipalities.

**Correlation between infra length and comp gaps**

Positive correlation
Much more clear/clean than GeoDK
Way fewer gaps
Aarhus has way more gaps than others - but this time more justified by network length
Cph a bit lower than expected from length of network

**Correlation between infra length and topo errors**

Some corr between length and errors. Also here many without one.
Aarhus also here has many errors - but this time aligns with network lenght.
Fredensborg has many errors compared to network length.

**Correlation between infra length and no components**

Clear positive correlation.

Aarhus again has many comp - but also large network.
Copenhagen has fewer components than expected from size - but possibly explained by small area.

Although not perfectly aligned with size, smaller areas tend to have smaller networks and fewer components, opposite for larger.

**Correlation between muni size and no components**

Some positive correlation - but very wide span.
Larger munis -- more comp.
Aarhus outlier - many comp compared to size - but also very big network.

**Correlation between infra dens and no components**

Look somewhat similar to plot for GeoDK.
No low density munis with many components, but for low density munis, both some with many and few components - probably partially explained by infra length.
