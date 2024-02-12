import requests

def check_git_vulnerability(url):
    git_urls = [url + "/.git/config", url + "/.git/index", url + "/.git/HEAD"]
    
    for git_url in git_urls:
        try:
            response = requests.get(git_url)
            if response.status_code == 200:
                print(f"[+] Found exposed .git directory at: {git_url}")
                return
        except requests.exceptions.RequestException as e:
            print(f"[-] Error occurred while checking {git_url}: {e}")
    
    print("[*] .git directory not found or not exposed")

if __name__ == "__main__":
    website_url = input("Enter the URL of the website to check for .git vulnerability: ")
    check_git_vulnerability(website_url)
