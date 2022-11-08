import { Link } from "react-router-dom";
import { ProfileDropdown } from "./ProfileDropdown/ProfileDropdown";

export const MainNavbar = () => {
  return (
    <nav className="w-full h-20 flex justify-between items-center px-8 z-10">
      <h1 className="text-2xl font-bold">
        <Link to="/">EAtHome</Link>
      </h1>

      <ul className="flex items-center">
        <li>
          <Link
            to="/shop"
            className="p-4 cursor-pointer hover:text-primary rounded-lg"
          >
            Shop
          </Link>
        </li>
        <li className="p-4">
          <ProfileDropdown />
        </li>
      </ul>
    </nav>
  );
};
