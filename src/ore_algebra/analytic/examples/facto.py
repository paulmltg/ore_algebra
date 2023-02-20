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
# only right factor has a degree n**2. !Not Fuchsian!
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

# The following operator is presented by van Straten (Calabi-Yau operators, 2017).
van_straten_dop = Tz**4 - 5*z*(5*Tz + 1)*(5*Tz + 2)*(5*Tz + 3)*(5*Tz + 4)

# The following operator have 0 as only integer exponent (with multiplicity 1)
# but its adjoint has no power series solution (the only integer exponent is -1).
adjoint_exponent_dop = 2*z**3*Dz**2 + (5*z**2 + 6*z)*Dz + z

# In the following list, the k-th operator annihilates the power series whose
# general term is the constant term of (x1 + 1/x1 + ... + xk + 1/xk)**n.
# Note : the k-th operator is Fuchsian and of order k.
# Conjecture [Beukers, Vlasenko, 2021] : they are irreducible (for all k).
beukeurs_vlasenko_dops = [(4*z**2 - 1)*Dz + 4*z, (16*z**3 - z)*Dz**2 + (48*z**2 - 1)*Dz + 16*z, (-144*z**6 + 40*z**4 - z**2)*Dz**3 + (-1296*z**5 + 240*z**3 - 3*z)*Dz**2 + (-2592*z**4 + 288*z**2 - 1)*Dz - 864*z**3 + 48*z, (-1024*z**7 + 80*z**5 - z**3)*Dz**4 + (-14336*z**6 + 800*z**4 - 6*z**2)*Dz**3 + (-55296*z**5 + 2048*z**3 - 7*z)*Dz**2 + (-61440*z**4 + 1344*z**2 - 1)*Dz - 12288*z**3 + 128*z, (14400*z**10 - 4144*z**8 + 140*z**6 - z**4)*Dz**5 + (360000*z**9 - 82880*z**7 + 2100*z**5 - 10*z**3)*Dz**4 + (2880000*z**8 - 515520*z**6 + 9268*z**4 - 25*z**2)*Dz**3 + (8640000*z**7 - 1158720*z**5 + 13608*z**3 - 15*z)*Dz**2 + (8640000*z**6 - 825600*z**4 + 5528*z**2 - 1)*Dz + 1728000*z**5 - 109440*z**3 + 320*z, (147456*z**11 - 12544*z**9 + 224*z**7 - z**5)*Dz**6 + (4866048*z**10 - 338688*z**8 + 4704*z**6 - 15*z**4)*Dz**5 + (55296000*z**9 - 3075840*z**7 + 31808*z**5 - 65*z**3)*Dz**4 + (265420800*z**8 - 11450880*z**6 + 82880*z**4 - 90*z**2)*Dz**3 + (530841600*z**7 - 17072640*z**5 + 78720*z**3 - 31*z)*Dz**2 + (371589120*z**6 - 8432640*z**4 + 21120*z**2 - 1)*Dz + 53084160*z**5 - 783360*z**3 + 768*z, (-2822400*z**14 + 826624*z**12 - 31584*z**10 + 336*z**8 - z**6)*Dz**7 + (-138297600*z**13 + 34718208*z**11 - 1105440*z**9 + 9408*z**7 - 21*z**5)*Dz**6 + (-2489356800*z**12 + 528711680*z**10 - 13751904*z**8 + 90384*z**6 - 140*z**4)*Dz**5 + (-20744640000*z**11 + 3670284800*z**9 - 76058880*z**7 + 367920*z**5 - 350*z**3)*Dz**4 + (-82978560000*z**10 + 12003174400*z**8 - 191870208*z**6 + 637488*z**4 - 301*z**2)*Dz**3 + (-149361408000*z**9 + 17261690880*z**7 - 203784192*z**5 + 417888*z**3 - 63*z)*Dz**2 + (-99574272000*z**8 + 8929320960*z**6 - 73200384*z**4 + 76960*z**2 - 1)*Dz - 14224896000*z**7 + 952627200*z**5 - 4935168*z**3 + 1792*z, (-37748736*z**15 + 3358720*z**13 - 69888*z**11 + 480*z**9 - z**7)*Dz**8 + (-2264924160*z**14 + 174653440*z**12 - 3075072*z**10 + 17280*z**8 - 28*z**6)*Dz**7 + (-51791265792*z**13 + 3421896704*z**11 - 50110464*z**9 + 223776*z**7 - 266*z**5)*Dz**6 + (-577102675968*z**12 + 32232701952*z**10 - 384334848*z**8 + 1312416*z**6 - 1050*z**4)*Dz**5 + (-3329438515200*z**11 + 154681344000*z**9 - 1461829632*z**7 + 3620160*z**5 - 1701*z**3)*Dz**4 + (-9766352977920*z**10 + 370055577600*z**8 - 2675785728*z**6 + 4449600*z**4 - 966*z**2)*Dz**3 + (-13317754060800*z**9 + 401552179200*z**7 - 2117173248*z**5 + 2094976*z**3 - 127*z)*Dz**2 + (-6849130659840*z**8 + 159205294080*z**6 - 571023360*z**4 + 271488*z**2 - 1)*Dz - 761014517760*z**7 + 13070499840*z**5 - 28606464*z**3 + 4096*z, (914457600*z**18 - 270648576*z**16 + 11059840*z**14 - 140448*z**12 + 660*z**10 - z**8)*Dz**9 + (74071065600*z**17 - 19486697472*z**15 + 696769920*z**13 - 7584192*z**11 + 29700*z**9 - 36*z**7)*Dz**8 + (2370274099200*z**16 - 550176012288*z**14 + 17038986624*z**12 - 156601632*z**10 + 498696*z**8 - 462*z**6)*Dz**7 + (38714476953600*z**15 - 7861661079552*z**13 + 208388936448*z**11 - 1587838560*z**9 + 3984288*z**7 - 2646*z**5)*Dz**6 + (348430292582400*z**14 - 61302652637184*z**12 + 1371240707328*z**10 - 8466726048*z**8 + 16052916*z**6 - 6951*z**4)*Dz**5 + (1742151462912000*z**13 - 262594912849920*z**11 + 4872727756800*z**9 - 23679448320*z**7 + 32006700*z**5 - 7770*z**3)*Dz**4 + (4645737234432000*z**12 - 592052526858240*z**10 + 8923673318400*z**8 - 32838948864*z**6 + 29054476*z**4 - 3025*z**2)*Dz**3 + (5973090729984000*z**11 - 633557545205760*z**9 + 7552421959680*z**7 - 19955195136*z**5 + 10089816*z**3 - 255*z)*Dz**2 + (2986545364992000*z**10 - 258683438039040*z**8 + 2355318466560*z**6 - 4133152512*z**4 + 935592*z**2 - 1)*Dz + 331838373888000*z**9 - 22924354682880*z**7 + 152023080960*z**5 - 156432384*z**3 + 9216*z, (15099494400*z**19 - 1381236736*z**17 + 31313920*z**15 - 261888*z**13 + 880*z**11 - z**9)*Dz**10 + (1434451968000*z**18 - 117405122560*z**16 + 2348544000*z**14 - 17022720*z**12 + 48400*z**10 - 45*z**8)*Dz**9 + (55037657088000*z**17 - 4003398942720*z**15 + 70018781184*z**13 - 434058240*z**11 + 1022736*z**9 - 750*z**7)*Dz**8 + (1108906868736000*z**16 - 71140560076800*z**14 + 1076366573568*z**12 - 5616568320*z**10 + 10682496*z**8 - 5880*z**6)*Dz**7 + (12785043898368000*z**15 - 717120208896000*z**13 + 9269412790272*z**11 - 39924943872*z**9 + 59245296*z**7 - 22827*z**5)*Dz**6 + (86299046313984000*z**14 - 4189825542389760*z**12 + 45579233525760*z**10 - 158120100864*z**8 + 174913200*z**6 - 42525*z**4)*Dz**5 + (335607402332160000*z**13 - 13938763707187200*z**11 + 125309288448000*z**9 - 339239956480*z**7 + 262498016*z**5 - 34105*z**3)*Dz**4 + (712309588623360000*z**12 - 24959281161830400*z**10 + 181267082772480*z**8 - 367154708480*z**6 + 180852320*z**4 - 9330*z**2)*Dz**3 + (739706111262720000*z**11 - 21504803733504000*z**9 + 122558195957760*z**7 - 175131279360*z**5 + 47196224*z**3 - 511*z)*Dz**2 + (301361749032960000*z**10 - 7121431166976000*z**8 + 30648175165440*z**6 - 28318801920*z**4 + 3168192*z**2 - 1)*Dz + 27396522639360000*z**9 - 512812803686400*z**7 + 1580138496000*z**5 - 819609600*z**3 + 20480*z]

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

# Example 8. of [Kauers, Koutschan, Verron 2023]. Is it algebraic?
example8ofKauers = (z-2)**3*(z-1)**3*z**3*Dz**3 + QQ(19/5)*(z-2)**2*(z-1)**2*z**2*(z**2 - QQ(16547/9576)*z + QQ(2420/1197))*Dz**2 + QQ(99/80)*(z-2)*(z-1)*z*(z**4 + QQ(8816399/112266)*z**3 - QQ(8566381/37422)*z**2 + QQ(7980386/56133)*z - QQ(3200/6237))*Dz - QQ(9/20)*z**6 + QQ(5640547/68040)*z**5 - QQ(20050393/136080)*z**4 - QQ(2904319/30240)*z**3 + QQ(5167531/54432)*z**2 + QQ(1144387/19440)*z + QQ(320/63)


### Chyzak's examples !Not Fuchsian! ###
pLQR8 = (1296*z**9 - 32085*z**8 + 248800*z**7 - 672000*z**6)*Dz**8 + (-3888*z**8 + 64170*z**7 - 248800*z**6)*Dz**7 + (17496*z**7 - 222120*z**6 + 644000*z**5)*Dz**6 + (-73116*z**6 + 730200*z**5 - 1736000*z**4)*Dz**5 + (2592*z**6 + 195840*z**5 - 1663600*z**4 + 3528000*z**3)*Dz**4 + (-19440*z**5 - 294660*z**4 + 2490800*z**3 - 5376000*z**2)*Dz**3 + (74520*z**4 - 17820*z**3 - 1849600*z**2 + 5376000*z)*Dz**2 + (-165780*z**3 + 1133040*z**2 - 2374400*z)*Dz + 1296*z**3 + 116685*z**2 - 896240*z + 2016000
# pLQR8_bad = pLQR8(z**j*Dz**i --> Dz**i*z**j). van Hoeij's code finds irreducibility very quickly.
pLQR8_bad = (1296*z**9 - 32085*z**8 + 248800*z**7 - 672000*z**6)*Dz**8 + (89424*z**8 - 1989270*z**7 + 13684000*z**6 - 32256000*z**5)*Dz**7 + (2412504*z**7 - 47387070*z**6 + 282783200*z**5 - 564480000*z**4)*Dz**6 + (32667732*z**6 - 554379540*z**5 + 2786728000*z**4 - 4515840000*z**3)*Dz**5 + (2592*z**6 + 237639240*z**5 - 3384909100*z**4 + 13746488000*z**3 - 16934400000*z**2)*Dz**4 + (42768*z**5 + 923905260*z**4 - 10598804000*z**3 + 32577216000*z**2 - 27095040000*z)*Dz**3 + (249480*z**4 + 1798681140*z**3 - 15576004000*z**2 + 32191488000*z - 13547520000)*Dz**2 + (508140*z**3 + 1502846040*z**2 - 8731502400*z + 9096192000)*Dz + 1296*z**3 + 280305*z**2 + 366756520*z - 1071592000
# monodromy at 1e-500 in 3min but too large loss of precision (in charpoly)
pLQR12 = (4096*z**15 - 8057595*z**14 + 4363520256*z**13 - 606943051776*z**12 - 263183196487680*z**11 + 100120377950208000*z**10)*Dz**12 + (716800*z**14 - 1321445580*z**13 + 667618599168*z**12 - 86185913352192*z**11 - 34476998739886080*z**10 + 12014445354024960000*z**9)*Dz**11 + (53771264*z**13 - 92383148256*z**12 + 43264674941184*z**11 - 5139383740268544*z**10 - 1885383259041300480*z**9 + 594715045024235520000*z**8)*Dz**10 + (2274022144*z**12 - 3618236338680*z**11 + 1559181490122240*z**10 - 168798968881053696*z**9 - 56320334797366886400*z**8 + 15859067867312947200000*z**7)*Dz**9 + (60012393152*z**11 - 87790839893664*z**10 + 34510550040138240*z**9 - 3367273163015356416*z**8 - 1010635834250546380800*z**7 + 249780318910178918400000*z**6)*Dz**8 + (1033753455728*z**10 - 1378540881648768*z**9 + 489246143695921152*z**8 - 42452845749189476352*z**7 - 11295000342150355353600*z**6 + 2397891061537717616640000*z**5)*Dz**7 + (8192*z**10 + 11817978434854*z**9 - 14219473030174656*z**8 + 4498666973572939776*z**7 - 341451819511938809856*z**6 - 78958354168459925913600*z**5 + 13987697858970019430400000*z**4)*Dz**6 + (348160*z**9 + 89429350059090*z**8 - 95870207845702656*z**7 + 26609265851213979648*z**6 - 1729382001408369229824*z**5 - 338152972193221312512000*z**4 + 47957821230754352332800000*z**3)*Dz**5 + (5856256*z**8 + 439042399810752*z**7 - 412729363214499456*z**6 + 98427354914525552640*z**5 - 5322236663399228375040*z**4 - 845224841008159653888000*z**3 + 89920914807664410624000000*z**2)*Dz**4 + (47985408*z**7 + 1342311357395808*z**6 - 1083810651335691264*z**5 + 215867787180707414016*z**4 - 9318275106273660764160*z**3 - 1127233709339754627072000*z**2 + 79929702051257253888000000*z)*Dz**3 + (198625984*z**6 + 2376272747116176*z**5 - 1601962666488175104*z**4 + 255781061899193548800*z**3 - 8259771543067023114240*z**2 - 676730454788951506944000*z + 23978910615377176166400000)*Dz**2 + (381497456*z**5 + 2126092481531712*z**4 - 1148741029122895872*z**3 + 137823913299263422464*z**2 - 2958274941652429701120*z - 123157676435039059968000)*Dz + 4096*z**5 + 248398369*z**4 + 697951026217824*z**3 - 283323135285181440*z**2 + 22701827323680325632*z - 242892071580928573440
