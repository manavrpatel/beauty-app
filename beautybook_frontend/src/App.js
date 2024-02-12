import React, { useEffect } from 'react';
import { Routes, Route} from 'react-router-dom';

import {Login, Signin} from './components';
import Home from './containers/Home';

const App = () => {

    return (
      
        <Routes>
            <Route path="login" element={<Login />} />
            <Route path="/" element={<Home />} />
            <Route path="/signin" element={<Signin />} />
        </Routes>
    );
  };
  
  export default App;