import React, { createContext, useContext, useState, useCallback } from 'react';
import PropTypes from 'prop-types';
import { APP_CONSTANTS } from '../utils/constants';

const ComparisonContext = createContext();

// eslint-disable-next-line react-refresh/only-export-components
export const useComparison = () => {
    const context = useContext(ComparisonContext);
    if (!context) {
        throw new Error('useComparison must be used within a ComparisonProvider');
    }
    return context;
};

export const ComparisonProvider = ({ children }) => {
    const [selectedProducts, setSelectedProducts] = useState([]);
    const [isComparing, setIsComparing] = useState(false);

    const addToComparison = useCallback((product) => {
        setSelectedProducts((prev) => {
            if (prev.find((p) => p.product_id === product.product_id)) {
                return prev;
            }
            if (prev.length >= APP_CONSTANTS.MAX_COMPARISON_ITEMS) {
                // Could trigger a toast notification here
                console.warn(`Cannot compare more than ${APP_CONSTANTS.MAX_COMPARISON_ITEMS} items`);
                return prev;
            }
            return [...prev, product];
        });
    }, []);

    const removeFromComparison = useCallback((productId) => {
        setSelectedProducts((prev) => prev.filter((p) => p.product_id !== productId));
    }, []);

    const clearComparison = useCallback(() => {
        setSelectedProducts([]);
    }, []);

    const value = {
        selectedProducts,
        addToComparison,
        removeFromComparison,
        clearComparison,
        isComparing,
        setIsComparing,
    };

    return (
        <ComparisonContext.Provider value={value}>
            {children}
        </ComparisonContext.Provider>
    );
};

ComparisonProvider.propTypes = {
    children: PropTypes.node.isRequired,
};
