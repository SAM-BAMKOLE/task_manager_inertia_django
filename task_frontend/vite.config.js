import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import tailwindcss from "@tailwindcss/vite";
import { resolve } from "path";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), tailwindcss()],
  root: "./",
  // base:
  //   process.env.NODE_ENV === "production"
  //     ? "/static/dist/"
  //     : "http://localhost:5173/",
  server: {
    host: "localhost",
    origin: "http://localhost:5173",
    port: 5173,
    strictPort: true,
  },
  resolve: {
    extensions: [".js", ".json"],
  },
  build: {
    outDir: "../static",
    emptyOutDir: true,
    manifest: "manifest.json",
    target: "es2015",
    rollupOptions: {
      input: "./src/entry-client.js",
    },
  },
  base: "/static/",
});
