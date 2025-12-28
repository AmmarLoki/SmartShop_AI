export const ENDPOINTS = {
    SEARCH: '/search',
    COMPARE: '/compare',
    RECOMMENDATIONS: (productId) => `/products/${productId}/recommendations`,
    HEALTH: '/health',
};
