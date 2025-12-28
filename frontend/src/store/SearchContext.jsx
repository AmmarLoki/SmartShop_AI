import React, { createContext, useContext, useState, useCallback } from 'react';
import PropTypes from 'prop-types';

const SearchContext = createContext();

// eslint-disable-next-line react-refresh/only-export-components
export const useSearch = () => {
    const context = useContext(SearchContext);
    if (!context) {
        throw new Error('useSearch must be used within a SearchProvider');
    }
    return context;
};

export const SearchProvider = ({ children }) => {
    const [query, setQuery] = useState('');
    const [results, setResults] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);
    const [filters, setFilters] = useState({});

    const clearResults = useCallback(() => {
        setResults([]);
        setError(null);
    }, []);

    const value = {
        query,
        setQuery,
        results,
        setResults,
        isLoading,
        setIsLoading,
        error,
        setError,
        filters,
        setFilters,
        clearResults,
    };

    return (
        <SearchContext.Provider value={value}>
            {children}
        </SearchContext.Provider>
    );
};

SearchProvider.propTypes = {
    children: PropTypes.node.isRequired,
};
