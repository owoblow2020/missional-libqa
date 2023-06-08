import React, { useState } from "react";
import Navigation from "../Navigation/Navigation";
import Home from "../pages/Home/Home";
import SearchConfig from "../pages/SearchConfig/SearchConfig";
import Loading from "../pages/Loading/Loading";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { isLoggedIn, login } from "../../services";

function App() {
  const [isAutheticated, setIsAutheticated] = useState(false);

  isLoggedIn()
    .then((loggedInState) => {
      if (loggedInState === true) {
        setIsAutheticated(loggedInState);
      } else {
        login();
      }
    })
    .catch(() => {
      login();
    });

  return isAutheticated ? (
    <Router>
      <div className="App">
        <Navigation />
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route
            exact
            path="/manage-search-config"
            component={SearchConfig}
          ></Route>
        </Switch>
      </div>
    </Router>
  ) : (
    <Loading />
  );
}

export default App;
