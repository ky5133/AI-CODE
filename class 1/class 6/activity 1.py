import time, pandas as pd
from textblob import TextBlob
from colorama import init, Fore
import textblob
init(autoreset=True)
try:
    df=pd.read_csv(r"C:/Users/Dinesh Bachani/Downloads/imdb_top_1000.csv")
except FileNotFoundError:
    print(Fore.RED+"File not found. Please check the file path and try again.")
    raise SystemExit
genres=sorted({g.strip() for xs in df['Genre'].dropna() for g in xs.split(',')})
def recommend(genre=None, mood=None, rating=None, n=5):
    d = df
    if genre: 
        d = d[d["Genre"].str.contains(genre, case=False, na=False)]
    if rating is not None: 
        d = d[d["IMDB_Rating"] >= rating]
    if d.empty:

        return "No suitable movie recommendations found."
    d, need_nonneg, out = d.sample(frac=1).reset_index(drop=True), bool(mood), []
    for _, r in d.iterrows():
        ov = r.get("Overview")
        if pd.isna(ov): 
            continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((r["Series_Title"], pol))
            if len(out) == n: 

                break
    return out if out else "No suitable movie recommendations found."

def get_genre():
     print(Fore.GREEN + "Available Genres: ", end="") 
     for i, g in enumerate(genres, 1): 
        print(f"{Fore.CYAN}{i}. {g}") 
        print() 
        while True:
            x = input(Fore.YELLOW + "Enter genre number or name: ").strip() 
            if x.isdigit() and 1 <= int(x) <= len(genres): 
               return genres[int(x) - 1] 
            x = x.title() 
            if x in genres: 
                return x 
            print(Fore.RED + "Invalid input. Try again.\n")


def get_rating():
    while True:
        x = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if x.lower() == "skip":
            return None
        try:
            r = float(x)
            if 7.6 <= r <= 9.3:
                return r
            else:
                print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

def senti(p):

    return "Positive 😊" if p > 0 else "Negative 😞" if p < 0 else "Neutral 😐"
def show(recs, name):
    print(Fore.YELLOW + f"\n🍿 AI-Analyzed Movie Recommendations for {name}:")
    for i, (t, p) in enumerate(recs, 1):
        print(f"{Fore.CYAN}{i}. 🎥 {t} (Polarity: {p:.2f}, {senti(p)})")
def dots():
    for _ in range(3): 
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
mood=input(Fore.GREEN + "How is your mood today ").strip().lower()
print(Fore.BLUE + "Analyzing your mood", end="",flush=True) 
dots()
mp = TextBlob(mood).sentiment.polarity
md = "positive 😊" if mp > 0 else "negative 😞" if mp < 0 else "neutral 😐"
print(f"\n{Fore.GREEN}Your mood is {md} (Polarity: {mp:.2f}).\n")
print(Fore.BLUE +"🎥Welcome to your peronal movie recomendation Assistant🎥")
name=input(Fore.GREEN + "Please enter your name: ").strip()
print(Fore.GREEN + f"Hello {name}! Nice to meet you.")
print(Fore.GREEN + "Let's find some movies for you!")
mood=(Fore.MAGENTA+"How is your mood today")
print(Fore.BLUE + "Analyzing your mood", end="",flush=True)
dots()
mp=TextBlob(mood).sentiment.polarity
md="positive 😊" if mp>0 else "negative 😞" if mp<0 else "neutral 😐"
print(f"\n{Fore.GREEN}Your mood is {md} (Polarity: {mp:.2f}).\n")
rating=get_rating()
print(Fore.GREEN + f"Finding movies for {name} with a rating of {rating} or higher... ",flush=True)
dots()
recs=recommend(mood=mood,rating=rating,n=5,genre=genres)    
print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
while True:
    a = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
    if a == "no":
        print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿\n"); break
    if a == "yes":
        recs = recommend(genre=genres, mood=mood, rating=rating, n=5)
        print(Fore.RED + recs + "\n") if isinstance(recs, str) else show(recs, name)
    else:
        print(Fore.RED + "Invalid choice. Try again.\n")
