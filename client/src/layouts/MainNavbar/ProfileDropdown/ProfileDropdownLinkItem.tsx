import { Menu } from "@headlessui/react";
import classNames from "classnames";
import { Fragment } from "react";
import { Link } from "react-router-dom";
import type { IDropdownLink } from "./dropdownLinks";

export const ProfileDropdownLinkItem = ({ link }: { link: IDropdownLink }) => {
  /* Use the `active` state to conditionally style the active item. */
  return (
    <Menu.Item as={Fragment}>
      {({ active }) => (
        <Link
          to={link.href}
          className={classNames(
            active ? "bg-violet-500 text-white" : "text-gray-900",
            "group flex w-full items-center rounded-md px-2 py-2 text-sm"
          )}
        >
          {link.label}
        </Link>
      )}
    </Menu.Item>
  );
};
