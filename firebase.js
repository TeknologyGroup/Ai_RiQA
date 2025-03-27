// frontend/src/firebase.js
import { initializeApp, getApps } from 'firebase/app';
import { 
  getAuth, 
  connectAuthEmulator, 
  GoogleAuthProvider 
} from 'firebase/auth';
import { 
  getFirestore, 
  connectFirestoreEmulator 
} from 'firebase/firestore';

const devConfig = {
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY,
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN,
  projectId: "ai-riqa-dev",
  storageBucket: "ai-riqa-dev.appspot.com",
  messagingSenderId: process.env.VUE_APP_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.VUE_APP_FIREBASE_APP_ID
};

const prodConfig = {
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY,
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN,
  project'sId: "ai-riqa",
  storageBucket: "ai-riqa.appspot.com",
  messagingSenderId: process.env.VUE_APP_FIREBASE_MESSAGING_SENDER_ID,
  appId: process.env.VUE_APP_FIREBASE_APP_ID
};

const config = process.env.NODE_ENV === 'production' ? prodConfig : devConfig;

// Verifica che le variabili siano definite
if (!config.apiKey || !config.authDomain || !config.appId) {
  throw new Error("Firebase configuration is incomplete. Check your environment variables.");
}

// Inizializzazione servizi
let auth = null;
let db = null;
let googleProvider = null;

const initFirebase = () => {
  try {
    if (getApps().length === 0) {
      const app = initializeApp(config);
      
      // Auth
      auth = getAuth(app);
      googleProvider = new GoogleAuthProvider();
      
      // Firestore
      db = getFirestore(app);
      
      if (process.env.NODE_ENV === 'development') {
        // Emulatori
        connectAuthEmulator(auth, "http://localhost:9099");
        connectFirestoreEmulator(db, 'localhost', 8080);
        console.log("Firebase emulators initialized");
      }
      
      console.log("Firebase initialized in", process.env.NODE_ENV, "mode");
    }
  } catch (error) {
    console.error("Firebase initialization error:", error);
  }
};

initFirebase();

export { 
  auth, 
  db, 
  googleProvider
};
