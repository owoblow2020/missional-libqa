import React from "react";
import "./Loading.scss";

class Loading extends React.Component {
  render() {
    return (
      <div className="loading">
        <h1>Loading...</h1>
        <small>please wait...</small>
      </div>
    );
  }
}

export default Loading;
