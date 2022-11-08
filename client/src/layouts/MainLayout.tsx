import { PropsWithChildren } from "react";
import { MainFooter } from "./MainFooter/MainFooter";
import { MainNavbar } from "./MainNavbar/MainNavbar";

export const MainLayout = ({ children }: PropsWithChildren) => {
  return (
    <div className="min-h-screen flex flex-col">
      <MainNavbar />
      <main className="flex-grow">{children}</main>
      <MainFooter />
    </div>
  );
};
