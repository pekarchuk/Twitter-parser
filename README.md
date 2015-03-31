# Twitter-parser
These methods are for parsing Twitter, using no API:
- getting user tweets
- getting followers
- getting following

Example of usage:
```python
tw = Twitter_methods('email@example.com', 'password')
tw.get_following("JeremyClarkson")
```
Result:
```python
['SamLFC17', 'teamginola', 'fbhutto', 'prettynormalme', 'nigelpauley', 'NivenJ1', 'OldowlThe', 'ShipsInPics', 'therealstucarr', '_youhadonejob', 'maitlis', 'GrumpyOldRick', 'AL1MB', 'DelevingnePoppy', 'JillieSpeed', 'DeborahJaneOrr', 'KermodeMovie', 'simonmayo', 'EvanHD', 'mrevgenylebedev', 'Simon_Kelner', 'Dholderd', 'bbcnickrobinson', 'micheleandjel', 'natnoo', 'davedins', '_seenit', 'SirPatStew', 'CrapTaxidermy', 'TheLTDA', 'HailoLondon', 'OfficialClancy', 'chelseahandler', 'LeahDeWavrin', 'rianacrehan', 'MarkElliott52', 'JamesBlunt', 'willcarling', 'ImogenEJ', 'OfficialJimWest', 'SimonJCLeBON', 'garyjkemp', 'vonsorgenfri', 'Nigella_Lawson', 'tarardavies', 'Bourdain', 'hughlaurie', 'caitlinmoran', 'TinaHobley', 'marthaward2', 'takiinoue', 'flynnoallott', 'Overstretched_', 'usasoccerguy', 'grahnort', 'laurabailey_uk', 'claire_neate', 'EllieHarrison__', 'ConvoyPQ17', 'melissakite1', 'JimCookePriest', 'amylmansell', 'Augusta__', 'PigeonJon', 'allottnick', 'GaryLineker', 'leshinton', 'ProfBrianCox', 'MBrundleF1', 'MatthewdAncona', 'GuidoFawkes', 'ShaneJacobson', 'AccidentalP', 'RichardHammond', 'Aiannucci', 'JensonButton', 'Amy__Macdonald', 'colinkett', 'daraobriain', 'RealSAlexander', 'alaindebotton', 'TheSunNewspaper', 'OC', 'BBC_TopGear', 'WillGompertzBBC', 'LewisHamilton', 'nickjfrost', 'toadmeister', 'vb_h', 'Lord_Sugar', 'tnewtondunn', 'Tickets4Troops', 'GeorgeMichael', 'ChelseaFC', 'nickmasondrums', 'VictoriaCoren', 'BillBailey', 'richardpbacon', 'charliesheen', 'Baddiel', 'Number10gov', 'sniffpetrol', 'simonpegg', 'TheAlexJames', 'bookcunt', 'LordGaryFarrow', 'AussieGrit', 'jackwhitehall', 'CharlesPEBrooks', 'tomwookieford', 'JoanneSalley', 'gmurray22', 'RowlandFrench', 'ChrisMoyles', 'Nicole_Ferger', 'tiff_tv', 'RikkiBrest', 'prodnose', 'BJGoldsmith', 'XanderArmstrong', 'RobBrydon', 'MrJChrist', 'janem', 'charltonbrooker', 'JuliaBradbury', 'geeeeunit', 'ianhislop', 'LindaPe', 'MaryHambro', 'ClaudiaWinkle', 'eddieizzard', 'SarahKSilverman', 'achrisevans', 'mediaguardian', 'stephenfry', 'campbellclaret', 'roseastor', 'PrivateEyeNews', 'camillalong', 'RachelSJohnson', 'wossy', 'henconrad', 'mermhart', 'rupertmurdoch', 'gilescoren', 'jimmycarr', 'EmClarkson1', 'Jemima_Khan', 'skstanding', 'MrJamesMay', 'emmafreud', 'Alice__BB', 'katereardon', 'Christa_dsouza', 'edvaizey']
```
