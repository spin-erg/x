- There are 2 methods to match up LSE-traded entities via Wikidata:
  - Use Wikidata entity `Q7110731`, instance of _Wikimedia category_, with associated Wikipedia categories in various languages.
    - This Wikipedia category has a bunch of useless subcategories (in that they're rather arbitrary).
    - This Wikipedia category lists 430 companies (there are many more trading on LSE by my count).
    - This seems to require maintenance, and may be missing some companies (TBC)
    - Some companies (e.g. Nokia) are "formerly traded on LSE":
      - Nokia is listed on LSE in that their bonds are yet to mature (LSE:38YE matures February 2019),
        but its Wikipedia page has no 'traded as' entry as said bonds have trading status `w`, meaning
        _'No Active Session'_
        - see: https://www.londonstockexchange.com/prices-and-markets/prices-help/trading-status.htm
    - There are 387 total pages in the formerly listed Wikipedia category, with Wikidata entity `Q7164691`.
  - Use Wikidata entity `Q171240`, instance of _stock exchange_, which has somewhere between 500-1000 linked entities

## Notes

- "Admission to Trading Only" was introduced in 2011, and explained here: https://www.lseg.com/sites/default/files/content/documents/att_only_factsheet.pdf
  - A plainer English explanation for the clients of an asset management company is [available here](https://www.debevoise.com/~/media/files/insights/publications/2011/01/admission%20to%20trading%20on%20london%20stock%20exchange%20no__/files/view%20client%20update/fileattachment/admissiontotradingonlondonstockexchangenowpossib__.pdf)
