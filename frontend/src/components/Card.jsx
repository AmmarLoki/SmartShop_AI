import React from 'react';
import PropTypes from 'prop-types';
import clsx from 'clsx';
import '../styles/global.css';

const Card = ({ children, className, ...props }) => {
    return (
        <div className={clsx('card', className)} {...props}>
            {children}
        </div>
    );
};

Card.propTypes = {
    children: PropTypes.node.isRequired,
    className: PropTypes.string,
};

export default Card;
