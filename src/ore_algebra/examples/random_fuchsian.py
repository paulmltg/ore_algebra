r"""
Random Fuchsian operators with rational singularities and exponents

This module provides a few irreducible Fuchsian operators extracted from the
dataset used for the experiments described in Chyzak, Goyer, Mezzarobba (2022),
Section 7. These operators were picked at random under some constraints on the
order, singular points, and local exponents at each singular points as
described in the article.

EXAMPLES::

        sage: from ore_algebra.examples.random_fuchsian import irred
        sage: irred[2,5,6].numerator().leading_coefficient().factor()
        (x - 28/3)^5 * (x - 121/16)^5 * (x - 65/12)^5 * (x - 3/10)^5 * (x + 53/10)^5 * (x + 53/6)^5
"""

from sage.repl.preparse import preparse
from sage.rings.polynomial.polynomial_ring_constructor import PolynomialRing
from sage.rings.integer import Integer as Integer
from sage.rings.rational_field import QQ

from ore_algebra import OreAlgebra

Pol, x = PolynomialRing(QQ, 'x').objgen()
Dop, Dx = OreAlgebra(Pol, 'Dx').objgen()

# irred[gen,order,degree] (not sure what gen stands for)

irred = {}

irred[1,2,2] = eval(preparse("""((1) * Dx^2
+ ((-4302*x-33686)/(180*x^2-905*x-4785)) * Dx^1
+ ((7128324*x^2+170561664*x-914731699)/(129600*x^4-1303200*x^3-3614300*x^2+34643400*x+91584900)))"""))

irred[1,4,2] = eval(preparse("""((1) * Dx^4
+ ((-8789*x-250083)/(1683*x^2-11052*x+3105)) * Dx^3
+ ((-573876259*x^2+5184664947*x-1245897126)/(944163*x^4-12400344*x^3+44199378*x^2-22877640*x+3213675)) * Dx^2
+ ((116088953763904*x^3-121641558287931*x^2-5636597753470860*x+12405624767176527)/(19068315948*x^6-375656021136*x^5+2572413374124*x^4-6785971942752*x^3+4745896331940*x^2-1278631299600*x+119741530500)) * Dx^1
+ ((3761488140623395072*x^4-2796968328358578264*x^3-331614221956180131573*x^2+1432286768863927980036*x-2245937427043850033919)/(128367902961936*x^8-3371888445716736*x^7+34161316701057216*x^6-164070061344389376*x^5+363892995858420576*x^4-302696102480290560*x^3+116275864918737600*x^2-21174134321376000*x+1487189808810000)))"""))

irred[2,3,3] = eval(preparse("""((1) * Dx^3
+ ((-381277225*x^2-788431755*x+18325709424)/(5890500*x^3-20196000*x^2-395942580*x+1799463600)) * Dx^2
+ ((-5421494604745625*x^4+48954833592924000*x^3+158868817738775325*x^2-2237565203895017700*x+4543644347878027392)/(3832653825000*x^6-26281054800000*x^5-470186842554000*x^4+4108179397608000*x^3+9287996212071720*x^2-157398483670084800*x+357669086840208000)) * Dx^1
+ ((222834891756421875*x^6-5580440718303193750*x^5+46401236528146447500*x^4-281575459198101293250*x^3+1854138529385081693325*x^2-6637179953341173564900*x+6340899106132497425376)/(111785736562500*x^9-1149796147500000*x^8-18599595251737500*x^7+252513536868450000*x^6+547719056317075500*x^5-17763039204417936000*x^4+44566625258768552940*x^3+355568864800739475600*x^2-2103630734250683352000*x+3186831563746253280000)))"""))

irred[2,5,4] = eval(preparse("""((1) * Dx^5
+ ((24645979552480*x^3-414806362828799*x^2-6140380543550081*x-6807970887923660)/(687429943200*x^4+228462294060*x^3-77245433114850*x^2-243810309252510*x+179137993834800)) * Dx^4
+ ((39480875588243076416000*x^6+9004334923464026624912720*x^5+57348739278644381535502648*x^4+437905499904253879966481524*x^3+3430687887998087028160505643*x^2+4458586592872170141958312920*x+16450811126586577150322962140)/(660922974556580736000*x^8+439305795325895097600*x^7-148460772555796239498960*x^6-518182310198893164224400*x^5+8533907208139565097665820*x^4+52794850945735552025572200*x^3+44431165112749165306696140*x^2-122169761330732357416574400*x+44881707461757822111456000)) * Dx^3
+ ((-402253835580037799210378240000*x^9-1871760751299048495706176012800*x^8+35366864727176365869737027313680*x^7-329248283349614581644685233516262*x^6-7316325084699689719016093175754974*x^5-18710451747784043548921564638802416*x^4+149350570273829052240306182942040927*x^3+1455436299826856363153253804395728020*x^2+6536736734973787060215978100497450300*x+8080926451869911179294697500462495500)/(68048629460345552578560000*x^12+67846387030131238873344000*x^11-22917007589238825119382124800*x^10-87649371017562372839193653280*x^9+2580220984203261078474116322000*x^8+17155950139255521293341465463640*x^7-77412420868986074042558470383300*x^6-947399546294583942949178925074940*x^5-2212531796006159252402319810968700*x^4+1209000517026597119360184763694580*x^3+5134093813469043175883662676944800*x^2-4916802676797802007585931667104000*x+1204195959150245540692093520640000)) * Dx^2
+ ((-1408244176348017185177028920320000*x^12-113307167125184244872088961878860800*x^11-2023970487364409457999053493395916800*x^10-34191194664143302286640771358266700160*x^9-261124545701604411848530588658345971092*x^8-13525082639479340305106227507024448112*x^7+3239929125723180040534344616416176412528*x^6-22186334011720259897145627274075090089672*x^5-68711716381058675159445908389938711427137*x^4+74758072615350661487138424212032151954040*x^3-2109163819586025959854179321275039195747100*x^2-4452741360150523496770216948071050269755000*x-4372889182868609096239111314940270838536050)/(77847632102635312149872640000*x^16+103488355683293516361474048000*x^15-34938878778553050650751104102400*x^14-145315712458960498620639875681280*x^13+5857176658968246783973873411083744*x^12+41193301508811067683259192134214080*x^11-384992156473889264093748343089997296*x^10-4391679024198196090448490552970900080*x^9+868311098675445761000163181217108574*x^8+158853540455244689875169496047335595160*x^7+652074542662890403790315172596993351364*x^6+456192197314549777127809491060529197000*x^5-1810610014852412041276463562624418487586*x^4-1090183192697823476192516598959627570880*x^3+3370708599493843529109864517263175353600*x^2-1954370062395004724391316806493834752000*x+358990082558034599608964151999114240000)) * Dx^1
+ ((43888135231738960167609796858265600000*x^15+2745991295001642206167981620243777536000*x^14+87027679413114261177317195810335851520000*x^13+1629607197737960372591827875078540083200000*x^12+14931831935339715568174333544849248872230400*x^11+55688492267012709532563476548505536405692864*x^10+194933639632012349787469798235901468193103280*x^9+2123811321547684149325060404422898910430424240*x^8+3586366021915833158806299268014042249628165560*x^7-25993269050791222693462053074823540559328262930*x^6+176227717367534240239788147481161963336541639761*x^5+176878019323523638954796039745304746754374982200*x^4-10580895443546795403721240743668643427794083568000*x^3-40923805675211589453288563750285621123920294732800*x^2-80065792010549570600491971728065154640222644736000*x-60499225396935182385758430666053784725524822794240)/(268586687521092245220576460800000*x^20+446314067288108704689087283200000*x^19-150606682448162027994638887034880000*x^18-676805163641812202803250894152704000*x^17+33530339103525366922930885685028518400*x^16+248023313692267199967365283786678634944*x^15-3405408178752769947709774145165531488800*x^14-38861498867445089073768889934449007253120*x^13+102076621309087569294549867223135282702800*x^12+2759808746819783013358987764173511843264540*x^11+7123080175826440478542240835763247296878550*x^10-64275131332467264207936519989249024121529590*x^9-452128819755491433568143743173454071419941700*x^8-837797139938820551482435553488991616196873680*x^7+740373518089517214271543637198534839225335150*x^6+3045508271741071672053605867901046674980136906*x^5-1601652666551615085397328028988103942240504400*x^4-4346682197741918461257761022574264177370976000*x^3+5282855303922093597736621493658978696948480000*x^2-2196418794622626059507181392978096186035200000*x+322760803426277747816427489779363630899200000)))"""))

irred[2,5,6] = eval(preparse("""((1) * Dx^5
+ ((-5128108531200*x^5+89585591787360*x^4+28064493964392*x^3-4948326183852076*x^2+4892914911799558*x+41370383855939061)/(44980531200*x^6-381397420800*x^5-4676947564608*x^4+40304971055712*x^3+86646529572240*x^2-834609791595624*x+241535292878880)) * Dx^4
+ ((35056170970573399621632000*x^10-434789329773835743178752000*x^9-3305648457917553664136033280*x^8+22792665869942700841571013120*x^7+465108882635341293309549139392*x^6-1753053890698517839871570697408*x^5-18538013647205533683445279361392*x^4+72414214947553729513331730338048*x^3+118709159502187973554538821380836*x^2-762208621587711835892072253657660*x+2377928695823413036816695548892219)/(7081368654619607040000*x^12-120088210101257502720000*x^11-963477126879176164147200*x^10+25177003225114181820825600*x^9-3765200727574963366373376*x^8-1813645336239967268370511872*x^7+5153305346717529650097867264*x^6+51125138126663956004482043904*x^5-217103325945909740110961421696*x^4-438066783002485834276994006400*x^3+2584504629075704917655487861216*x^2-1411114043168410296798390147840*x+204187541971302188734225190400)) * Dx^3
+ ((-612051226940523129584311228830842880000*x^15+10324427076269127450956438437201182720000*x^14-49933317436012214710964939439108115660800*x^13-462398619437540465245364797677913677004800*x^12+6728602980027558925980237222783478279987200*x^11+39337236081028039200696445567476074225817600*x^10-425925566835883335355767099081097720627201536*x^9-4654928501598374372148140815533663982807253760*x^8+30991396791188548655433440466850885639347772416*x^7+140202857718924018262369373404786637638641722624*x^6-1097502990502246490552626498705068161802477547968*x^5+269110712624929497288604629812645050570860646176*x^4+11170125853205024119056722640122174960826359768608*x^3-21918377244998160863069183799494910968611942069320*x^2-82167839593933099911499431801722354136152862768750*x+223864649760312097807101767749471466220511235629185)/(6051950750448565913294733312000000*x^18-153946497214535395419434778624000000*x^17-582455815717350862498692323082240000*x^16+44593062523523075425683017359687680000*x^15-180352724044835623060254452437116518400*x^14-4807808272930945609517250107542221619200*x^13+37512485557684305686403452720087864573952*x^12+220805995655277560717674604814220154044416*x^11-2812703173665757400762154893370006678011904*x^10-2208371167862206282964315679499280790650880*x^9+101053414584623222279252066020215629485817856*x^8-153139365772647315166132372068315121826537472*x^7-1699218781212162993045571377301772337982119936*x^6+5059288353965785374429601244051420058637584384*x^5+9106418471846965156647320437717599070640401920*x^4-45161096585432447272206363982560354021840804096*x^3+34573745616304558247197011575621643533032258560*x^2-9713764545512201149476460727450861018788147200*x+937051457292884456614066928443353210636288000)) * Dx^2
+ ((521036245868079542239645442824948649664970752000000*x^20-3803417047856570661383091369316039458300100608000000*x^19-150005275536183381844529548193286337409733812551680000*x^18+706215589918660855979489135382024567450053294161920000*x^17+29945411254467973534757166508835548458582357149614080000*x^16-158785064762488030567462913700518834911010734070169600000*x^15-2935163609060241903287459233437043451241867566050236825600*x^14+17388956102427859095438322433303704399674850388319569510400*x^13+157170824736711889146885451092209710896642072825630182117376*x^12-907138337185034657457300293109193654901134869579601258635264*x^11-5612881416903653630120646027424243809633283399502607205963776*x^10+25092656919740490884289848422758823435481824851127737760094208*x^9+165610407678721264241040109318670973344212492227267787785123584*x^8-517681023584445900530512597617644126542912712700056016023124992*x^7-3237555231691775470650174671463380196925217704131319022064037632*x^6+10615767254383484776344206998834323555069981936031440878264120320*x^5+11112457812946964974476479210607096273510464025608077073260278896*x^4-52222072933934061057702129518111071764278742354910855233770300640*x^3+49212230692554838263617438095595516789875307271433564209952812840*x^2+187749938002028739453991746311705923381995225556788785768962128600*x-388071097517798585430870130161305856442539915150489771008864152695)/(544439919102830266116420493072190668800000000*x^24-18465587256237659859115261723365133516800000000*x^23+8421937327768909839122505021080293343232000000*x^22+6383780362084631377023215900731365012799488000000*x^21-56152707277658288981077058047717984839212728320000*x^20-795793866557554794944564047109738312490056417280000*x^19+12482637536789640763530120395889351870901522740019200*x^18+30308671066600432940678362224613593038602067823820800*x^17-1265879298491201494467983595848414824415938913482309632*x^16+2394761309683901384356132910218154391516120901214011392*x^15+69323113717835713711961624438351780098662059518992580608*x^14-323609510907769734120835812584194796795762142173863084032*x^13-1997183774118448443388899822017157189059903177442311798784*x^12+15748642449231153747743589892267023264509496864340388610048*x^11+20349160474003658381980578082260798864654161516819647561728*x^10-391592176440181459741211471966414826379958689438057529081856*x^9+370183740082324528972410232075534260731288737232339401900032*x^8+4768385190401304751226136279041594515474007825499576870764544*x^7-11644165359112475408542605454239801014889110985455773678534656*x^6-17705588849326635643393631190566290212011824959316712257781760*x^5+84982428789318175938789064253613383174957329088726400481579008*x^4-81134962938168953596270025612380702618361893070899500290211840*x^3+33078350066195905935762193325462086791592574428486517912371200*x^2-6256578571884720474563455827155327829243800939422691229696000*x+452661996359636323072220556196159130520935195280233594880000)) * Dx^1
+ ((-1711556981257167358660943961493854380165831994675165344563200000*x^25+15878842159232600956279416531888462454645289660596773244108800000*x^24+160843957999504169182957780358165864441505549047731024966975488000*x^23-4943517621097874961968163167971715772024265865910388382112940032000*x^22+65204179307964560949247804644939130703867015047091625498362511360000*x^21+6425085796080511073532087719492319428606636646513316645425905664000*x^20-5367063561439336020382187762247501608922702729856326050748463841280000*x^19+1139946794760929015098098726866672333260860317955416414415224832000000*x^18+13786322014617093553495688839262406672424029522072784913847872520192000*x^17+4484324041321078066689066293667961616167698208929424202465060770529280000*x^16+2346756292288342786913914602538081499436830984628539409010432887954898944*x^15-492216116472357807205800651901520699492107820689939262120879990943867125760*x^14+909976155407779426144671348969156350556061367185912804269543273492120576000*x^13+21395365215606868516773104448131873036117191598970850381868750856736406999040*x^12-64646052247079978701549176788371073862238401328273148004253858272283414517760*x^11-410950567918099238850233809548865651332381818984223380399065118884480628145152*x^10+1179412940419675095096459194990511962698145277057938818237560501315841683182080*x^9+5320587951999766816847939794337132161669228614779834580308250784313520624021760*x^8-2436650678687825489153812953885271342494826107433111999153812954866742258832000*x^7-138149850594284798121659073800245847318225112655101832249673213874072604803664960*x^6+413639639931664661913717169684760245990379500463935227134572628834903417705923808*x^5+371763378142585805466820515342247615578564577539325238549218843560933267175297200*x^4-4532516268456881444671627646524125285916819069316127054727635582444868338507885000*x^3+3217210082496068227026286487440148702174283452566073833772306730265630286802115500*x^2+21183849236156711918837256587734295321531493109255080107056307246562131568107313750*x-34702037287245803422976784945540540609637281732067549910009824505574785203557570075)/(519428752494490742932718094360214824253359390720000000000*x^30-22021614819297680455585027542146607653241382502400000000000*x^29+103406270867472244544846871978342745715158837886976000000000*x^28+8319615677729575183439086343982580359973313917747200000000000*x^27-120836496879060266664702387796640802605158522412523847680000000*x^26-974629350257429032244107267352529101572208017127610777600000000*x^25+29719840320259048002936657985031462364134868295212200047411200000*x^24-29636395181755004015769604438749928340604537153716194639872000000*x^23-3587676338630990384765151864581213384799402669366246353512955904000*x^22+19754121335987475489774265714312204549392388550368878422403317760000*x^21+234992855303269946421635632123516355004488467650477959734342264553472*x^20-2358639981173758307487990135156022028793151045884885548473376613335040*x^19-6916228754051775442704302822230140440344863659572304648153153069383680*x^18+149513158592181308655730270357001015972043904379210377684818492338995200*x^17-107990473784591900718455108891391447120501512715062945691718156151685120*x^16-5617525635290816583753427442875150329816208384662263843056579544296194048*x^15+17379110526359201702798837125919170713908409714104208986186746978054963200*x^14+120437546983286098648450177286078387701790252942173347344015326631920926720*x^13-672798515366052206334459588265611478494471508554950722997918113035725045760*x^12-1078480038806297722693446286095589130232128778435454845952941484815081799680*x^11+13172607326276152078861575924256669049783202879119837028215606775384118394880*x^10-8758875956425744523347307214292583018536273898777749691573514465746508840960*x^9-126794492484229520036963422074795165383758698713031438791925041229590805872640*x^8+278445867232961144547229615378621993633965218320990735195775446351811222568960*x^7+337369796019708308882505950640280097322326091646593263411978676667952072294400*x^6-1715325885796662913472674430695347835546361933571738193772045227960804860002304*x^5+1927063836331851101559549154301508604957849494211890461744713035547610293862400*x^4-1012343173032021322820714759389581823508015376021645602010988251055447474176000*x^3+281052460894244050063907778112668259789944237080500453726507334334606213120000*x^2-40066274258243420548967284249304845964924214146620243441697483656082227200000*x+2319028457365415709581460905401833033752830213070688965313853123775692800000)))"""))

irred[3,3,5] = eval(preparse("""((1) * Dx^3
+ ((-37276100316*x^4-8601296521971*x^3+149474526562354*x^2-851516260119981*x+1606375172887730)/(60207507360*x^5-1357738101720*x^4+10766894818680*x^3-33663219309720*x^2+21109635466920*x+50367182065200)) * Dx^2
+ ((-244962605945443932*x^8+45859894027452154377*x^7-1007721565559420627511*x^6+7688451401051418251751*x^5-10700444172772190981212*x^4-151584123526871575963626*x^3+812508614558115570090512*x^2-1394044793550319515881430*x+523936206539527555046735)/(14645054712768480*x^10-660520578153355920*x^9+12685635710012415150*x^8-134497429354272364380*x^7+847929913011990138330*x^6-3135724106883297930000*x^5+5862200627940909582330*x^4-1360052817241898920140*x^3-11899750655303006826330*x^2+8591086400229176243400*x+10249083020317568427000)) * Dx^1
+ ((3612630465937377271296*x^12-34847198210004251666553504*x^11+1214323652964968262407229084*x^10-18389563613810827299100150875*x^9+158046460793874663922760730966*x^8-826155207999895832163818812791*x^7+2505450484359110983431547996570*x^6-3180870458747487002695340817081*x^5-3436514987049513841913427774018*x^4+12416246770727538978764204120859*x^3+2523223218251925254166023092170*x^2-20023104718177006637248729222320*x-8670024295507734979387367314900)/(143931597717088621440*x^15-9737394363136772972640*x^14+296805518829532843570440*x^13-5374736569789980282940050*x^12+64117800033505201966052070*x^11-526993531541075189435464620*x^10+3020206887409287886072602840*x^9-11842329693864967921225061460*x^8+29534459320186329611791388700*x^7-35715306059567401841457843960*x^6-20824869529453481354980517400*x^5+121727941389987133586763768390*x^4-81381731516357672782477425330*x^3-124551810125977847709358161900*x^2+105950131451442330918186321000*x+84264988358975155511950170000)))"""))

irred[4,4,3] = eval(preparse("""((1) * Dx^4
+ ((3348152203*x^2-31637133076*x+59125377396)/(75315240*x^3-1303422120*x^2+6899452560*x-11001070080)) * Dx^3
+ ((-322596484080077900*x^4+15988727042629656667*x^3-231730571492254215098*x^2+1274479487856801877152*x-2356655368804738543008)/(3502819174654800*x^6-121241119183984800*x^5+1690882851101043600*x^4-12129907155140174400*x^3+47104852136916974400*x^2-93741424638762700800*x+74734623717020467200)) * Dx^2
+ ((-4944775196347932477070*x^6+96246681870541809327831*x^5-632950856064133846487028*x^4+1334050468347601932646402*x^3+3222997729871087195102772*x^2-22316961365697458203852824*x+34776180106511727325739760)/(366044603751426600*x^9-19004545432089617400*x^8+429494309943265967400*x^7-5539645199758602933000*x^6+44896840115193463597200*x^5-236914340999728269477600*x^4+813426786960396801192000*x^3-1751552688077007546931200*x^2+2146303658529110797516800*x-1140749296416600411340800)) * Dx^1
+ ((-17483283827572888736888400*x^8+89323443588786794725249395*x^7+6027729750374375677821936804*x^6-118685781917169083324382695614*x^5+1112622460040899341209884074958*x^4-6323380727201323628141021864232*x^3+22047940443205483377192041931420*x^2-43367858299121997001379196583080*x+36959585891499041335544730527712)/(351915282046621533240*x^12-24361293304547944224480*x^11+761355391311403516227600*x^10-14196991050674080962112800*x^9+175828583426543752660595640*x^8-1522970839368971326255521600*x^7+9455918973122537925993023040*x^6-42388134777081857232134265600*x^5+136115535491916678212760685440*x^4-305297941208861119092244070400*x^3+453976854359579592885043200000*x^2-401870462937137059149769605120*x+160194054796627495844094935040)))"""))