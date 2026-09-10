## 📊 Status Veckouppgift 4


Här nedan presenteras en översikt över statusen på lösande av uppgfterna.

| Uppgift                           | Status |
|:----------------------------------|:------:|
| 1. Diskutera tillsammans          |   🟢   |
| 2. Projekt                        |   🔴   |
| 3. Extra                          |   🔴   |


## 1️⃣Diskutera tillsammans
1. Vilka fördelar kan du se med CI & CD på din arbetsplats?  
CI & CD medger att nya features och funktionalitet snabbt kan levereras med hög kvalité. Samtliga stakeholders 
kan ta del av den senaste koden och feedback kan snabbt leda till åtgärder.  


2. Vad är poängen med linting?  
Jag har främst använt linting vid html design. Linting möjliggör att samtliga i ett projekt följer samma regler avseende stil och kod.
Linting hjälper utveckalren att hitta fel och inkonsekvent eller onödigt komplicerad design


3. Hur arbetar man med git och flera branches inom ett team? Skulle du vilja ända något på din arbetsplats?
Man använder en "main" branch som innehåller den testade och mest aktuella kodbasen. Ansvariga för system
integration säkerställer att det som integreras också testas så att den inte genererar fel. Normalt skapar man en utvecklingsbranch
som används för ny kod och kodutveckling. Innan något mergas tillbaka till "main" säkerställer man att allt fungerar på utckecklingsbranchen ("dev").  
Från "dev" branchen skapar man nya brancher för att utveckla nya features eller funktionalitet. Dessa kallas ofta featurebrancher. Liksom på "main" 
branchen ska features testas innan de mergas tillbaka till "dev" branchen.


4. Vad är en pull request?
En "pull request" gör man då man är färdig med sin kod på en isolerad branch. Requesten gör mina ändringar synliga för övriga i projektet som kan granska 
och läsa koden. De kan då även testa koden och godkänna ändringarna. Då ändringarna är godkända genomförs en "merge" till den branch koden var utbranchad 
från, dev eller main. 



## 2️⃣Projekt
Jag har valt att skapa två enkla klasser där fokus varit på att öva på metodik snarare än avancerad funktionalitet. En klass, Calculator, simulerar en 
miniräknare som klarar räknesätten addition, subtraktion, multiplikation och division. Klasser har en metod för varje räknesätt som returnerar resultatet 
av beräkningen av två parametrar. Klassen CalculatorService har en metod som tar en calculator, ett räknesätt och två tal som parametrar. 
Jag har valt att 
enhetstesta Calculator och endast Integrationstesta Calculator_Service. 

Som övning har jag utnyttjat parameterisering i mina enhetstester.

### Testfiler
#### Unittester
tests/unit/test_calculator_unit.py

``` python
pytest -v -m unittest
```
#### Integrationstester
tests/integration/test_calculator_calculator_service.py

``` python
pytest -v -m integrationtest
```

## 3️⃣Extra
todo