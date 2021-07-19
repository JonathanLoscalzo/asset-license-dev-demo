import axios from "axios";

function authHeaders() {
  if (localStorage.getItem("JWT_AUTH") != null) {
    return {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("JWT_AUTH")}`,
      },
    };
  } else {
    return {};
  }
}

const AcmeApi = () => {
  const instance = axios.create({
    baseURL: process.env.REACT_APP_ACME_BACKEND,
    // timeout: 1000,
    ...authHeaders(),
    // headers: { 'Authorization': `Bearer ${localStorage.getItem("JWT_AUTH")}` },
    withCredentials: true
  });

  return instance;
}

export const api = {
  async login(username: string, password: string) {
    const params = new URLSearchParams();
    params.append("username", username);
    params.append("password", password);
    await AcmeApi()
      .post("/auth/token", params)
      .then((resp) => {
        localStorage.setItem("JWT_AUTH", resp.data.access_token);
        window.location.reload(false);
      });
  },
  async logout() {
    localStorage.removeItem("JWT_AUTH")
  },
  async getLicenses() {
    return AcmeApi().get("/api/v1/licenses").then(resp => resp.data)
  },
  async getAssets() {
    return AcmeApi().get("/api/v1/resources").then(resp => resp.data)
  },
  async getDevelopers() {
    return AcmeApi().get("/api/v1/developers").then(resp => resp.data)
  },
  async createDeveloper(formData: { fullname: string, active: boolean }) {
    return AcmeApi().post("/api/v1/developers", formData).then(resp => resp.data)
  }
};
