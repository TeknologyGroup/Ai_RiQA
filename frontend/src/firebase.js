// frontend/src/firebase.js
import { initializeApp, getApps } from 'firebase/app';
import { getAuth, connectAuthEmulator, GoogleAuthProvider } from 'firebase/auth';

const devConfig = {
  apiKey: process.env.VUE_APP_FIREBASE_API_KEY || "AIzaSyASWWmeByDWyd-qC6aPF9f2MX6HY6wq0i4",
  authDomain: process.env.VUE_APP_FIREBASE_AUTH_DOMAIN || "ai-riqa.firebaseapp.com",
  projectId: "ai-riqa-dev",
  storageBucket: "ai-riqa-dev.appspot.com",
  messagingSenderId: "1057289763194",
  appId: "1:1057289763194:web:bb48ac936910e25a01bec3"
};

const prodConfig = {
  // Config separata per produzione (da inserire in futuro)
};

const config = process.env.NODE_ENV === 'production' ? prodConfig : devConfig;

// Inizializzazione con controllo errori
let auth = null;
let googleProvider = null;

try {
  if (getApps().length === 0) {
    const app = initializeApp(config);
    console.log("Firebase initialized in", process.env.NODE_ENV, "mode");
    auth = getAuth(app);
    googleProvider = new GoogleAuthProvider();
    
    if (process.env.NODE_ENV === 'development') {
      connectAuthEmulator(auth, "http://localhost:9099");
    }
  }
} catch (error) {
  console.error("Firebase initialization error:", error);
}

export { auth, googleProvider };
