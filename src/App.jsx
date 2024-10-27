import { useState } from "react";
import Home from "./componentes/Juegos/Home";
import { RouterProvider } from "react-router-dom";
import {AppRouter} from './routes/AppRouter'

function App(){
    return (
       <RouterProvider router={AppRouter}></RouterProvider>
       
    )
}

export default App