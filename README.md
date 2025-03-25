Ecco una guida dettagliata per avviare correttamente e rendere funzionale il chatbot AI_RIQA, basata sulla struttura del progetto. La guida copre l’installazione delle dipendenze, la configurazione del database, l’avvio del server backend, l’accesso all’interfaccia grafica e i test di base per verificare che tutto funzioni. È pensata per utenti con conoscenze tecniche di base, ma include anche dettagli per configurazioni avanzate.

Guida per Avviare il Chatbot AI_RIQA
Benvenuto nella guida per avviare AI_RIQA, un chatbot avanzato con interfaccia grafica e supporto per simulazioni matematiche, fisiche, quantistiche, biologiche e astrali. Segui i passaggi qui sotto per installarlo e avviarlo correttamente sul tuo sistema.

Prerequisiti
	•	Sistema Operativo: Windows, macOS o Linux.
	•	Python: Versione 3.10 o superiore installata (scaricabile da python.org).
	•	Git: Per clonare il repository (opzionale, scaricabile da git-scm.com).
	•	Node.js e npm: Per il frontend Vue.js (scaricabili da nodejs.org).
	•	Browser: Chrome, Firefox o Edge per accedere all’interfaccia grafica.

Passo 1: Clonare o Scaricare il Progetto
	1	Clona il Repository: git clone https://github.com/TeknologyGroup/AI_RIQA.git
	2	cd AI_RIQA
	3   Scarica Manualmente:
	◦	Vai su GitHub, scarica il progetto come ZIP, estrailo e entra nella cartella AI_RIQA.

Passo 2: Installare le Dipendenze
Il progetto richiede librerie Python per il backend e Node.js per il frontend.
	1	Backend (Python):
	◦	Crea un ambiente virtuale (opzionale ma consigliato): python -m venv venv
	◦	source venv/bin/activate  # Linux/macOS
	◦	venv\Scripts\activate     # Windows
	◦	
	◦	Installa le dipendenze: pip install -r requirements.txt
	◦	
	◦	Contenuto di requirements.txt (assicurati che sia presente): fastapi==0.115.0
	◦	uvicorn==0.30.6
	◦	numpy==1.26.4
	◦	scipy==1.13.0
	◦	qiskit==0.46.0
	◦	requests==2.31.0
	◦	pytesseract==0.3.10
	◦	pillow==10.4.0
	◦	matplotlib==3.9.2
	◦	psycopg2-binary==2.9.9
	◦	
	2	Frontend (Vue.js):
	◦	Entra nella directory del frontend: cd frontend
	◦	
	◦	Installa le dipendenze Node.js: npm install
	◦	
	◦	Torna alla directory principale: cd ..
	◦	
	3	Tesseract OCR (per il caricamento di immagini):
	◦	Linux: sudo apt install tesseract-ocr
	◦	macOS: brew install tesseract
	◦	Windows: Scarica e installa da qui, poi aggiungi il percorso a PATH.

Passo 3: Configurare il Database
AI_RIQA supporta SQLite (default) o PostgreSQL. Scegli uno dei due.
	1	SQLite (Default):
	◦	Non richiede configurazione aggiuntiva.
	◦	Esegui: python backend/database.py
	◦	
	◦	Verrà creato un file riqa.db nella directory principale.
	2	PostgreSQL (Opzionale):
	◦	Installa PostgreSQL localmente o usa un servizio cloud (es. Heroku, AWS).
	◦	Crea un database chiamato riqa.
	◦	Imposta le variabili d’ambiente: export DATABASE_TYPE="postgresql"
	◦	export DATABASE_URL="dbname=riqa user=postgres password=secret host=localhost"
	◦	 Nota: Sostituisci secret e localhost con le tue credenziali reali.
	◦	Inizializza il database: python backend/database.py
	◦	

Passo 4: Configurare Firebase (Login con Google)
	1	Crea un Progetto Firebase:
	◦	Vai su Firebase Console, crea un nuovo progetto.
	◦	Abilita l’autenticazione e configura il provider “Google”.
	2	Aggiorna firebase.js:
	◦	Trova le credenziali nella sezione “Configurazione Web” del tuo progetto Firebase.
	◦	Modifica AI_RIQA/frontend/src/firebase.js: const firebaseConfig = {
	◦	  apiKey: "YOUR_API_KEY",
	◦	  authDomain: "YOUR_AUTH_DOMAIN",
	◦	  projectId: "YOUR_PROJECT_ID",
	◦	  storageBucket: "YOUR_STORAGE_BUCKET",
	◦	  messagingSenderId: "YOUR_MESSAGING_SENDER_ID",
	◦	  appId: "YOUR_APP_ID"
	◦	};
	◦	firebase.initializeApp(firebaseConfig);
	◦	export const auth = firebase.auth();
	◦	export const googleProvider = new firebase.auth.GoogleAuthProvider();
	◦	
	3	Aggiungi Firebase al Frontend:
	◦	Assicurati che index.html includa gli script Firebase (già presenti nel codice fornito).

Passo 5: Avviare il Server Backend
	1	Esegui il Server: python backend/app.py
	2	
	◦	Il server sarà disponibile su http://localhost:8000.
	3	Verifica:
	◦	Apri un browser e vai su http://localhost:8000/docs per vedere la documentazione API Swagger.
	◦	Testa un endpoint, ad esempio: curl -X POST "http://localhost:8000/chat" -H "Content-Type: application/json" -d '{"message": "x^2"}'
	◦	

Passo 6: Avviare l’Interfaccia Grafica
	1	Esegui il Frontend:
	◦	Torna nella directory frontend: cd frontend
	◦	
	◦	Avvia il server di sviluppo Vue.js: npm run serve
	◦	
	◦	Il frontend sarà disponibile su http://localhost:8080 (o una porta simile indicata nel terminale).
	2	Accesso Statico (Alternativa)**:
	◦	Se non vuoi usare npm run serve, il backend serve già i file statici. Vai direttamente a: http://localhost:8000/static/index.html
	◦	

Passo 7: Testare il Chatbot
	1	Login:
	◦	Clicca su “Login” nell’interfaccia e accedi con il tuo account Google.
	2	Inviare un Messaggio:
	◦	Digita “Risolvi x^2 - 4 = 0” nel campo di input e premi “Invia”.
	◦	Risultato atteso: una risposta con i risultati matematici.
	3	Caricare un File:
	◦	Usa il pulsante di caricamento per inviare un’immagine con un’equazione (es. JPG/PNG).
	◦	Il chatbot estrarrà il testo con OCR e risponderà.
	4	Visualizzare un Grafico:
	◦	Vai a http://localhost:8000/graph/math per scaricare un grafico PNG.
	5	Simulazione Remota:
	◦	Modifica client.py per testare: import requests
	◦	result = requests.post("http://localhost:8000/simulate", json={"sim_type": "quantum", "params": {"n_qubits": 2}}).json()
	◦	print(result)
	◦	
	6	Risultati Condivisi:
	◦	Vai a http://localhost:8000/shared_results per vedere i dati salvati nel database.

Passo 8: Configurazioni Avanzate (Opzionale)
	1	Deploy su Server Remoto:
	◦	Usa Docker: docker build -t ai_riqa .
	◦	docker run -p 8000:8000 ai_riqa
	◦	
	◦	Oppure carica su un VPS (es. DigitalOcean) e configura un IP pubblico.
	2	Google Drive:
	◦	Aggiungi l’integrazione con Google Drive API per salvare i risultati (richiede ulteriori configurazioni).
	3	Personalizzazione:
	◦	Modifica i colori in frontend/src/assets/style.css o aggiungi nuove simulazioni in core.py.

Risoluzione dei Problemi
	•	Errore “Modulo non trovato”:
	◦	Verifica che tutte le dipendenze siano installate (pip install -r requirements.txt).
	•	Server non si avvia:
	◦	Controlla che la porta 8000 non sia occupata (lsof -i :8000 su Linux/macOS).
	•	Frontend non carica:
	◦	Assicurati che npm run serve sia attivo o che i file in frontend/public siano corretti.
	•	Database non funziona:
	◦	Controlla le variabili d’ambiente per PostgreSQL o il percorso di riqa.db per SQLite.

Esempi di Utilizzo
	•	Matematica: “Risolvi x^2 - 4 = 0” → Risultati: soluzioni e grafico.
	•	Balistica: “v0=20, angolo=45°” → Traiettoria e dati.
	•	Quantistica: “Simula 2 qubit” → Probabilità di misurazione.
	•	Biologica: “Tasso 0.1” → Curva di crescita.
	•	Astrale: “Raggio 1 AU” → Orbita circolare.

Congratulazioni! Hai avviato con successo AI_RIQA. Per supporto o personalizzazioni, consulta il codice sorgente o contatta lo sviluppatore.

