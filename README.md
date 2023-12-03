# Challenge for Multiversx

# Cerinta challenge
    Using python, the provided python sdk libraries (see below), and the above MultiversX transaction execution engine specifications/constraints, try to write some scenarios that interact with the devnet (or testnet) and verify (or not) the expectations for successfully executed transactions (e.g. eGLD transfer from one account to another - success or failed, smart contract call - success or failed etc.)
    The result of the test suite should generate a report with transaction execution statistics (e.g. total number of transactions, number of transactions     successful, number of transactions failed, etc). 

# Pasi preliminari:
  - Instalare VM folosind Linux
  - Instalare tool-uri necesare realizarii proiectului (PyCharm, Postman)
  - Creare wallet pe Testnet
  - Request Faucet din Wallet si realizarea unui numar de tranzactii direct de pe site
  - Interogarea tranzactiilor realizate folosing proxy in Postman
  - Instalarea packetelor multiversx in terminal
# Realizarea proiectului in PyCharm:
  - Parcurgerea documentatiei (Cookbook) si familiarizarea cu functiile din cadrul pachetelor multiverx
  - Creearea mai multor fisiere pentru a decentraliza codul:
         * config.py = contine adrese, path-uri si parole stocate in variabile pentru o utilizare mai usoara in cod
         * Librarii.py = contine toate librariile utilizate in cod pentru a reduce liniile utilizate in restul fisierelor .py
         * Actions.py
         * Transactions.py
         * raport.txt
         * requirements.txt
         * main.py

  1) **config.py**
          Acest fisier contine adrese, path-uri si parole stocate ca si variabile globale pentru a putea fi utilizate cu mai multa usurinta in cod
  2) **Librarii.py**
          Fisierul contine toate librariile utilizate in cod pentru a reduce numarul de linii utilizate in restul fisierelor .py
  3) **Actions.py**
          Utilizat pentru a definii principalele functii cu rol de actiune in cod, acestea fiind:
              * delay(n) = functie utilizata pentru a seta delay-uri in parcurgerea codului cu un numar de secunde dat de utilizator, avand rolul de a oferi timp platformei sa proceseze si sa afiseze tranzactiile in sectiunea Transactions                               inainte de a le interoga (pentru a evita afisarea mesajului pending)
              * semnare(t, signer, transC) = functie cu rol de semnare a tranzactiilor propuse in cod
              * output(t,proxy,hashes, number) = functie care extrage hash-urile aferente tranzactiilor (t) din lista de hash-uri (hashes) care au fost trimise spre broadcast, folosite pentru a le putea afisa in consola cu rol de debugg (cu                                                   un delay de 1 secunda la final in cazul in care folosim aceasta functie de mai multe ori consecutiv)
              * report_file(transaction,hashes,number,proxy) = aceasta functie are un rol similar cu functia "output", doar ca in loc sa afiseze datele in consola, le scrie intr-un fisier .txt localizat intr-o locatie specifica
  4) **Transactions.py**
          In acest fisier am propus mai multe functii, fiecare dintre aceste functii are rol de intocmire a unui tip de tranzactie spre a fi trimise catre blockchain:
              * transaction_true(account) = propune o tranzactie EGLD care va avea status "success"
              * transaction_false_amount(account) = propune o tranzactie EGLD care va avea status "failed"
              * transaction2_true(account) = un al doilea exemplu de tranzactie EGLD cu status "success"
              * transaction_EGDT_true() = aceasta functie realizeaza o tranzactie EGDT care va fi "success"
              * transaction_EGDT_false() = aceasta functie realizeaza o tranzactie EGDT care va fi "failed"
              * transaction_smart_contract() = functia realizeaza o tranzactie care invoca un smart contract
  5) **raport.txt**
         Fisierul respectiv contine raportul propriu zis in care se pot observa statusurile tranzactiilor trimise catre blockchain
  6) **requirements.txt** = contine pachetele multiversx instalate in proiectul PyCharm utilizat
  7) **main.py**
         In fisierul main am m-am folosit de toate functiile si informatiile declarate in fisierele prezentate mai sunt in scopul crearii mai multor tipuri de tranzactii, semnarea lor, trimierea lor catre blockchain si interogarea acestora          pentru a putea realiza raportul cu istoricul tranzactiilor si statusul acestora

  # Probleme si dificultati
      Problema principala in acest proiect este trimiterea smart contractului catre blockchain, acesta va fi perceptul mereu ca fiind un "fail" (banuiala mea este ca nu poate avea statusul "success" deoarece nu am reusit sa imi generez un        fisier .wasm)

