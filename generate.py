import datetime

root = []
Edit = True
url=None
btn_text=None
texte=None
titre=None

story_base=(f"""

  <div id="StoryPadding">
  <div id="Story">
    <h2>{titre}</h2>
  <hr />
  <p>{texte}</p>
  </div>
  </div>
""")

while Edit:
    print(
        "1 - Ajouter un article\n"
        "2 - Ajouter du texte supplémentaire\n"
        "3 - Sauvegarder"
    )

    mode = input("> ").strip()

    if mode == "1":
        article = {}

        button_article = input(
            "Ajouter un bouton ? [Oui/Non] : "
        ).strip().lower()

        if button_article in {"oui", "o"}:
            article["url"] = input("URL du bouton : ").strip()
            article["btn_text"] = input("Texte du bouton : ").strip()
            article["type"] = "story_btn"
        else:
          article["type"] = "story_base"

        article["titre"] = input("Titre de l'article : ").strip()
        article["texte"] = input("Texte de l'article : ").strip()

        root.append(article)

    elif mode == "2":
        texte_supplementaire = input(
            "Texte supplémentaire : "
        ).strip()

        # Store it separately, for example:
        root.append({
            "type": "texte_supplementaire",
            "texte": texte_supplementaire
        })

    elif mode == "3":
        print("Sauvegarde...")
        # Add your save code here
        Edit = False

    else:
        print("Choix invalide.")



prelude="""
<!DOCTYPE html>
<style>
  @media screen and (min-width: 200px) and (max-width: 400px) {
    img { display: none; }
}

@media screen {
  * {
    font-size   : 12px;
    background-color: #EDC9FF;
    text-align: center;
  }
}

a {
  text-decoration: none;
}

p {
  font-size: 120%;
  color: #874392;
}

#Story p{
  background-color: #B98DE1;
  color: white;
}

h1 {
  font-size: xx-large;
  text-align: center;
  color: #874392;
}

h2 {
  font-size: medium;
}

#Story h2 {
  background-color: #B98DE1;
  color: white;
}

#Story {
  background-color: #B98DE1;
  padding: 1%;
  border-radius: 2%;
}

#StoryPadding {
  padding-bottom: 5%;
  padding-left: 2%;
  padding-right: 2%;
}

#CtaBtn {
  text-decoration: none;
  border-radius: 2.5%;
  background-color: #9A66D5;
  color: #DFA952;
  text-align: center;
  padding-top: 3%;
  padding-bottom: 3%;
  transition: transform 0.2s ease;
}

#CtaBtn:hover {
  text-decoration: none;
  background-color: #B370BD;
  color: #FFC849;
  transform: scale(1.05);
}

#CtaBtnPadding {
  background-color: #B98DE1;
  padding-left: 25%;
  padding-right: 25%;
}

@media print {
  p {
    font-family : garamond, serif;
    font-size : 10px;
  }
    img {
    display:none
  }
}

 /* For smart phones */
@media screen and (max-width: 600px) {
}

/* For tablets */
@media screen and (min-width: 600px) and (max-width: 900px) {
}

/* For desktop computers */
@media screen and (min-width: 900px) {
} 

 /* Device dimensions */
@media screen and (max-device-height: 600px) {
}

/* Device orientation */
@media screen and (orientation: portrait) {
}

/* Device aspect ratio */
@media screen and (device-aspect-ratio: 16/9) {
} 
</style>
<html>
<head>
 <meta name="viewport" content="width=device-width, initial-scale=1"> 
</head>

<body>
  <header>
    <h1>Courr-Île</h1>
    <p>l'infolettre pour les eleves, par les eleves</p>
  </header>
"""

file = prelude

for i in range(len(root)):
  texte = root[i]["texte"]
  titre = root[i].get("titre", "")
  url = root[i].get("url", "")
  btn_text = root[i].get("btn_text", "")
  story_btn=(f"""  
    <div id="StoryPadding">
    <div id="Story">
      <h2>{titre}</h2>
    <hr />
    <p>{texte}</p>
    <a href="{url}">
      <div id="CtaBtnPadding">
        <div id="CtaBtn">{btn_text}</div>
      </div>
    </a>
    </div>
    </div>
    """)
  story_base=(f"""

    <div id="StoryPadding">
    <div id="Story">
      <h2>{titre}</h2>
    <hr />
    <p>{texte}</p>
    </div>
    </div>
  """)
  file = file + (
      story_base if root[i]["type"] == "story_base"
      else (
          story_btn if root[i]["type"] == "story_btn"
          else (f"<p>{texte}</p>")
      )
  )

date = datetime.datetime.now()
filename = f"courr-ile-{date.strftime("%Y-%m-%d")}.html"
try:
  with open(filename, "x") as f:
    f.write(file)
    print(f"Fichier HTML sauvgardé dans {filename}")
except FileExistsError:
  overwrite = input(
    f"Le fichier {filename} exsiste déjà. Voulez-vous le remplacer? [Oui/Non] : \n>v"
  ).strip().lower()
  if overwrite in {"oui","o"}:
    with open(filename, "w") as f:
      f.write(file)
      print(f"Fichier HTML sauvgardé dans {filename}")
  else:
      print("Sauvgarde annulée.")
