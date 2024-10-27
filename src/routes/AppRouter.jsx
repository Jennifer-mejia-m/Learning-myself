import { createBrowserRouter } from "react-router-dom";
import Home from "../componentes/Juegos/Home";
import TresEnLinea from "../componentes/Juegos/TresEnLinea";
import NotFound from "../componentes/Juegos/NotFound";

export const AppRouter = createBrowserRouter([
    {
        path: '/',
        element: <Home />
    },
    {
        path: '/jugar',
        element: <TresEnLinea />
    },
    {
        path: '*',
        element: <NotFound />
    }
]);