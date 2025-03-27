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
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY || "AIzaSyASWWmeByDWyd-qC6aPF9f2MX6HY6wq0i4",
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN || "ai-riqa.firebaseapp.com",
  projectId: "ai-riqa-dev",
  storageBucket: "ai-riqa-dev.appspot.com",
  messagingSenderId: "1057289763194",
  appId: "1:1057289763194:web:bb48ac936910e25a01bec3"
};

const prodConfig = {
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY,
  authDomain: "ai-riqa.web.app",
  projectId: "ai-riqa",
  storageBucket: "ai-riqa.appspot.com",
  messagingSenderId: "1057289763194",
  appId: "1:1057289763194:web:bb48ac936910e25a01bec3"
};

const config = process.env.NODE_ENV === 'production' ? prodConfig : devConfig;

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
  googleProvider,
  // Esporta altri servizi quando servono:
  // storage, functions, analytics, etc.
};
