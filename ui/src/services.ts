import axios from "axios";

import settings from "./settings";

axios.defaults.baseURL = settings.baseApiUri;
axios.defaults.headers.common["x-requested-with"] = "XMLHttpRequest";

function getAxiosInstance() {
  const HTTP = axios.create({
    withCredentials: true,
  });

  HTTP.interceptors.response.use(
    function handle2xx(response) {
      return response;
    },
    function handleError(error) {
      // Handle session refresh redirects
      if (
        error.response &&
        error.response.status === 403 &&
        error.response.data &&
        error.response.data.refresh_url
      ) {
        window.location.assign(error.response.data.refresh_url);
      }

      return Promise.reject(error);
    }
  );
  return HTTP;
}

export async function isLoggedIn(): Promise<boolean> {
  /* Get the user's login state from the API */
  const result = await getAxiosInstance().get("/session/is_loggedin");

  if (result.status === 200) {
    return true;
  } else if (result.status === 403) {
    return false;
  } else {
    throw new Error(`Unexpected status code ${result.status} encountered.`);
  }
}

export function login() {
  /* Redirect to the login uri to start the auth flow */
  window.location.assign(settings.loginRedirectUri);
}

export async function logout() {
  /* Call the API to log the user out */
  await getAxiosInstance().post("/session/logout");
}
