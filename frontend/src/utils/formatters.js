import { APP_CONSTANTS } from './constants';

export const formatPrice = (price, currency = APP_CONSTANTS.CURRENCY_SYMBOL) => {
    if (price === null || price === undefined) return 'N/A';
    return `${currency}${Number(price).toFixed(2)}`;
};

export const truncateText = (text, maxLength = 100) => {
    if (!text) return '';
    if (text.length <= maxLength) return text;
    return `${text.slice(0, maxLength)}...`;
};

export const formatDate = (dateString) => {
    if (!dateString) return '';
    return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });
};
