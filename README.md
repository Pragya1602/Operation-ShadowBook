# Operation-ShadowBook
OSINT Investigation of Illegal Betting Sites ; Shadow Payment Ring
Date: Jan 15, 2026

Analyst: Pragya Chauhan

Target: 1xBet Shadow Network (Offshore Gambling Syndicate)
The Objective: A banned offshore betting brand- 1xBet . To track how they actively bypass ISP blocking orders by rapidly spawning "mirror domains" and abusing localized UPI payment systems.
Classification: TLP:CLEAR (Publicly Releasable)

Phase 1:
Because law enforcement continually submits blocking requests to ISPs under section 69A of the IT Act, betting syndicates can't rely on a single URL. They use a technique called Domain Hopping. We will track their domains and the frequency with which they hop. (https://indian.1xbet.com/en)- url we are working with .
OSINT Technique: use crt.sh (Certificate Transparency logs)
 Drop 1xBet into crt.sh (Certificate Transparency logs)- this didnt work.
Hence I created an automation method of extracting this data(Pyhton) which you can view in the .py file. 

The certificate was unextractable hence I pivoted to Internet Archive and found a lot of info:
The number of new urls created:
2025- 719
2026- 171(up until now)
