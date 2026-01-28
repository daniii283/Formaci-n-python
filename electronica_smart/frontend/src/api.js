import axios from "axios";

const api = axios.create({
  baseURL: "https://silver-carnival-7vj46rp6g49hpw99-8000.app.github.dev/", // ⚠️ CAMBIA esto si estás en Codespaces o usas una URL externa
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;
