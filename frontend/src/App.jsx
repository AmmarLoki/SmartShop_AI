import React from 'react';
import { RouterProvider } from 'react-router-dom';
import router from './router';
import './styles/global.css';

import { SearchProvider } from './store/SearchContext';
import { ComparisonProvider } from './store/ComparisonContext';

function App() {
  return (
    <SearchProvider>
      <ComparisonProvider>
        <RouterProvider router={router} />
      </ComparisonProvider>
    </SearchProvider>
  );
}

export default App;
