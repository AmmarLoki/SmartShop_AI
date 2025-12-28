import React from 'react';
import Card from '../components/Card';

const HomePage = () => {
    return (
        <div className="container animate-fade-in">
            <div className="text-center py-5">
                <h1 className="font-bold" style={{ fontSize: '2.5rem', color: 'var(--color-primary)' }}>
                    SmartShop AI
                </h1>
                <p className="text-muted" style={{ fontSize: '1.25rem' }}>
                    Your intelligent shopping assistant for natural language product discovery
                </p>
            </div>

            <div className="d-flex justify-center">
                <Card className="w-100" style={{ maxWidth: '600px' }}>
                    <p className="text-center text-muted">
                        Search functionality coming in the next step...
                    </p>
                </Card>
            </div>
        </div>
    );
};

export default HomePage;
