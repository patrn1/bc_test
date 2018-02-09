const path = require("path");
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');

module.exports = env => {
    return [
        {
            name: "risks",
            entry: "./risks/resources/js/app",
            output: {
                path: path.join(__dirname, "risks/static/risks/js"),
                filename: "app.js",
                publicPath : "/static/risks/js/"
            },
            module : {
                rules : [
                    {
                        test: /\.vue$/,
                        loader: 'vue-loader'
                    }
                ]
            },
            plugins: env && env.dev ? [] : [
                new UglifyJsPlugin({
                    uglifyOptions: {
                        ecma: 6
                    },
                    test: /\.js($|\?)/i,
                    cache: true,
                    parallel: true
                })
            ]
        }
    ];
}