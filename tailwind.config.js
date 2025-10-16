/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.{html,js}", // Project-level templates
    "./Shoe/templates/**/*.{html,js}", // App-level templates
    "./**/templates/**/*.{html,js}", // All app-level templates (recursive)
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};