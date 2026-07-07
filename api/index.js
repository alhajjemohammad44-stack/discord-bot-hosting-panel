const express = require('express');
const app = express();

app.get('*', (req, res) => {
  res.json({
    status: 'ok',
    message: 'Discord Bot Hosting Panel - Vercel Node.js',
    path: req.path,
    time: new Date().toISOString()
  });
});

module.exports = app;
