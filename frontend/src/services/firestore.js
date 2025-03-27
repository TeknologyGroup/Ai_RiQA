import { db } from '../firebase'
import { collection, addDoc, query, where, getDocs } from 'firebase/firestore'

export const saveSimulation = async (simulationData, userId) => {
  try {
    const docRef = await addDoc(collection(db, 'simulations'), {
      ...simulationData,
      userId,
      createdAt: new Date()
    })
    return docRef.id
  } catch (e) {
    console.error("Error adding document: ", e)
    throw e
  }
}

export const getUserSimulations = async (userId) => {
  const q = query(
    collection(db, 'simulations'),
    where('userId', '==', userId)
  )
  const querySnapshot = await getDocs(q)
  return querySnapshot.docs.map(doc => ({ id: doc.id, ...doc.data() }))
}
