import io from 'socket.io-client'

const socket = io(process.env.VUE_APP_WS_URL)

export const connectSocket = () => {
  socket.connect()
}

export const disconnectSocket = () => {
  socket.disconnect()
}

export const subscribeToSimulation = (callback) => {
  socket.on('simulation_update', data => {
    callback(null, data)
  })
}

export const unsubscribeFromSimulation = () => {
  socket.off('simulation_update')
}
