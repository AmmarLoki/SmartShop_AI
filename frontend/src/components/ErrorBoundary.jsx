import React from 'react';
import PropTypes from 'prop-types';
import Button from './Button';

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null };
    }

    static getDerivedStateFromError(error) {
        return { hasError: true, error };
    }

    componentDidCatch(error, errorInfo) {
        console.error('ErrorBoundary caught an error:', error, errorInfo);
    }

    render() {
        if (this.state.hasError) {
            return (
                <div className="d-flex flex-column align-center justify-center p-5 text-center">
                    <h2 className="text-danger mb-4">Something went wrong</h2>
                    <p className="text-muted mb-4">{this.state.error?.message || 'Unexpected error occurred'}</p>
                    <Button onClick={() => window.location.reload()}>
                        Reload Page
                    </Button>
                </div>
            );
        }

        return this.props.children;
    }
}

ErrorBoundary.propTypes = {
    children: PropTypes.node.isRequired,
};

export default ErrorBoundary;
