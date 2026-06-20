# Operation-ShadowBook
OSINT Investigation of Illegal Betting Sites ; Shadow Payment Ring
Date: June 15, 2026

Analyst: Pragya Chauhan

Target: 1xBet Shadow Network (Offshore Gambling Syndicate)
The Objective: A banned offshore betting brand- 1xBet . To track how they actively bypass ISP blocking orders by rapidly spawning "mirror domains" and abusing localized UPI payment systems.
Classification: TLP:CLEAR (Publicly Releasable)

Phase 1:
Because law enforcement continually submits blocking requests to ISPs under section 69A of the IT Act, betting syndicates can't rely on a single URL. They use a technique called Domain Hopping. We will track their domains and the frequency with which they hop. 
OSINT Technique: use crt.sh (Certificate Transparency logs)
 Drop 1xBet into crt.sh (Certificate Transparency logs)- this didnt work.
Hence I created an automation method of extracting this data(Pyhton) which you can view in the .py file. 

The certificate was unextractable hence I pivoted to Internet Archive and found a lot of info:
The number of new urls created:
2025- 719
2026- 171(up until now)

Phase 2: Content Delivery Networks (CDNs) & IP Geolocation
OSINT Technique: Use tool lookup extensions or command-line commands (dig or nslookup;I used nslookup) to find out where the mirrors point.

The Blueprint: Most offshore syndicates route traffic through security reverse-proxies like Cloudflare or Akamai to mask their true origin IPs. However, sometimes their staging or admin login panels are misconfigured, revealing origin servers located in offshore, non-cooperative hosting jurisdictions.
the urls I found:
<img width="1823" height="876" alt="image" src="https://github.com/user-attachments/assets/6c2fe5f7-9367-453b-87c5-db7190740b25" />
<img width="1772" height="712" alt="Screenshot 2026-06-20 131635" src="https://github.com/user-attachments/assets/b1ccdca8-6293-445b-94c5-f3617e500d67" />
<img width="1775" height="897" alt="Screenshot 2026-06-20 131646" src="https://github.com/user-attachments/assets/6b85cc01-182e-479b-9a7b-83af83b22b7c" />
using the most recently active url , the IPv4 adress is: 207.241.237.3
Now extracting info from my favourite tool ViewDNS.info
this currently has hit a dead end. But enough info for case study .


