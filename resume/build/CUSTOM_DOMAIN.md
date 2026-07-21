# Wiring a custom domain (e.g. `sudhanshubhatnagar.com`) to this site

## When you're ready

1. Buy the domain from any registrar (Namecheap, Google Domains, Cloudflare, etc.)
2. In the registrar's DNS settings, add these records:

   For an apex domain (`sudhanshubhatnagar.com`):
   ```
   A  185.199.108.153
   A  185.199.109.153
   A  185.199.110.153
   A  185.199.111.153
   ```

   For a `www` subdomain, additionally add:
   ```
   CNAME  www  sudhanshu311.github.io.
   ```

3. Create a file named `CNAME` (no extension) at the repo root containing exactly one line — the apex domain, no protocol, no trailing slash. Example:
   ```
   sudhanshubhatnagar.com
   ```

4. Commit + push. GitHub Pages picks it up automatically and provisions HTTPS via Let's Encrypt within a few minutes.

5. In the repo Settings → Pages, verify "Enforce HTTPS" is checked (it will only appear once the cert is issued — can take 15 min).

## Don't create `CNAME` before the DNS records propagate — GH Pages will show an "improperly configured" warning otherwise.

## After the domain is live, update the following files to use the new URL:

- `resume/build/data.py` → `PROFILE["site"]` = `"https://sudhanshubhatnagar.com/resume/"`
- `sitemap.xml` (at repo root)
- `robots.txt` (Sitemap: line)
- `resume/sw.js` (nothing to change — uses relative URLs)

Then `cd resume/build && python3 generate.py` and commit.
