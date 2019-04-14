'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
  NODE_ENV: '"development"',
  API_URL_PREFIX: '"http://localhost:8000"',
  STATIC_URL_PREFIX: '"http://localhost:8000/static"'
})
