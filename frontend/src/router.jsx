import React from 'react';
import { createBrowserRouter } from 'react-router-dom';
import MainLayout from './layout/MainLayout';
import HomePage from './pages/HomePage';
import SearchResultsPage from './pages/SearchResultsPage';
import ComparisonPage from './pages/ComparisonPage';
import NotFoundPage from './pages/NotFoundPage';
import ErrorBoundary from './components/ErrorBoundary';

const router = createBrowserRouter([
    {
        path: '/',
        element: <ErrorBoundary><MainLayout /></ErrorBoundary>,
        errorElement: <NotFoundPage />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
            {
                path: 'search',
                element: <SearchResultsPage />,
            },
            {
                path: 'compare',
                element: <ComparisonPage />,
            },
            {
                path: '*',
                element: <NotFoundPage />,
            },
        ],
    },
]);

export default router;
