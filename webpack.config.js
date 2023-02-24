const path = require('path')

module.exports = {
    entry: './frontend/src/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, 'exercises', 'static')
    },
    module: {
        rules: [
            {
              test: /\.jsx?$/, // compilation to es6
              exclude: /node_modules/,
              use: {
                loader: 'babel-loader',
                options: {
                  presets: ['react', 'es2015', 'es2016', 'stage-0'],
                  plugins: ['syntax-dynamic-import'],
                },
              },
            },
      ]
    }
}