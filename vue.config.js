// vue.config.js
module.exports = {
  // Configurazioni di base
  publicPath: '/',
  outputDir: 'dist',
  assetsDir: 'assets',
  lintOnSave: false,
  productionSourceMap: false,

  // Configurazione del server di sviluppo
  devServer: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:5000', // URL del tuo backend
        changeOrigin: true,
        pathRewrite: { '^/api': '' },
      },
    },
  },
};
