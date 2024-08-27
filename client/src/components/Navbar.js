import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-white bg-opacity-50 backdrop-blur-md p-4 shadow-md sticky top-0 z-50">
      <div className="container mx-auto flex items-center">
        <Link to="/home" className="flex items-center space-x-4">
          <img src={"./app_logo.png"} alt="App Logo" className="h-20" />
        </Link>
        <div className="flex-grow flex justify-center space-x-12">
          <Link
            to="/home"
            className="text-black font-semibold px-4 py-2 rounded-md transition duration-300 hover:bg-black hover:text-white"
          >
            Home
          </Link>
          <Link
            to="/profile"
            className="text-black font-semibold px-4 py-2 rounded-md transition duration-300 hover:bg-black hover:text-white"
          >
            Profile
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
