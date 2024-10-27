import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import TresEnLinea from './componentes/Juegos/TresEnLinea'
import Home from './componentes/Juegos/Home'
import App from './App'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
  </StrictMode>
)
