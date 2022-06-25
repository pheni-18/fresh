import React from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { ArticleListPage } from 'pages/article/ArticleListPage';

function App() {
  return (
    <div className="App">
       <Router>
          <div>
            <Route exact path='/' component={ArticleListPage}/>
          </div>
        </Router>
    </div>
  );
}

export default App;
