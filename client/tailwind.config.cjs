/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "rgb(139 92 246)",
      },
    },
  },
  plugins: [require("@headlessui/tailwindcss")],
};
