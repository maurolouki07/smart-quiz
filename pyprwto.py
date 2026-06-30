import streamlit as st

st.title("ΚΑΛΩΣ ΗΡΘΕΣ ΣΤΟ ΤΕΣΤ ΕΡΓΑΣΙΑΚΗΣ ΠΡΟΣΩΠΙΚΟΤΗΤΑΣ 10 ΕΡΩΤΗΣΕΩΝ")

# Αρχικοποίηση της μνήμης του Streamlit για το βήμα και τις απαντήσεις
if "step" not in st.session_state:
    st.session_state.step = 1
if "apantiseis" not in st.session_state:
    st.session_state.apantiseis = {}

# --- ΕΡΩΤΗΣΗ 1 ---
if st.session_state.step == 1:
    erwthsh1 = st.radio("1. Σου αρέσει να δουλεύεις με αριθμούς ή σε πιο θεωρητικό επίπεδο;", ["προτιμώ να δουλεύω με αριθμούς", "προτιμώ τη θεωρία"], key="q1")
    if st.button("Επόμενο", key="btn1"):
        st.session_state.apantiseis["erwthsh1"] = erwthsh1
        st.session_state.step = 2
        st.rerun()

# --- ΕΡΩΤΗΣΗ 2 ---
elif st.session_state.step == 2:
    erwthsh2 = st.radio("2. Πώς προτιμάς να δουλεύεις;", ["Μόνος", "Ομαδικά"], key="q2")
    if st.button("Επόμενο", key="btn2"):
        st.session_state.apantiseis["erwthsh2"] = erwthsh2
        st.session_state.step = 3
        st.rerun()

# --- ΕΡΩΤΗΣΗ 3 ---
elif st.session_state.step == 3:
    erwthsh3 = st.radio("3. Έχεις υπομονή με τα δύσκολα προβλήματα;", ["Ναι", "Όχι"], key="q3")
    if st.button("Επόμενο", key="btn3"):
        st.session_state.apantiseis["erwthsh3"] = erwthsh3
        st.session_state.step = 4
        st.rerun()

# --- ΕΡΩΤΗΣΗ 4 ---
elif st.session_state.step == 4:
    erwthsh4 = st.radio("4. Σου αρέσει να αναλύεις πολύπλοκα οικονομικά δεδομένα;", ["Ναι", "Όχι"], key="q4")
    if st.button("Επόμενο", key="btn4"):
        st.session_state.apantiseis["erwthsh4"] = erwthsh4
        st.session_state.step = 5
        st.rerun()

# --- ΕΡΩΤΗΣΗ 5 ---
elif st.session_state.step == 5:
    erwthsh5 = st.radio("5. Ενδιαφέρεσαι να λύνεις προβλήματα συμπεριφοράς στο εργασιακό σου περιβάλλον;", ["Ναι", "Όχι"], key="q5")
    if st.button("Επόμενο", key="btn5"):
        st.session_state.apantiseis["erwthsh5"] = erwthsh5
        st.session_state.step = 6
        st.rerun()

# --- ΕΡΩΤΗΣΗ 6 ---
elif st.session_state.step == 6:
    erwthsh6 = st.radio("6. Θεωρείς ότι η ψυχολογία σχετίζεται με την αποδοτικότητα;", ["Ναι", "Όχι"], key="q6")
    if st.button("Επόμενο", key="btn6"):
        st.session_state.apantiseis["erwthsh6"] = erwthsh6
        st.session_state.step = 7
        st.rerun()

# --- ΕΡΩΤΗΣΗ 7 ---
elif st.session_state.step == 7:
    erwthsh7 = st.radio("7. Σε ενδιαφέρουν τα υλικά κατασκευής και υποστήριξης;", ["Ναι", "Όχι"], key="q7")
    if st.button("Επόμενο", key="btn7"):
        st.session_state.apantiseis["erwthsh7"] = erwthsh7
        st.session_state.step = 8
        st.rerun()

# --- ΕΡΩΤΗΣΗ 8 ---
elif st.session_state.step == 8:
    erwthsh8 = st.radio("8. Θεωρείς την κοινωνική προσφορά πιο σημαντική από την προσωπική ανάπτυξη;", ["Ναι", "Όχι"], key="q8")
    if st.button("Επόμενο", key="btn8"):
        st.session_state.apantiseis["erwthsh8"] = erwthsh8
        st.session_state.step = 9
        st.rerun()

# --- ΕΡΩΤΗΣΗ 9 ---
elif st.session_state.step == 9:
    erwthsh9 = st.radio("9. Η βιολογία και οι ζωντανοί οργανισμοί πάντα σου κινούσαν το ενδιαφέρον;", ["Ναι", "Όχι"], key="q9")
    if st.button("Επόμενο", key="btn9"):
        st.session_state.apantiseis["erwthsh9"] = erwthsh9
        st.session_state.step = 10
        st.rerun()

# --- ΕΡΩΤΗΣΗ 10 ---
elif st.session_state.step == 10:
    erwthsh10 = st.radio("10. Θεωρείς ότι υπάρχουν εργασίες που πρέπει να αμείβονται καλύτερα από άλλες;", ["Ναι", "Όχι"], key="q10")
    if st.button("Δες το αποτέλεσμα", key="btn10"):
        st.session_state.apantiseis["erwthsh10"] = erwthsh10
        st.session_state.step = 11
        st.rerun()

# --- ΑΠΟΤΕΛΕΣΜΑΤΑ ---
elif st.session_state.step == 11:
    st.write("--- ΥΠΟΛΟΓΙΣΜΟΣ ΑΠΟΤΕΛΕΣΜΑΤΟΣ ---")
    
    # Παίρνουμε τις απαντήσεις από τη μνήμη για να κάνουμε τον έλεγχο
    ans1 = st.session_state.apantiseis["erwthsh1"]
    ans3 = st.session_state.apantiseis["erwthsh3"]
    
    if ans1 == "προτιμώ να δουλεύω με αριθμούς" and ans3 == "Ναι":
        st.success("ΣΥΓΧΑΡΙΤΗΡΙΑ! ΕΙΣΑΙ ΜΑΛΑΚΑΣ!!! by lefte")
    else:
        st.info("ΣΥΓΧΑΡΙΤΗΡΙΑ ΕΙΣΑΙ ΜΕΓΑΛΟΣ ΜΑΛΑΚΑΣ!!! by lefte")
        
    # Κουμπί για επανεκκίνηση του τεστ
    if st.button("Κάνε πάλι το τεστ", key="reset"):
        st.session_state.step = 1
        st.session_state.apantiseis = {}
        st.rerun()
