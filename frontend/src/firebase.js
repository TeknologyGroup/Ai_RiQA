// AI_RIQA/frontend/src/firebase.js
import firebase from 'firebase/app';
import 'firebase/auth';

const firebaseConfig = {
  apiKey: "AIzaSyASWWmeByDWyd-qC6aPF9f2MX6HY6wq0i4",
  authDomain: "ai-riqa.firebaseapp.com",
  projectId: "ai-riqa",
  storageBucket: "ai-riqa.firebasestorage.app",
  messagingSenderId: "1057289763194",
  appId: "1:1057289763194:web:bb48ac936910e25a01bec3",
  measurementId: "G-8NPXZF37GJ"
};

// Inizializza Firebase
firebase.initializeApp(firebaseConfig);

export const auth = firebase.auth();
export const googleProvider = new firebase.auth.GoogleAuthProvider();
