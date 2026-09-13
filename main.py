import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client

# Supabase Credentials (Project Settings -> API se lein)
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def scrape_and_upload():
    # Sample Target URL (Apni university site ke acc change karein)
    url = "https://example-university-papers.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example Extraction (Site ke structure ke hisab se modify karein)
    for link in soup.find_all('a', href=True):
        if '.pdf' in link['href']:
            paper_data = {
                "university": "AKTU",
                "course": "B.Tech CSE",
                "subject": link.text.strip() or "Mathematics",
                "year": "2024",
                "pdf_url": link['href']
            }
            # Supabase Insert
            supabase.table('pyq_papers').insert(paper_data).execute()
            print(f"Saved: {paper_data['subject']}")

if __name__ == "__main__":
    scrape_and_upload()
