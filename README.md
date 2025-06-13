# Wiki Scraper

A simple Python script that fetches current country leaders from an API, saves them to JSON, pretty-prints their info (with clickable terminal links!), and pulls the first paragraph from each leader’s Wikipedia page.

---

## 🚀 Features

- Fetches country codes and leader data from `https://country-leaders.onrender.com`  
- Saves the results to `leaders.json`  
- Pretty-prints each leader’s:
  - Full name  
  - Birth date  
  - Place of birth
  - Wikipedia URL
- Extracts and prints the **first real paragraph** from a leader’s Wikipedia article  

---

## 🛠 Requirements

- Python 3.13.2
---

## 🎬 Usage

Simply run the script:

1. Fetches and saves all leaders to `leaders.json`.  
2. Pretty-prints each leader’s data in your console (with clickable hyperlinks if supported).  
3. Extracts & prints the first paragraph from the first leader’s Wikipedia page.  

---

## 🔧 Configuration

- **`root_url`**  
  By default it’s set to `https://country-leaders.onrender.com`.  
  To target a different API endpoint, edit the `root_url` variable at the top of `leaders_scraper.py`.

- **Output file**  
  The JSON dump is written to `leaders.json`. Change this in the `save(...)` call if you need a different path.

---

## 📄 Example Output

```text
Country: belgium
  Name: Marc Wilmots
  Birth Date: 1969-02-22
  Place of Birth: Brussels
  Wikipedia url
  --------------------
...
First paragraph:
 Marc Wilmots (born 22 February 1969) is a Belgian former professional footballer...
```

And your `leaders.json` will look like:

```json
{
  "belgium": [
    {
      "first_name": "Marc",
      "last_name": "Wilmots",
      "birth_date": "1969-02-22",
      "place_of_birth": "Brussels",
      "wikipedia_url": "https://en.wikipedia.org/wiki/Marc_Wilmots"
    },
    ...
  ],
  ...
}
```

---

