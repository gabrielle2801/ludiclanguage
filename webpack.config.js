const path = require('path')

module.exports = {
    entry: './frontend/src/index.js',
    output: {
        filename: 'game.js',
        path: path.resolve(__dirname, 'exercises', 'static')
    },
    module: {
      rules: [
        {
        test: /\.js|.jsx$/,
        exclude: /node_modules/,
        use: "babel-loader",
        },
        {
          test: /\.css$/,
        exclude: /node_modules/,
        use: ["style-loader", "css-loader"],
        }
      ]
    }
}