import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import '../styles/global.css';

const Button = ({
    children,
    variant = 'primary',
    className,
    isLoading,
    disabled,
    ...props
}) => {
    return (
        <button
            className={clsx('btn', `btn-${variant}`, className)}
            disabled={disabled || isLoading}
            {...props}
        >
            {isLoading ? <span className="spinner" /> : children}
        </button>
    );
};

Button.propTypes = {
    children: PropTypes.node.isRequired,
    variant: PropTypes.oneOf(['primary', 'secondary', 'outline']),
    className: PropTypes.string,
    isLoading: PropTypes.bool,
    disabled: PropTypes.bool,
};

export default Button;
