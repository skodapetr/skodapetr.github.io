---
layout: post
language: cs
title: Mám ročníkový projekt ... co teď?
category: final-thesis
---

Nalezení vhodného tématu a ochotného vedoucího je prvním krokem v ročníkovém projektu a případně bakalářské práci.
Ačkoliv může být splnění předchozích dvou kroků skoro důvodem k oslavě, je třeba neusnout na vavřínech.
Co by tedy měl student dělat dále?

<!-- more -->

Hned na úvod je nutné předeslat, že jednotlivé kroky, jejich relevanci a rozsah je třeba vždy konzultovat s vedoucím práce.
Obecně není možné dát jednotný seznam, který by bylo možné vždy slepě následovat. 
Na druhou stranu jsou některé základní kroky o jejichž shrnutí se pokusím ve zbytku tohoto příspěvku.

Doporučuji, povinnost pro mé studenty, přečíst příspěvek o <a href="{% post_url 2022-03-05-závěrečné-práce.html %}">závěrečných pracích obecně</a> včetně detailů pro oba typy práce.
Zatímco výše zmíněné příspěvky jsou spíše deklarativní, tedy říkají, jak by práce měla vypadat, tento příspěvek se soustředí více na to jak toho dosáhnout.

## Domluvil jsem si téma
Pro zapsání tématu ročníkového projektu, je třeba tří věcí:
* Název projektu
* Krátký popis 
* Odkaz na veřejný URL repozitář

Tuto informaci je třeba poslat vašemu vedoucímu, ten může následně vyplnit potřebné údaje do SIS.
Tyto údaje slouží pouze pro ročníkový projekt, nejedná se tedy o zadání bakalářské práce.
Z toho důvodu si není třeba lámat s popiskem a názvem příliš hlavu. 
Rozsah popisu by měl být 3-5 vět.
Z hlediska obsahu by měl být dostatečný, aby si po jeho přečtení čtenáři bylo jasné, co zhruba budete dělat.

## Textová část práce
Dalším krokem je založení projektu pro text bakalářské práce, ano už teď na začátku.
Osobně doporučuji [overleaf](https://overleaf.com/).
Výhodou je absence nutnosti instalovat prostředí a snadná synchronizace. 
Založte si prázdný projekt a tam zkopírujte šablonu pro bakalářkou práci. 
Pokud jste nikdy nepsali v LaTeXu, je ideální čas se naučit pár základních příkazů.
Jakmile budete mít projekt vytvořený pošlete odkaz svému vedoucímu.
Ideálně je to spojit s předchozím krokem.

Další otázku, kterou je třeba si hned na začátku zodpovědět je jazyk práce.
Zde doporučuji využít nejsilnějšího z trojice: Angličtina, Čeština, Slovenština.
Předem upozorňuji, že nejsem korektorem a za správnost jazykového projevu zodpovídá autor textu.
Současně nedoporučuji volit angličtinu, pokud by se jednalo o první větší text, který v daném jazyce píšete.

## Existující řešení
A stejně jako u každé dlouhodobější práce i zde platí v jisté míře přísloví "dvakrát měř, jednou řež".
Ročníkový projekt je tedy třeba zahájit, pokud se s vedoucím nedohodnete jinak, pomocí rešerše.
V zásadě se jedná o to, že se zamyslíte, zda-li plně rozumíte zadání, problému který chcete řešit.
Pokud ano, pokusíte se najít existující řešení, třeba i jen částečné, vybraného problému. 
Všechna nalezená řešení i postup jejich hledání je pak třeba dokumentovat v sekci **related work**.

Ukažme si to na příkladu, implementace aplikace pro tvorbu poznámek.
Nejprve je třeba identifikovat klíčová slova a fráze, zde se nabízí třeba:
* *note taking app*
* *note management*
* ....

Z hlediska jazyka je v tuto chvíli vhodné přejít do angličtiny, neb tím maximalizujete šanci na nalezení relevantních materiálů.

Dalším krokem je výběr vyhledávače:
* váš oblíbený vyhledávač(e)
* [Google](https://google.com/) / [DuckDUckGo](https://duckduckgo.com/) nebo jiné nelokální alternativy
* [Google Scholar](https://scholar.google.com/) pro vědecké publikace
* [ChatGPT](https://chat.openai.com/chat), [Bing](https://www.bing.com/)

Následně provedeme zadání jednotlivých frází do vyhledávačů/nástrojů a prohlídneme výsledky.
Zběžným pohledem na obsah můžeme provést první filtraci a rozhodnout se o relevanci zdroje. 
Relevantní zdroje je pak třeba detailně nastudovat.
Do textu práce je třeba zanést:
* trojice čas, dotaz, nástroj
* kolik výsledků jsme prohlédli - například prvních 20
* kritéria filtrace
* seznam nalezených/relevantních zdrojů

Jakmile takto identifikujete relevantní zdroje, je třeba přistoupit k jejich detailní analýze.
Pro každý je dobré použít vlastní (nečíslovanou) sekci.
V té je vhodné algoritmus/program/řešení krátce popsat, případně přiložit screenshot.
Případně je možné okomentovat nějaký výraznější vlastnosti oproti ostatním zdrojům.

Nakonec celé sekce je pak vhodné umístit popis kritérií, která vyhodnotíte na každém nástroji.
Tento seznam můžete vymyslet a případně rozšířit na základě zkušeností s předchozího hledání.
Seznam by tedy mohl obsahovat:
* CRUD pro poznámky
* použití Markdownu
* licence
* dostupné zdarma
* lokální instalace
* vkládání obrázků do poznámek

Každý z požadavků je vhodné krátce popsat, stačí několik vět. 
Cílem je se ujistit, že čtenář skutečně pochopí požadavek stejně jako autor textu.

Následně je možné vložit tabulku, ve které jsou sloupce kritéria a řádky nástroje.
Zde se snažte držet jednoduchého značení, například:
* splňuje - fajvka
* nesplňuje - křížek
* nelze rozhodnout, nedostatek informací - otazník
* částečně splňuje - pomlčka

Pokud chcete zvednout úroveň své práce, můžete tu samou tabulku vložit do svého repozitáře ve strojově čitelném formátu.
Jen pozor na to, že je pak třeba lehce změnit obsah, neb identifikace toolu názvem, není pro strojové zpracování dobrý nápad.

Na závěr této sekce je pak třeba vložit odstavec, který tuto sekci shrnuje:
* jaké skupiny nástrojů jsme našli
* jaké byli zajímavé funkcionality
* jaký nástroj(e) je nejblíže tomu co chceme dělat
* proč tento nástroj(e) není řešením našeho problému

..... pokračování příště.

