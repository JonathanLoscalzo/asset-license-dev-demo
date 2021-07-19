import React, { useEffect } from "react";
import logo from "./logo.svg";
import "./App.css";
import { AuthPage } from "./modules/auth";

import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useHistory,
} from "react-router-dom";
import Developers from "./modules/developers/index";
import Assets from "./modules/assets/index";
import Licenses from "./modules/licenses/index";
import { api } from "./utils/api";
import { Container, Row, Col } from "reactstrap";
const Private = (props: any) => {
  if (localStorage.getItem("JWT_AUTH")) {
    return props.children;
  }
  return <AuthPage />;
};

function App() {
  return (
    <Container>
      <Private>
        <div className="App">
          <header className="App-header"></header>
          <Router>
            <div>
              <Row>
                <ul>
                  <li>
                    <Link to="/">Home</Link>
                  </li>
                  <li>
                    <Link to="/developers">Developers</Link>
                  </li>
                  <li>
                    <Link to="/assets">Assets</Link>
                  </li>
                  <li>
                    <Link to="/licenses">Licenses</Link>
                  </li>
                  <li>
                    <Link to="/logout">Logout</Link>
                  </li>
                </ul>
              </Row>
              <hr />
              <Row>
                <Switch>
                  <Route exact path="/">
                    <>{"HOME"}</>
                  </Route>
                  <Route path="/developers">
                    <Developers />
                  </Route>
                  <Route path="/assets">
                    <Assets />
                  </Route>

                  <Route path="/licenses">
                    <Licenses />
                  </Route>

                  <Route path="/logout">
                    <Logout />
                  </Route>
                </Switch>
              </Row>
            </div>
          </Router>
        </div>
      </Private>
    </Container>
  );
}

const Logout = () => {
  let history = useHistory();
  useEffect(() => {
    const f = async () => {
      await api.logout();
      history.push("/");
      window.location.reload(false);
    };
    f();
  });

  return <></>;
};

export default App;
