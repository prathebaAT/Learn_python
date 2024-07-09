import feedparser

class JobListing:
    def __init__(self, title, company, location, job_type, link, published, category):
        self.title = title
        self.company = company
        self.location = location
        self.job_type = job_type
        self.link = link
        self.published = published
        self.category = category

class JobPortal:
    def __init__(self, feed_url):
        self.feed_url = feed_url
        self.job_listings = []

    def fetch_jobs(self):
        job_feed = feedparser.parse(self.feed_url)
        if job_feed.entries:
            for entry in job_feed.entries:
                title = entry.title
                company = entry.get('company', 'N/A')
                location = entry.get('location', 'N/A')
                job_type = entry.get('type', 'N/A')
                link = entry.link
                published = entry.get('published', 'N/A')
                category = entry.get('category', 'N/A')

                job = JobListing(title, company, location, job_type, link, published, category)
                self.job_listings.append(job)
        else:
            print("No entries found in the RSS feed.")

    def print_job_listings(self):
        for job in self.job_listings:
            print(f"Title: {job.title}")
            print(f"Company: {job.company}")
            print(f"Location: {job.location}")
            print(f"Type: {job.job_type}")
            print(f"Link: {job.link}")
            print(f"Published: {job.published}")
            print(f"Category: {job.category}")
            print("=" * 30)


if __name__ == "__main__":
    feed_url = ''
    portal = JobPortal(feed_url)
    portal.fetch_jobs()
    portal.print_job_listings()
