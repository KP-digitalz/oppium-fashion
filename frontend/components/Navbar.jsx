import React from "react";
import Link from "next/link";
import Image from "next/image";
import { Bars3Icon } from "@heroicons/react/24/solid";
import { MagnifyingGlassIcon } from "@heroicons/react/24/outline";
import { UserIcon } from "@heroicons/react/24/outline";
import { ShoppingBagIcon } from "@heroicons/react/24/outline";
import Logo from "../public/oppium_logo.gif";

const Navbar = () => {
  return (
    <nav>
      <div className="grid grid-cols-3 p-9 items-center">
        <Link href="/" prefetch={false}>
          <Image alt="" src={Logo} />
        </Link>

        <div className="flex items-center justify-center space-x-10">
          <Link href="/women" prefetch={false}>
            Women
          </Link>
          <Link href="/men" prefetch={false}>
            Men
          </Link>
          <Link href="/discounts" prefetch={false}>
            Discounts
          </Link>
        </div>

        <div className="flex items-center justify-end space-x-4">
          <MagnifyingGlassIcon className="h-5 w-5 cursor-pointer" />
          <ShoppingBagIcon className="h-5 w-5 cursor-pointer" />
          <UserIcon className="h-5 w-5 cursor-pointer" />
          {/* <Bars3Icon className="hidden md:inline h-6 w-6 cursor-pointer" /> */}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
