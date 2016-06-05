module.exports = {
  entry: [
    './app/app.js'
  ],
  output: {
    path: __dirname + '/media/app',
    filename: "bundle.js"
  },
  module: {
    loaders: [
      {
        test: /\.(js|jsx)$/,
        loader: 'babel-loader',
        query: {
          presets: ['react', 'es2015']
        }
      }
    ]
  }
};
