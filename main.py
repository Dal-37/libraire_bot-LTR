import sqlite3
import discord
import os

conn = sqlite3.connect("librairie.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS fantastique(
            date INT PRIMARY KEY,
            title TEXT,
            auteur TEXT);
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS réaliste(
            date INT PRIMARY KEY,
            title TEXT,
            auteur TEXT);
            """)


cur.execute("""CREATE TABLE IF NOT EXISTS sf(
            date INT PRIMARY KEY,
            title TEXT,
            auteur TEXT);
            """)

cur.execute("""CREATE TABLE IF NOT EXISTS theatre(
            date INT PRIMARY KEY,
            title TEXT,
            auteur TEXT);
            """)
cur.execute("""CREATE TABLE IF NOT EXISTS poesie(
            date INT PRIMARY KEY,
            title TEXT,
            auteur TEXT);
            """)
cur.execute("""CREATE TABLE IF NOT EXISTS idee(
            date INT PRIMARY KEY,
            title TEXT,
            auteur TEXT);
            """)
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS policier(
            date INT PRIMARY KEY,
            title TEXT,
            auteur TEXT);
            """)
conn.commit()

class Bot(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print("Bot en ligne")

    async def on_message(self, message):
        #recherche par genre( réaliste, SF, fantastique, théâtre, poèsie, idée, policier)
        if message.content.startswith("/réaliste"):

            cur.execute("SELECT * FROM réaliste;")
            repr = cur.fetchall()


            embedr = discord.Embed(
                title="Réaliste",
                description="""Sont dans la catégorie réaliste les romans et nouvelles se déroulant dans la vie 
                courante comme les grands classiques de la littérature de XIXe siècle.""",
                colour= discord.Colour.dark_red()

            )

            embedr.add_field(name="Oeuvres:", value=str(repr))

            await message.channel.send(embed=embedr)

        if message.content.startswith("/SF"):

            cur.execute("SELECT * FROM sf;")
            repsf = cur.fetchall()

            embedsf = discord.Embed(
                title="Science-fiction",
                colour=discord.Colour.purple()

            )

            embedsf.add_field(name="Oeuvres:", value=str(repsf))

            await message.channel.send(embed=embedsf)

        if message.content.startswith("/fantastique"):

            cur.execute("SELECT title FROM fantastique;")
            repf = cur.fetchall()
            print(repf)

            embedf = discord.Embed(
                title="Fantastique/Fantasy",
                colour=discord.Colour.dark_green()

            )

            embedf.add_field(name="Oeuvres:", value=str(repf))

            await message.channel.send(embed=embedf)

        if message.content.startswith("/theatre"):

            cur.execute("SELECT * FROM theatre;")
            rept = cur.fetchall()

            embedt = discord.Embed(
                title="Théâtre",
                colour=discord.Colour.blue()

            )

            embedt.add_field(name="Oeuvres:", value=str(rept))

            await message.channel.send(embed=embedt)

        if message.content.startswith("/poesie"):

            cur.execute("SELECT * FROM poesie;")
            repp = cur.fetchall()

            embedp = discord.Embed(
                title="Science-fiction",
                colour=discord.Colour.dark_gold()

            )

            embedp.add_field(name="Oeuvres:", value=str(repp))

            await message.channel.send(embed=embedp)

        if message.content.startswith("/idee"):

            cur.execute("SELECT * FROM idee;")
            repi = cur.fetchall()

            embedi = discord.Embed(
                title="Littérature d'idée",
                colour=discord.Colour.dark_teal()

                )

            embedi.add_field(name="Oeuvres:", value=str(repi))

            await message.channel.send(embed=embedi)

        if message.content.startswith("/policier"):

            cur.execute("SELECT * FROM policier;")
            reppol = cur.fetchall()

            embedpol = discord.Embed(
                title="Policier",
                colour=discord.Colour.light_grey()
               )

            embedpol.add_field(name="Oeuvres:", value=str(reppol))

            await message.channel.send(embed=embedpol)

        #recherche par auteur
        if message.content.startswith("/auteur"):
            auteur = message.content.split(" ")[1]
            autvar = (auteur,)
            cur.execute("SELECT title FROM fantastique WHERE auteur = ?", autvar)
            resultf = cur.fetchall()
            cur.execute("SELECT title FROM sf WHERE auteur = ?", autvar)
            resultsf = cur.fetchall()
            cur.execute("SELECT title FROM réaliste WHERE auteur = ?", autvar)
            resultr = cur.fetchall()
            cur.execute("SELECT title FROM idee WHERE auteur = ?", autvar)
            resulti = cur.fetchall()
            cur.execute("SELECT title FROM poesie WHERE auteur = ?", autvar)
            resultp = cur.fetchall()
            cur.execute("SELECT title FROM theatre WHERE auteur = ?", autvar)
            resultt = cur.fetchall()
            cur.execute("SELECT title FROM policier WHERE auteur = ?", autvar)
            resultpol = cur.fetchall()

            embedaut = discord.Embed(
                title="Voici le résultat de votre recherche",
                colour=discord.Colour.blurple()
            )

            embedaut.add_field(name="Fantastique:", value=str(resultf))
            embedaut.add_field(name="SF", value=str(resultsf))
            embedaut.add_field(name="Réaliste", value=str(resultr))
            embedaut.add_field(name="Littérature d'idée", value=str(resulti))
            embedaut.add_field(name="Poesie", value=str(resultp))
            embedaut.add_field(name="Théâtre", value=str(resultt))
            embedaut.add_field(name="Policier", value=str(resultpol))





            await message.channel.send(embed=embedaut)

        if message.content.startswith("/date"):
            date = message.content.split(" ")[1]
            datevar = (int(date),)
            cur.execute("SELECT title FROM fantastique WHERE date = ?", datevar)
            resultf = cur.fetchall()
            cur.execute("SELECT title FROM sf WHERE date = ?", datevar)
            resultsf = cur.fetchall()
            cur.execute("SELECT title FROM réaliste WHERE date = ?", datevar)
            resultr = cur.fetchall()
            cur.execute("SELECT title FROM idee WHERE date = ?", datevar)
            resulti = cur.fetchall()
            cur.execute("SELECT title FROM poesie WHERE date = ?", datevar)
            resultp = cur.fetchall()
            cur.execute("SELECT title FROM theatre WHERE date = ?", datevar)
            resultt = cur.fetchall()
            cur.execute("SELECT title FROM policier WHERE date = ?", datevar)
            resultpol = cur.fetchall()

            embedate = discord.Embed(
                title="Voici le résultat de votre recherche",
                colour=discord.Colour.blurple()
            )

            embedate.add_field(name="Fantastique:", value=str(resultf))
            embedate.add_field(name="SF", value=str(resultsf))
            embedate.add_field(name="Réaliste", value=str(resultr))
            embedate.add_field(name="Littérature d'idée", value=str(resulti))
            embedate.add_field(name="Poesie", value=str(resultp))
            embedate.add_field(name="Théâtre", value=str(resultt))
            embedate.add_field(name="Policier", value=str(resultpol))

            await message.channel.send(embed=embedate)




if __name__ == "__main__":
    bot = Bot()
    bot.run(os.envir[TOKEN])
