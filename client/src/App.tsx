import { Route, Routes } from "react-router-dom";
import Navbar from "./layouts/Navbar/Navbar";

function App() {
  return (
    <div>
      <Navbar />
      <Routes>
        <Route path="/" element={<h1>home</h1>} />
        <Route path="/account-settings" element={<h1>account-settings</h1>} />
        <Route path="*" element={<h1>Not Found</h1>} />
      </Routes>
    </div>
  );
}

export default App;
