Ecco il contenuto per il tuo file `DATABASE_SETUP.md` che puoi includere nel progetto:

```markdown
# Configurazione del Database AI_RIQA

AI_RIQA supporta sia **SQLite** (default) che **PostgreSQL**. Questa guida spiega come configurare entrambi.

## 1. SQLite (Configurazione Predefinita)

### Setup Automatico
```bash
python3 backend/database.py
```
Verrà creato automaticamente il file `riqa.db` nella directory principale.

## 2. PostgreSQL (Configurazione Avanzata)

### Prerequisiti
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

### Configurazione Database

1. **Crea database e utente**:
   ```bash
   sudo -u postgres psql -c "CREATE DATABASE riqa;"
   sudo -u postgres psql -c "CREATE USER riqa_admin WITH PASSWORD 'Martynb85.';"
   sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE riqa TO riqa_admin;"
   ```

2. **Verifica la configurazione**:
   ```bash
   sudo -u postgres psql -c "\l"          # Lista database
   sudo -u postgres psql -c "\du"         # Lista utenti
   ```

### Configurazione AI_RIQA

Imposta le variabili d'ambiente:
```bash
export DATABASE_TYPE="postgresql"
export DATABASE_URL="dbname=riqa user=riqa_admin password=Martynb85. host=localhost"
```

Inizializza il database:
```bash
python3 backend/database.py
```

## 3. Test della Connessione

### Per PostgreSQL:
```bash
psql -h localhost -U riqa_admin -d riqa -W
```

### Comandi utili PostgreSQL:
```sql
\dt                         -- Lista tabelle
\d+ nome_tabella            -- Struttura tabella
\q                          -- Esci
```

## 4. Switching tra Database

Per tornare a SQLite:
```bash
unset DATABASE_TYPE DATABASE_URL
```

## Troubleshooting

### Errori di connessione PostgreSQL:
1. Verifica il servizio:
   ```bash
   sudo systemctl status postgresql
   ```

2. Controlla i log:
   ```bash
   sudo tail -n 50 /var/log/postgresql/postgresql-*.log
   ```

3. Modifica i permessi in:
   ```bash
   sudo nano /etc/postgresql/*/main/pg_hba.conf
   ```
   Aggiungi:
   ```
   host    riqa    riqa_admin    127.0.0.1/32    md5
   ```

## Note sulla Sicurezza
- Per ambienti di produzione, usa sempre password complesse
- Limita i privilegi degli utenti al minimo necessario
- Considera l'uso di connessioni SSL per PostgreSQL

```

Puoi personalizzare ulteriormente il file con:
- Istruzioni specifiche per il tuo ambiente
- Requisiti aggiuntivi del tuo progetto
- Esempi di configurazione per diversi ambienti (dev/test/prod)
