import React from "react";
import HomeScreen from "./screens/HomeScreen/HomeScreen";
import About from "./screens/HomeScreen/about/About";
import Header from "./components/Header/Header";
import WavLibrary from "./screens/wavlibrary/WavLibrary";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

const App = () => {
  return (
    <Router>
      <Header />
      <Switch>
        <Route exact path="/">
          <HomeScreen />
        </Route>
        <Route path="/about">
          <About />
        </Route>
        <Route path="/wavlibrary">
          <WavLibrary />
        </Route>
      </Switch>
    </Router>
  );
};

export default App;
