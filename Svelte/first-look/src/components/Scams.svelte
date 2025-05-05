<script context="module">
	export const selectedScam = () => {
		const scams = [
			'Din grand-tante fra sveits har dessverre gått bort, men gode nyheter. Du har arvet en masse penger! 5,000,000$ Eneste som trengs er at du betaler inn noen kroner i frakt!',
			'Gratulerer! Du har blitt valgt til å motta en revolusjonerende ny eliksir utviklet av en hemmelig forskergruppe. Den gir deg superintelligens, uendelig energi og en perfekt hårdag for livet! Alt du trenger å gjøre er å sende inn en liten administrasjonsavgift – før det er for sent!',
			'Høyt ærede mottaker! En skjult tekst fra en 3000 år gammel egyptisk grav har avslørt DITT navn som den utvalgte. Du har rett til å motta den hellige amuletten som gir evig lykke og rikdom. Men først må du betale en beskjeden sum for at våre arkeologer skal frakte den til deg.',
			'NASA har nettopp funnet en gammel satellitt svevende i rommet – og gjett hva? Den tilhører din oldefar! Vi har åpnet databasen og funnet bevis for at du er den rettmessige arvingen til en intergalaktisk konto med 10 milliarder kreditter. Vi trenger bare en liten overføringsavgift for å aktivere kontoen din.',
			'Kjære borger! Etter en gjennomgang av kongehusets gamle registre har vi oppdaget at du egentlig er en fjern slektning av kongen. Som takk for din tålmodighet gjennom årene, ønsker vi å gi deg en tittel, et slott og en livslang inntekt. Bare send inn penger for dokumenter, så ordner vi papirene umiddelbart!',
			'En sjokkerende feil har skjedd i det globale lotterisystemet, og din e-postadresse er tilfeldig valgt som vinner av jackpotten! 100 millioner dollar venter på deg! Overføringsteamet vårt trenger kun en liten bekreftelsesbetaling for å sette i gang transaksjonen. Skynd deg, før feilen oppdages!'
		];
		return scams[Math.floor(Math.random() * scams.length)];
	}
	export const selectedScamPayment = () => {
		const payments = []
        for (let i = 0; i < 5000; i+= 250) {
			payments.push(i)
        }
        return payments[Math.floor(Math.random() * payments.length)];
    }
</script>