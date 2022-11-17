# -*- coding: utf-8 - vim: tw=80
"""
Some examples arosing when I implemented the factorization of linear
differential operators.
"""

# Copyright 2021 Alexandre Goyer, Inria Saclay Ile-de-France
#
# Distributed under the terms of the GNU General Public License (GPL) either
# version 2, or (at your option) any later version
#
# http://www.gnu.org/licenses/

from sage.rings.rational_field import QQ
from ore_algebra import DifferentialOperators

Diffops, z, Dz = DifferentialOperators(QQ, 'z')



# from http://koutschan.de/data/fcc1/. (fcc4, fcc5, fcc6 are available in
# ore_algebra's examples).
fcc3 = 2*(-1+z)*z**2*(3+z)**2*Dz**3+3*z*(3+z)*(-6+5*z+5*z**2)*Dz**2+6*(-3+3*z+12*z**2+4*z**3)*Dz+6*z*(2+z)

# Fuchsian operators with linear factors but without rational solution:
# - the first one is the annihilator of sqrt(1+z) and sqrt(1+2z).
# - thanks to Emre Sertoz for the second one (arosing from actual computations).
# - the differential Galois group (= monodromy group) of the third one is composed by homotheties.
sqrt_dop = (4*z**2 + 6*z + 2)*Dz**2 + (4*z + 3)*Dz - 1
sertoz_dop = (-128*z**2 + 8)*(z*Dz)**3 + (-256*z**2-24)*(z*Dz)**2 + (32*z**2 + 10)*(z*Dz)+ 64*z**2
exact_guessing_dop = (2*z*Dz - 1).lclm(2*z*Dz - 3)

# DEtools[DFactor] (of Maple, diffop package) fails with the following operator.
# Thanks to Bruno Salvy for reporting it. We suspect that the large exponent
# (=-972) at point 3 is the cause. !Not Fuchsian! (Update: 2020, Dec)
salvy_dop = (z**2*Dz + 3)*((z - 3)*Dz + 4*z**5)

# The only right factor of the following operator has a degree k (a parameter)
# while the degree of the full operator is 2. For more details, see the article
# "Explicit degree bounds for right factors of linear differential operators" by
# Alin Bostan, Tanguy Rivoal and Bruno Salvy (2020). !Not Fuchsian!
bostan_dop = lambda k: z*Dz**2 + (2-z)*Dz + k

# This example is from van Hoeij's phd thesis (section 3.1). It seems that its
# only right factor has a degree n^2. !Not Fuchsian!
vanhoeij_dop = lambda n: Dz**2 - (1/n)*Dz + n/z

# These reducible operators do not admit factorization with coefficients in QQ
# (to be confirmed) but involve algebraic numbers (of degree n!).
QQbar_dop = lambda n: sum(z**i*Dz**i for i in range(n+1))

# Annihilator of the hypergeometric function 2F1(a,b;c;z).
hypergeo_dop = lambda a,b,c: z*(1 - z)*Dz**2 + (c - (a + b + 1)*z)*Dz - a*b

# This reducible operator admits no factorization in the first Weyl algebra (QQ[z]<Dz>).
# (not so interesting because it admits z as solutions)
irr_weyl_dop = Dz**2 + (-z**2 + 2*z)*Dz + z - 2

# This operator is given as example to illustrate the newton polygon's
# definition in [Formal Solutions ..., van Hoeij, 1997] (Example 3.1).
Tz = z*Dz
newton_dop = z**6*Tz**9 + 2*z**5*Tz**8 + 3*z**4*Tz**7 + 2*z**3*Tz**6 + (z**2 + 2*z**4)*Tz**5 + (5*z**2 - 3*z)*Tz**3 + 3*z*Tz**2 + (2 + 2*z)*Tz + 7*z

# The following operator have 0 as only integer exponent (with multiplicity 1)
# but its adjoint has no power series solution (the only integer exponent is -1).
adjoint_exponent_dop = 2*z**3*Dz**2 + (5*z**2 + 6*z)*Dz + z


# The following irreducible fuchsian operators were studied by [Zagier, 2016]
dop_a = 1800*z*(7*z - 62)*(z**2 + 50*z + 20)*Dz**2 + (30240*z**3 + 124560*z**2 - 10245600*z - 446400)*Dz + 6048*z**2 - 139453*z - 249550
dop_b = 90000*z**3*(2911*z+310)*(z**2+50*z+20)*Dz**4+18000*z**2*(154283*z**3+5185005*z**2+1675710*z+142600)*Dz**3+50*z*(147290778*z**3+2740219655*z**2+566777510*z+37497600)*Dz**2+(4599496440*z**3+28145233025*z**2+6744696050*z+53568000)*Dz+250881624*z**2-19383210*z+22459500

# The following irreducible fuchsian operators annihilate the power series of
# general term:
# (6n)!n!/((3n)!(2n)!(2n)!) for the first one,
# (30n)!n!/((16n)!(10n)!(5n)!) for the second one.
# These operators are algebraic, see [Villegas, 2007]
simple_chebychev_dop = (216*z**2 - 2*z)*Dz**2 + (432*z - 1)*Dz + 30
chebychev_dop = (11337408000000000*z**8 - 11250*z**7)*Dz**8 + (362797056000000000*z**7 - 275625*z**6)*Dz**7 + (4043927462400000000*z**6 - 2223250*z**5)*Dz**6 + (19459527091200000000*z**5 - 7118750*z**4)*Dz**5 + (40810981455014400000*z**4 - 8665432*z**3)*Dz**4 + (33378063480115200000*z**3 - 3181944*z**2)*Dz**3 + (7972406431637760000*z**2 - 181392*z)*Dz**2 + (251637206929920000*z - 48)*Dz + 3726543300480


# The following operator is a product Q*P*P with ord(P)=ord(Q)=2, which is found irreducible with DFactor.
# The second one is the irreducible Q * P * P + R where R is small so that the exponents structure is inchanged.
QPP = (192*z**18 - 3456*z**17 + 28224*z**16 - 138240*z**15 + 452160*z**14 - 1040256*z**13 + 1725888*z**12 - 2080512*z**11 + 1808640*z**10 - 1105920*z**9 + 451584*z**8 - 110592*z**7 + 12288*z**6)*Dz**6 + (-21312*z**17 + 359040*z**16 - 2741952*z**15 + 12552960*z**14 - 38377920*z**13 + 82574976*z**12 - 128274240*z**11 + 145038336*z**10 - 118544640*z**9 + 68352000*z**8 - 26409984*z**7 + 6144000*z**6 - 651264*z**5)*Dz**5 + (942336*z**16 - 14691248*z**15 + 103973136*z**14 - 442340672*z**13 + 1262108832*z**12 - 2549027888*z**11 + 3743267280*z**10 - 4033162720*z**9 + 3167315328*z**8 - 1768516096*z**7 + 666110208*z**6 - 151768576*z**5 + 15790080*z**4)*Dz**4 + (-20111616*z**15 + 286581760*z**14 - 1866288160*z**13 + 7377950144*z**12 - 19807197440*z**11 + 38177885376*z**10 - 54280917984*z**9 + 57362028416*z**8 - 44636499968*z**7 + 24866254336*z**6 - 9378210304*z**5 + 2141675520*z**4 - 223150080*z**3)*Dz**3 + (185131008*z**14 - 2417460448*z**13 + 14786677716*z**12 - 56364214480*z**11 + 149347936824*z**10 - 289050926992*z**9 + 417012130548*z**8 - 449508602336*z**7 + 357527514720*z**6 - 203635305344*z**5 + 78432331584*z**4 - 18243937280*z**3 + 1928724480*z**2)*Dz**2 + (-44568576*z**13 + 2435213664*z**12 - 28367498140*z**11 + 156077341768*z**10 - 511117695296*z**9 + 1113550268696*z**8 - 1716854054820*z**7 + 1931267337888*z**6 - 1590546221216*z**5 + 936281683712*z**4 - 372006341440*z**3 + 88941614080*z**2 - 9617080320*z)*Dz - 7240679424*z**12 + 49326035616*z**11 - 109231891400*z**10 - 17327453053*z**9 + 638416965641*z**8 - 1805014881821*z**7 + 3063663869775*z**6 - 3640200220578*z**5 + 3119697806036*z**4 - 1903574724872*z**3 + 783554180800*z**2 - 193562337280*z + 21507932160
QPPR = (192*z**18 - 3456*z**17 + 28224*z**16 - 138240*z**15 + 452160*z**14 - 1040256*z**13 + 1725888*z**12 - 2080512*z**11 + 1808640*z**10 - 1105920*z**9 + 451584*z**8 - 110592*z**7 + 12288*z**6)*Dz**6 + (-21312*z**17 + 359040*z**16 - 2741952*z**15 + 12552960*z**14 - 38377920*z**13 + 82574976*z**12 - 128274240*z**11 + 145038336*z**10 - 118544640*z**9 + 68352000*z**8 - 26409984*z**7 + 6144000*z**6 - 651264*z**5)*Dz**5 + (942336*z**16 - 14691248*z**15 + 103973136*z**14 - 442340672*z**13 + 1262108832*z**12 - 2549027888*z**11 + 3743267280*z**10 - 4033162720*z**9 + 3167315328*z**8 - 1768516096*z**7 + 666110208*z**6 - 151768576*z**5 + 15790080*z**4)*Dz**4 + (-20111616*z**15 + 286581760*z**14 - 1866288160*z**13 + 7377950144*z**12 - 19807197440*z**11 + 38177885376*z**10 - 54280917984*z**9 + 57362028416*z**8 - 44636499968*z**7 + 24866254336*z**6 - 9378210304*z**5 + 2141675520*z**4 - 223150080*z**3)*Dz**3 + (185131008*z**14 - 2417460448*z**13 + 14786677716*z**12 - 56364214480*z**11 + 149347936824*z**10 - 289050926992*z**9 + 417012130548*z**8 - 449508602336*z**7 + 357527514720*z**6 - 203635305344*z**5 + 78432331584*z**4 - 18243937280*z**3 + 1928724480*z**2)*Dz**2 + (-44568576*z**13 + 2435213664*z**12 - 28367498140*z**11 + 156077341768*z**10 - 511117695296*z**9 + 1113550268696*z**8 - 1716854054820*z**7 + 1931267337888*z**6 - 1590546221216*z**5 + 936281683712*z**4 - 372006341440*z**3 + 88941614080*z**2 - 9617080320*z)*Dz - 7240679424*z**12 + 49326035616*z**11 - 109231891400*z**10 - 17327453053*z**9 + 638416965641*z**8 - 1805014881821*z**7 + 3063663869775*z**6 - 3640200220578*z**5 + 3119697806036*z**4 - 1903574724680*z**3 + 783554180224*z**2 - 193562336896*z + 21507932160


### Chyzak's examples !Not Fuchsian! ###
pLQR8 = (1296*z**9 - 32085*z**8 + 248800*z**7 - 672000*z**6)*Dz**8 + (-3888*z**8 + 64170*z**7 - 248800*z**6)*Dz**7 + (17496*z**7 - 222120*z**6 + 644000*z**5)*Dz**6 + (-73116*z**6 + 730200*z**5 - 1736000*z**4)*Dz**5 + (2592*z**6 + 195840*z**5 - 1663600*z**4 + 3528000*z**3)*Dz**4 + (-19440*z**5 - 294660*z**4 + 2490800*z**3 - 5376000*z**2)*Dz**3 + (74520*z**4 - 17820*z**3 - 1849600*z**2 + 5376000*z)*Dz**2 + (-165780*z**3 + 1133040*z**2 - 2374400*z)*Dz + 1296*z**3 + 116685*z**2 - 896240*z + 2016000
# pLQR8_bad = pLQR8(z**j*Dz**i --> Dz**i*z**j). van Hoeij's code finds irreducibility very quickly.
pLQR8_bad = (1296*z**9 - 32085*z**8 + 248800*z**7 - 672000*z**6)*Dz**8 + (89424*z**8 - 1989270*z**7 + 13684000*z**6 - 32256000*z**5)*Dz**7 + (2412504*z**7 - 47387070*z**6 + 282783200*z**5 - 564480000*z**4)*Dz**6 + (32667732*z**6 - 554379540*z**5 + 2786728000*z**4 - 4515840000*z**3)*Dz**5 + (2592*z**6 + 237639240*z**5 - 3384909100*z**4 + 13746488000*z**3 - 16934400000*z**2)*Dz**4 + (42768*z**5 + 923905260*z**4 - 10598804000*z**3 + 32577216000*z**2 - 27095040000*z)*Dz**3 + (249480*z**4 + 1798681140*z**3 - 15576004000*z**2 + 32191488000*z - 13547520000)*Dz**2 + (508140*z**3 + 1502846040*z**2 - 8731502400*z + 9096192000)*Dz + 1296*z**3 + 280305*z**2 + 366756520*z - 1071592000
# monodromy at 1e-500 in 3min but too large loss of precision (in charpoly)
pLQR12 = (4096*z**15 - 8057595*z**14 + 4363520256*z**13 - 606943051776*z**12 - 263183196487680*z**11 + 100120377950208000*z**10)*Dz**12 + (716800*z**14 - 1321445580*z**13 + 667618599168*z**12 - 86185913352192*z**11 - 34476998739886080*z**10 + 12014445354024960000*z**9)*Dz**11 + (53771264*z**13 - 92383148256*z**12 + 43264674941184*z**11 - 5139383740268544*z**10 - 1885383259041300480*z**9 + 594715045024235520000*z**8)*Dz**10 + (2274022144*z**12 - 3618236338680*z**11 + 1559181490122240*z**10 - 168798968881053696*z**9 - 56320334797366886400*z**8 + 15859067867312947200000*z**7)*Dz**9 + (60012393152*z**11 - 87790839893664*z**10 + 34510550040138240*z**9 - 3367273163015356416*z**8 - 1010635834250546380800*z**7 + 249780318910178918400000*z**6)*Dz**8 + (1033753455728*z**10 - 1378540881648768*z**9 + 489246143695921152*z**8 - 42452845749189476352*z**7 - 11295000342150355353600*z**6 + 2397891061537717616640000*z**5)*Dz**7 + (8192*z**10 + 11817978434854*z**9 - 14219473030174656*z**8 + 4498666973572939776*z**7 - 341451819511938809856*z**6 - 78958354168459925913600*z**5 + 13987697858970019430400000*z**4)*Dz**6 + (348160*z**9 + 89429350059090*z**8 - 95870207845702656*z**7 + 26609265851213979648*z**6 - 1729382001408369229824*z**5 - 338152972193221312512000*z**4 + 47957821230754352332800000*z**3)*Dz**5 + (5856256*z**8 + 439042399810752*z**7 - 412729363214499456*z**6 + 98427354914525552640*z**5 - 5322236663399228375040*z**4 - 845224841008159653888000*z**3 + 89920914807664410624000000*z**2)*Dz**4 + (47985408*z**7 + 1342311357395808*z**6 - 1083810651335691264*z**5 + 215867787180707414016*z**4 - 9318275106273660764160*z**3 - 1127233709339754627072000*z**2 + 79929702051257253888000000*z)*Dz**3 + (198625984*z**6 + 2376272747116176*z**5 - 1601962666488175104*z**4 + 255781061899193548800*z**3 - 8259771543067023114240*z**2 - 676730454788951506944000*z + 23978910615377176166400000)*Dz**2 + (381497456*z**5 + 2126092481531712*z**4 - 1148741029122895872*z**3 + 137823913299263422464*z**2 - 2958274941652429701120*z - 123157676435039059968000)*Dz + 4096*z**5 + 248398369*z**4 + 697951026217824*z**3 - 283323135285181440*z**2 + 22701827323680325632*z - 242892071580928573440
