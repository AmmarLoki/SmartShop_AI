import client from './client';
import { ENDPOINTS } from './endpoints';

export const searchProducts = async ({ query, limit = 10 }) => {
    const response = await client.post(ENDPOINTS.SEARCH, { query, limit });
    return response.data;
};

export const compareProducts = async (productIds) => {
    const response = await client.post(ENDPOINTS.COMPARE, { product_ids: productIds });
    return response.data;
};

export const getRecommendations = async (productId) => {
    const response = await client.get(ENDPOINTS.RECOMMENDATIONS(productId));
    return response.data;
};

export const checkHealth = async () => {
    const response = await client.get(ENDPOINTS.HEALTH);
    return response.data;
};
