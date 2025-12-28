export const isValidUrl = (string) => {
    try {
        new URL(string);
        return true;
    } catch {
        return false;
    }
};

export const isValidPrice = (price) => {
    return !isNaN(parseFloat(price)) && isFinite(price) && Number(price) >= 0;
};

export const isNotEmpty = (value) => {
    return value !== null && value !== undefined && value.trim() !== '';
};
