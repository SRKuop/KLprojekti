#KaloriLaskuri
#Muistilista: -----------------------------------------------------------------------------------------------
#Käyttäjän tiedot: ikä pituus paino sukupuoli tärkeät päivittäisen kulutuksen laskentaan. Valmis (x)
#Nimi lähinnä siksi, että ohjelma voi tervehtiä käyttäjää aloitettaessa. Valmis (x)
#Painon muutos, jotta käyttäjä voi seurata omaa edistystään. Valmis ( )
#Aktiivisuuden määrittämiselle paremmat termit. Valmis ( )
#Kulutuksen laskenta on vielä profiilissa 26.2.2024
#Parannusidea #1 iän merkintä vuoden perusteella datetimellä, jotta se päivittyy käytettäessä. Valmis( )
#Parannusidea #2 laskenta ja tietojen muutokset omassa luokassaan? Valmis (x)
#Parannusidea #3 Painon lisäksi muuta seurantaa edistyksen seurantaan? Esim. bodyfat% tai Hip-2-Waist. Ei BMI,
#koska se ei tuloksissaan ota huomioon yksilön lihaksen ja rasvan määrää. Valmis ( )
#Korjaus: Muuta niin, että avatessa lukee tiedostosta tiedot käyttäjäksi, jotta tietoja ei tarvitse syöttää,
#joka kerta uusiksi. Lisäksi mieti parempi tapa varastoida tiedot, kuin tekstitiedosto. Valmis ( )
#Muistutus: Muuta profiilin tiedot piilotetuiksi ennen, kun ohjelman lopullinen versio on valmis. Valmis ( )
#Kun olet tyytyväinen tähän laskuriin, ala työstämään uuden kielen opettelua, jotta saat sen siirrettyä puhelimeen
#ja tabletille käyttöjärjestelmittäin. Sen jälkeen voit jatkaa "Salaisen ainesosa tm" työstämistä. Sillä ei ole
#kiire koska se vaatii muiden apua ja lopuksi muuta se moduliksi, jota käyttää tämän kanssa yhteistyössä.
#-------------------------------------------------------------------------------------------------------------

class Profiili:
    def __init__(self, nimi: str, sukupuoli: str, ika: int, pituus: float, paino: float):
        self.nimi = nimi
        self.pituus = pituus
        self.paino = paino
        self.ika = ika
        self.sukupuoli = sukupuoli
        self.kulutus = 0
        self.kalorit = 0

    def __str__(self):
        return f"{self.nimi};{self.sukupuoli};{self.ika};{self.pituus};{self.paino}"

    def laske_kulutus(self):
        while self.sukupuoli.lower() not in ["mies", "nainen"]:
            self.sukupuoli = input("Anna sukupuoli uudestaan (mies/nainen): ")

        while True:
            aktiivisuustaso = input("Ilmoita aktiivisuustasosi (Vähäinen/Matala/Keskiverto/Korkea/Hyvin korkea): ")
            if aktiivisuustaso.lower() == "vähäinen":
                aktiivisuus = 1.2
                break
            elif aktiivisuustaso.lower() == "matala":
                aktiivisuus = 1.375
                break
            elif aktiivisuustaso.lower() == "keskiverto":
                aktiivisuus = 1.55
                break
            elif aktiivisuustaso.lower() == "korkea":
                aktiivisuus = 1.725
                break
            elif aktiivisuustaso.lower() == "hyvin korkea":
                aktiivisuus = 1.9
                break
            else:
                print("Anna yksi edellämainituista tasoista.")

        if self.sukupuoli.lower() == "mies":
            perusaineenvaihdunta = 10 * self.paino + 6.25 * self.pituus - 5 * self.ika + 5
        elif self.sukupuoli.lower() == "nainen":
            perusaineenvaihdunta = 10 * self.paino + 6.25 * self.pituus - 5 * self.ika - 161
        
        kaloritarve = perusaineenvaihdunta * aktiivisuus
        self.kulutus = kaloritarve

    def kulutus_manuaalisesti(self, kalorikulutus:float):
        self.kulutus = kalorikulutus

    def lisaa_kalorit(self, kaloreita:float):
        self.kalorit = kaloreita
            
#Laskenta luokassa nimensä mukaisesti lisää matematiikkaa kaiken taustalla. 

class Laskenta:
    def __init__(self):
        self.profiilit = {}

    def lisaa_profiili(self, profiili: Profiili):
        self.profiilit[profiili.nimi] = profiili

    def paino_kasvaa(self, profiili: Profiili, muutos: float):
        profiili.paino += muutos

    def paino_vahenee(self, profiili: Profiili, muutos: float):
        profiili.paino -= muutos

    def laske_painon_muutos(self, profiili: Profiili):
        kulutus = profiili.kulutus
        kalorit_elimistoon = profiili.kalorit
        erotus = kalorit_elimistoon - kulutus
        muutos = erotus / 7700
        
        if muutos > 0:
            self.paino_kasvaa(profiili, muutos)
        elif muutos < 0:
            self.paino_vahenee(profiili, abs(muutos))
        
        return muutos
    
    def hae_profiili(self, nimi: str):
        return self.profiilit.get(nimi)
    
    def kaikki_profiilit(self):
        return self.profiilit


#Sovellus ottaa vastaan komennot käyttäjältä ja palauttaa käyttäjän komentojen perusteella halutut tiedot
#Parannusehdotus #1 Kehitä lopulliseen versioon paremmat komennot, kuin numeroidut. Valmis ( ) 

class KaloriLaskuri:
    def __init__(self):
        self.__luettelo = Laskenta()
        self.__kayttajan_nimi = None

    def kayttajan_nimi(self):
        self.__kayttajan_nimi = input("Anna nimesi: ")

    def ohje(self):
        print("1 lisää käyttäjä")
        print("2 käyttäjän tiedot")
        print("3 laske kulutus")
        print("4 lisää kulutus manuaalisesti")
        print("5 lisää kalorit")
        print("6 laske painon muutos")
        print("0 lopetus")

    def lisaa_profiili(self, nimi: str, sukupuoli: str, ika: int, pituus: float, paino: float):
        profiili = Profiili(nimi, sukupuoli, ika, pituus, paino)
        self.__luettelo.lisaa_profiili(profiili)

    def valitse_profiili(self, nimi: str):
        return self.__luettelo.hae_profiili(nimi)

    def laske_kulutus(self, profiili: Profiili):
        profiili.laske_kulutus()
        return profiili.kulutus

    def lisaa_kalorit(self, profiili: Profiili, kalorit: float):
        profiili.lisaa_kalorit(kalorit)

    def laske_painon_muutos(self):
        nimi = self.__kayttajan_nimi
    
        if self.__luettelo.profiilit[nimi].kulutus == 0:
            print("Päivittäistä kulutusta ei ole vielä ilmoitettu. Ilmoita se ensiksi tai anna minun laskea se sinulle.")
            return
    
        vanha_paino = self.__luettelo.profiilit[nimi].paino
    
        muutos = self.__luettelo.laske_painon_muutos(self.__luettelo.profiilit[nimi])
        uusi_paino = vanha_paino + muutos 
    
        print(f"Uusi paino on {uusi_paino:.2f} kilogrammaa.")

    def lisaa_kulutus_manuaalisesti(self):
        nimi = self.__kayttajan_nimi
        kulutus = float(input("Anna kulutus: "))
        if nimi in self.__luettelo.profiilit:
            self.__luettelo.profiilit[nimi].kulutus_manuaalisesti(kulutus)
            print("Kulutus lisätty onnistuneesti.")
        else:
            print("Profiilia ei löytynyt.")


    def suorita(self):
        print("Hei, tervetuloa käyttämään KaloriLaskuria!")
        try:
            with open("profiilit.txt", "r") as tiedosto:
                sisalto = tiedosto.read().strip()
                if sisalto:
                    tiedot = sisalto.split(";")
                    if len(tiedot) == 5:
                        self.lisaa_profiili(tiedot[0],tiedot[1],int(tiedot[2]),float(tiedot[3]),float(tiedot[4]))
                    else:
                        print("Virheellinen tiedostomuoto")
        except FileNotFoundError:
            print("Näytät käyttävän sovellusta ensimmäisen kerran. Luothan ensiksi käyttäjän.")
            with open("profiilit.txt", "w") as tiedosto:
                pass

        self.kayttajan_nimi()

        self.ohje()

        while True:
            print()
            komento = input("komento: ")
            if komento == "0":
                nimi = self.__kayttajan_nimi
                print(f"Heippa {nimi}!")
                break

            elif komento == "1":
                if self.__kayttajan_nimi is None:
                    print("Jokin meni pieleen, antaisitko nimesi uudelleen.")
                    continue

                sukupuoli = input("Sukupuoli (mies/nainen): ")
                if sukupuoli.lower() not in ["mies", "nainen"]:
                    print("Virheellinen sukupuoli, ole hyvä ja anna sukupuoli joko 'mies' tai 'nainen'.")
                    continue

                annettu_ika = input("Ikä: ")
                if not annettu_ika.isdigit():
                    print("Ikä täytyy olla kokonaisluku.")
                    continue
                ika =int(annettu_ika)

                pituus_str = input("Pituus (cm): ")
                if not pituus_str.replace(".", "", 1).isdigit():
                    print("Pituuden täytyy olla numero.")
                    continue
                pituus = float(pituus_str)

                paino_str = input("Paino (kg): ")
                if not paino_str.replace(".", "", 1).isdigit():
                    print("Painon täytyy olla numero.")
                    continue
                paino = float(paino_str)

                if sukupuoli.lower() in ["mies", "nainen"] and ika >= 0 and pituus > 0 and paino > 0:
                    self.lisaa_profiili(self.__kayttajan_nimi, sukupuoli, ika, pituus, paino)
                    with open("profiilit.txt", "w") as tiedosto:
                        tiedosto.write(f"{self.valitse_profiili(self.__kayttajan_nimi)}")
                else:
                    print("Virheelliset tiedot. Tarkista syöte ja yritä uudelleen.")

            elif komento == "2":
                if self.__kayttajan_nimi is None:
                    print("Jokin meni pieleen, antaisitko nimesi uudelleen.")
                    continue
                nimi = self.__kayttajan_nimi
                valittu_profiili = self.valitse_profiili(nimi)
                if valittu_profiili:
                    print(f"Tämänhetkiset tiedot: {valittu_profiili.nimi}: {valittu_profiili.ika}v {valittu_profiili.sukupuoli},pituus: {valittu_profiili.pituus}cm, paino: {valittu_profiili.paino}kg")

            elif komento == "3":
                if self.__kayttajan_nimi is None:
                    print("Jokin meni pieleen, antaisitko nimesi uudelleen.")
                    continue
                nimi = self.__kayttajan_nimi
                valittu_profiili = self.valitse_profiili(nimi)
                if valittu_profiili:
                    kulutus = self.laske_kulutus(valittu_profiili)
                    print(f"Kalorinkulutus: {kulutus:.1f}")

            elif komento == "4":
                self.lisaa_kulutus_manuaalisesti()

            elif komento == "5":
                if self.__kayttajan_nimi is None:
                    print("Jokin meni pieleen, antaisitko nimesi uudelleen.")
                    continue
                nimi = self.__kayttajan_nimi
                kalorit = float(input("Tämänpäiväinen kalorisaanti: "))
                valittu_profiili = self.valitse_profiili(nimi)
                if valittu_profiili:
                    self.lisaa_kalorit(valittu_profiili, kalorit)

            elif komento == "6":
                self.laske_painon_muutos()

            else:
                self.ohje()

sovellus = KaloriLaskuri()
sovellus.suorita()