module.exports = {
  publicPath: '/',
  outputDir: 'dist',
  indexPath: 'index.html',
  filenameHashing: true,
  productionSourceMap: false,
  configureWebpack: {
    performance: {
      hints: false
    }
  }
}
