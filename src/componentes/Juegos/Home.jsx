import { Link } from "react-router-dom"

function Home() {
  return (
    <>
        <div>
            <h3>Hola, vamos a jugar tres en línea</h3>
            <h4>estás listo?</h4>
        </div>
        <div>
            <Link to="/jugar">Jugar</Link>
        </div>
    </>    
  )
}

export default Home

