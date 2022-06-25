import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Home from 'Home';

function App() {
  return (
    <div className="App">
       <Router>
          <div>
            <Route exact path='/' component={Home}/>
          </div>
        </Router>
    </div>
  );
}

export default App;
