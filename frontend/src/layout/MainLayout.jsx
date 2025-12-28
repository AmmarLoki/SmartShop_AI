import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import '../styles/global.css';

const MainLayout = () => {
    return (
        <div className="d-flex flex-column" style={{ minHeight: '100vh' }}>
            <header style={{ borderBottom: '1px solid var(--border-color)', padding: '1rem 0', backgroundColor: 'var(--bg-surface)' }}>
                <div className="container d-flex justify-between align-center">
                    <Link to="/" style={{ fontSize: '1.25rem', fontWeight: 'bold' }}>
                        SmartShop AI
                    </Link>
                    <nav className="d-flex gap-md">
                        <Link to="/" className="text-secondary">Home</Link>
                    </nav>
                </div>
            </header>

            <main style={{ flex: 1, padding: '2rem 0' }}>
                <Outlet />
            </main>

            <footer style={{ borderTop: '1px solid var(--border-color)', padding: '1.5rem 0', marginTop: 'auto', backgroundColor: 'var(--bg-surface)' }}>
                <div className="container text-center text-muted text-sm">
                    &copy; {new Date().getFullYear()} SmartShop AI. All rights reserved.
                </div>
            </footer>
        </div>
    );
};

export default MainLayout;
