// frontend/src/firebase.js
import firebase from 'firebase/app';
import 'firebase/auth';

const devConfig = {
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY || "AIzaSyASWWmeByDWyd-qC6aPF9f2MX6HY6wq0i4",
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN || "ai-riqa.firebaseapp.com",
  projectId: "ai-riqa-dev",  // Suffisso -dev per ambiente sviluppo
  storageBucket: "ai-riqa-dev.appspot.com",
  messagingSenderId: "1057289763194",
  appId: "1:1057289763194:web:bb48ac936910e25a01bec3"
};

const prodConfig = {
  // Config separata per produzione (da inserire in futuro)
};

const config = process.env.NODE_ENV === 'production' ? prodConfig : devConfig;

// Inizializzazione con controllo errori
try {
  if (!firebase.apps.length) {
    firebase.initializeApp(config);
    console.log("Firebase initialized in", process.env.NODE_ENV, "mode");
  }
} catch (error) {
  console.error("Firebase initialization error:", error);
}

// Export con protezione
export const auth = firebase.apps[0]?.auth() || null;
export const googleProvider = auth ? new firebase.auth.GoogleAuthProvider() : null;

// Controllo sicurezza per sviluppo
if (process.env.NODE_ENV === 'development') {
  auth?.useEmulator("http://localhost:9099");  // Per testing locale
}
