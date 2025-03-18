# narco_tech

Got it! Let’s simplify the case to **two devices** (a laptop and a smartphone) with a focused storyline and realistic, non-technobabble evidence. Here’s the streamlined version:

---

### **Simplified Case Storyline: "The Accountant’s Mistake"**  
**Target:** **Luis Moreno**  
**Role:** Mid-level accountant for the **NarcoTech cartel**, posing as a freelance tax consultant.  

**Background:**  
Luis uses two devices to launder money for NarcoTech:  
1. **Windows 10 Laptop**: For creating fake invoices and communicating with cartel members.  
2. **Android Smartphone**: For encrypted chats, cryptocurrency transfers, and coordinating cash pickups.  

**Plot:**  
Luis made two critical mistakes:  
1. **Unencrypted Backup**: He saved a **passwords.txt** file on his laptop’s desktop with credentials for his crypto wallets.  
2. **Location Tagging**: His smartphone’s camera app geotagged photos of a warehouse used to store drug cash.  

---

### **Evidence to Simulate on Both Devices**  
#### **1. Windows Laptop Evidence**  
**a. Financial Records**  
- **What**:  
  - Fake invoices (Excel files) labeled **"Client_Payments_2023.xlsx"** with coded entries (e.g., "Project Alpha" = $50k cocaine shipment).  
  - PDFs of altered bank statements showing fake "consulting fees" from **"Delta Logistics LLC"** (a shell company).  
- **Where**:  
  - `C:\Users\Luis\Documents\Freelance\Invoices\`  
  - **Recycle Bin**: Recently deleted folder `\Old_Statements` with unedited bank PDFs.  
- **Why**: Proves money laundering through forged financial records.  

**b. Cryptocurrency Activity**  
- **What**:  
  - **Electrum Bitcoin Wallet** installed, with transaction history sending BTC to darknet market addresses.  
  - A **NotePad file** `crypto_notes.txt` listing wallet recovery phrases.  
- **Where**:  
  - Wallet files: `C:\Users\Luis\AppData\Roaming\Electrum\wallets\`  
  - `crypto_notes.txt` saved carelessly on the desktop.  
- **Why**: Links Luis to cartel payments via Bitcoin.  

**c. Communication**  
- **What**:  
  - **Telegram Desktop** chats with a contact named "Jefe" discussing "shipment delays."  
  - **ProtonMail** drafts (never sent) with coded messages like "Package delivered to Warehouse 12."  
- **Where**:  
  - Telegram logs: `C:\Users\Luis\AppData\Roaming\Telegram Desktop\`  
  - Browser history (Chrome) showing ProtonMail login activity.  
- **Why**: Shows coordination with cartel members.  

**d. Anti-Forensics Traces**  
- **What**:  
  - **VeraCrypt** installed, but Luis forgot to encrypt a folder named `\Freelance\Invoices`.  
  - **BleachBit** execution logs showing cleanup of `%Temp%` files weekly.  
- **Where**:  
  - VeraCrypt registry keys: `HKEY_CURRENT_USER\Software\VeraCrypt`  
  - Prefetch file: `BLEACHBIT.EXE-XXXXX.pf`  
- **Why**: Demonstrates intent to hide activities.  

---

#### **2. Android Smartphone Evidence**  
**a. Encrypted Chats**  
- **What**:  
  - **Signal** messages with a group named "Delivery Team" discussing "fuel costs" (code for bribe payments).  
  - **WhatsApp** voice notes from "Jefe" saying, "Clean the office tonight" (order to destroy evidence).  
- **Where**:  
  - Signal backups: `/sdcard/Signal/Backups/`  
  - WhatsApp media: `/sdcard/WhatsApp/Media/`  
- **Why**: Direct evidence of Luis’s role in cartel ops.  

**b. Cryptocurrency Transfers**  
- **What**:  
  - **Binance App** installed, with transaction history converting BTC to Monero (XMR).  
  - SMS confirmation codes for crypto exchanges.  
- **Where**:  
  - Binance cache: `/data/data/com.binance.app/`  
  - SMS database: `/data/data/com.android.providers.telephony/databases/mmssms.db`  
- **Why**: Shows efforts to anonymize funds via privacy coins.  

**c. Geolocation Evidence**  
- **What**:  
  - Google Maps timeline showing Luis visited a **remote warehouse** (GPS: 19.4326° N, 99.1332° W) weekly.  
  - Photos of the warehouse’s exterior (geotagged) in the Gallery app.  
- **Where**:  
  - Maps timeline data: `/data/data/com.google.android.apps.maps/`  
  - Photo metadata: `/sdcard/DCIM/Camera/IMG_20231015.jpg`  
- **Why**: Links Luis to a physical cartel stash house.  

**d. Suspicious Apps**  
- **What**:  
  - **VPN App** (NordVPN) used daily at 8:00 PM (during "cleaning" sessions).  
  - **Calculator Vault App** (secret photo vault) hiding images of cash-filled suitcases.  
- **Where**:  
  - Vault app data: `/data/data/com.photovault.hidden/`  
  - NordVPN logs: `/data/data/com.nordvpn.android/`  
- **Why**: Proactive hiding of incriminating media.  

---

### **Steps to Simulate the Forensic Images**  
#### **For the Laptop**:  
1. Create a **Windows 10 VM** with user activity (e.g., tax software, personal emails).  
2. Add fake invoices, bank PDFs, and crypto notes to the desktop/documents.  
3. Install Telegram and ProtonMail. Simulate chats and draft emails.  
4. Run BleachBit once to generate cleanup logs.  
5. Image the VM using **FTK Imager** (save as `.dd`).  

#### **For the Smartphone**:  
1. Use an **Android emulator** (e.g., Android Studio) or old Android phone.  
2. Install Signal, WhatsApp, Binance, NordVPN, and a photo vault app.  
3. Send test messages, take geotagged photos, and simulate crypto transactions.  
4. Perform a **physical image** of the device using **Magnet Acquire** or `adb pull`.  

---

### **Key Analysis Goals**  
1. **Laptop**:  
   - Recover deleted bank statements from the Recycle Bin.  
   - Extract Bitcoin wallet addresses from `crypto_notes.txt`.  
   - Correlate invoice edits with Telegram chat timestamps.  

2. **Smartphone**:  
   - Decrypt the photo vault app to recover images of cash.  
   - Map Luis’s location history to the warehouse’s coordinates.  
   - Trace Monero transactions from Binance to darknet markets.  

---

### **Conclusion**  
This simplified case focuses on **two devices** with **realistic evidence** (financial docs, encrypted chats, crypto activity, and geolocation). It avoids overcomplication but still provides enough depth for forensic analysis, including:  
- Anti-forensics (VeraCrypt, BleachBit).  
- Cross-device corroboration (warehouse visits + chats).  
- "Smoking gun" evidence (unencrypted crypto notes, geotagged photos).  

Perfect for a training exercise or a beginner-friendly forensic challenge! Let me know if you need help setting up the VM/emulator. 🔍
