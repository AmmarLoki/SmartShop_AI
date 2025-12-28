import React from 'react';
import '../styles/variables.css';
import '../styles/animations.css';

const Loader = () => {
    return (
        <div className="d-flex justify-center align-center p-4">
            <div className="spinner"></div>
        </div>
    );
};

export default Loader;
