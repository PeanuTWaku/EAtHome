import { PropsWithChildren } from "react";
import { MainFooter } from "./MainFooter/MainFooter";
import { MainNavbar } from "./MainNavbar/MainNavbar";

export const MainLayout = ({ children }: PropsWithChildren) => {
  return (
    <div className="h-full flex flex-col">
      <MainNavbar />
      <main className="flex-1 py-4">{children}</main>
      <MainFooter />
    </div>
  );
};
