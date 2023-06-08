const settings = {
  baseApiUri:
    process.env.REACT_APP_BASE_API_URI || "http://localhost:10000/api",
  loginRedirectUri:
    process.env.REACT_APP_LOGIN_REDIRECT_URI ||
    "http://localhost:10000/api/session/login",
};

export default settings;
