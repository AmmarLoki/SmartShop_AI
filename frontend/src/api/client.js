import axios from 'axios';

const client = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || '/api/v1',
    headers: {
        'Content-Type': 'application/json',
    },
});

// Response interceptor for error handling
client.interceptors.response.use(
    (response) => response,
    (error) => {
        // Handle specific error cases here (e.g., 401 Unauthorized)
        if (error.response) {
            console.error('API Error:', error.response.data);
        } else {
            console.error('Network Error:', error.message);
        }
        return Promise.reject(error);
    }
);

export default client;
