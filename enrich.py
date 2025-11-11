#!/usr/bin/env python3
# threatintel/enrich.py
import socket, json, time, csv, os, requests

INPUT = "iocs.txt"
OUT_JSON = "reports/threatintel_enriched.json"
OUT_CSV = "reports/threatintel_enriched.csv"
VT_API_KEY = ""  # optional; safe if empty (stub)

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except Exception:
        return None

def get_asn_whois(ip):
    # simple whois via ipinfo.io (no key, limited). Replace with your API if you have keys.
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=8)
        if r.status_code==200:
            data = r.json()
            return {"asn": data.get("org"), "city": data.get("city"), "country": data.get("country")}
    except:
        pass
    return {}

def vt_lookup(ioc):
    if not VT_API_KEY:
        return {"note":"VT key missing - stubbed"}
    headers = {"x-apikey": VT_API_KEY}
    if "." in ioc and all(c.isdigit() or c=='.' for c in ioc): # ip
        url=f"https://www.virustotal.com/api/v3/ip_addresses/{ioc}"
    else:
        url=f"https://www.virustotal.com/api/v3/domains/{ioc}"
    try:
        r = requests.get(url, headers=headers, timeout=12)
        return r.json() if r.status_code==200 else {"error":r.status_code}
    except Exception as e:
        return {"error":str(e)}

def main():
    os.makedirs("reports", exist_ok=True)
    iocs = [x.strip() for x in open(INPUT) if x.strip()]
    out = []
    for i in iocs:
        row = {"ioc": i, "resolved_ip": None, "asn": None, "city": None, "country": None, "vt": None}
        ip = resolve_domain(i) if not all(ch.isdigit() or ch=='.' for ch in i) else i
        row["resolved_ip"] = ip
        if ip:
            who = get_asn_whois(ip)
            row.update(who)
        row["vt"] = vt_lookup(ip or i)
        out.append(row)
        time.sleep(1.5)
    with open(OUT_JSON,"w") as f: json.dump(out,f,indent=2)
    with open(OUT_CSV,"w",newline='') as f:
        writer = csv.DictWriter(f, fieldnames=out[0].keys())
        writer.writeheader()
        writer.writerows(out)
    print("[+] Enrichment complete:", OUT_JSON, OUT_CSV)

if __name__=="__main__":
    main()
