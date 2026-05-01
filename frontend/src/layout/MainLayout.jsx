import { Outlet } from 'react-router-dom';
import Navigation from '../components/Navigation';

function MainLayout() {
  return (
    <div className="app-shell">
      <Navigation />
      <main className="page-container">
        <Outlet />
      </main>
    </div>
  );
}

export default MainLayout;
